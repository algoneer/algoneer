""" Visualize the SHAP values with additive force style layouts.

Source: https://github.com/slundberg/shap/blob/master/shap/plots/force.py

Adapted to extract the required data for the D3 plots
"""

import os
import io
import string
import json
import random
from IPython.core.display import display, HTML  # type: ignore
from IPython import get_ipython  # type: ignore
import base64
import numpy as np
import scipy.cluster  # type: ignore
import sys

if sys.version_info[0] >= 3:
    from collections.abc import Sequence
else:
    from collections import Sequence

import warnings
import re
from shap.plots import labels
from shap.common import (
    convert_to_link,
    Instance,
    Model,
    Data,
    DenseData,
    Link,
    hclust_ordering,
)


def force_plot(
    base_value,
    shap_values,
    features=None,
    feature_names=None,
    out_names=None,
    link="identity",
    plot_cmap="RdBu",
    show=True,
    figsize=(20, 3),
    ordering_keys=None,
    ordering_keys_time_format=None,
    text_rotation=0,
):
    """ Visualize the given SHAP values with an additive force layout.
    
    Parameters
    ----------
    base_value : float
        This is the reference value that the feature contributions start from. For SHAP values it should
        be the value of explainer.expected_value.
    shap_values : numpy.array
        Matrix of SHAP values (# features) or (# samples x # features). If this is a 1D array then a single
        force plot will be drawn, if it is a 2D array then a stacked force plot will be drawn.
    features : numpy.array
        Matrix of feature values (# features) or (# samples x # features). This provides the values of all the
        features, and should be the same shape as the shap_values argument.
    feature_names : list
        List of feature names (# features).
    out_names : str
        The name of the outout of the model (plural to support multi-output plotting in the future).
    
    link : "identity" or "logit"
        The transformation used when drawing the tick mark labels. Using logit will change log-odds numbers
        into probabilities. 
    """

    # auto unwrap the base_value
    if type(base_value) == np.ndarray and len(base_value) == 1:
        base_value = base_value[0]

    if type(base_value) == np.ndarray or type(base_value) == list:
        if type(shap_values) != list or len(shap_values) != len(base_value):
            raise Exception(
                "In v0.20 force_plot now requires the base value as the first parameter! "
                "Try shap.force_plot(explainer.expected_value, shap_values) or "
                "for multi-output models try "
                "shap.force_plot(explainer.expected_value[0], shap_values[0])."
            )

    assert (
        not type(shap_values) == list
    ), "The shap_values arg looks looks multi output, try shap_values[i]."

    link = convert_to_link(link)

    if type(shap_values) != np.ndarray:
        return visualize(shap_values)

    # convert from a DataFrame or other types
    if str(type(features)) == "<class 'pandas.core.frame.DataFrame'>":
        if feature_names is None:
            feature_names = list(features.columns)
        features = features.values
    elif str(type(features)) == "<class 'pandas.core.series.Series'>":
        if feature_names is None:
            feature_names = list(features.index)
        features = features.values
    elif isinstance(features, list):
        if feature_names is None:
            feature_names = features
        features = None
    elif features is not None and len(features.shape) == 1 and feature_names is None:
        feature_names = features
        features = None

    if len(shap_values.shape) == 1:
        shap_values = np.reshape(shap_values, (1, len(shap_values)))

    if out_names is None:
        out_names = ["output value"]
    elif type(out_names) == str:
        out_names = [out_names]

    if shap_values.shape[0] == 1:
        if feature_names is None:
            feature_names = [
                labels["FEATURE"] % str(i) for i in range(shap_values.shape[1])
            ]
        if features is None:
            features = ["" for _ in range(len(feature_names))]
        if type(features) == np.ndarray:
            features = features.flatten()

        # check that the shape of the shap_values and features match
        if len(features) != shap_values.shape[1]:
            msg = "Length of features is not equal to the length of shap_values!"
            if len(features) == shap_values.shape[1] - 1:
                msg += (
                    " You might be using an old format shap_values array with the base value "
                    "as the last column. In this case just pass the array without the last column."
                )
            raise Exception(msg)

        instance = Instance(np.zeros((1, len(feature_names))), features)
        e = AdditiveExplanation(
            base_value,
            np.sum(shap_values[0, :]) + base_value,
            shap_values[0, :],
            None,
            instance,
            link,
            Model(None, out_names),
            DenseData(np.zeros((1, len(feature_names))), list(feature_names)),
        )

        return visualize(
            e, plot_cmap, figsize=figsize, show=show, text_rotation=text_rotation
        )

    else:

        if shap_values.shape[0] > 3000:
            warnings.warn(
                "shap.force_plot is slow for many thousands of rows, try subsampling your data."
            )

        exps = []
        for k in range(shap_values.shape[0]):
            if feature_names is None:
                feature_names = [
                    labels["FEATURE"] % str(i) for i in range(shap_values.shape[1])
                ]
            if features is None:
                display_features = ["" for i in range(len(feature_names))]
            else:
                display_features = features[k, :]

            instance = Instance(np.ones((1, len(feature_names))), display_features)
            e = AdditiveExplanation(
                base_value,
                np.sum(shap_values[k, :]) + base_value,
                shap_values[k, :],
                None,
                instance,
                link,
                Model(None, out_names),
                DenseData(np.ones((1, len(feature_names))), list(feature_names)),
            )
            exps.append(e)

        return visualize(
            exps,
            plot_cmap=plot_cmap,
            ordering_keys=ordering_keys,
            ordering_keys_time_format=ordering_keys_time_format,
            text_rotation=text_rotation,
        )


class Explanation:
    def __init__(self):
        pass


class AdditiveExplanation(Explanation):
    def __init__(
        self, base_value, out_value, effects, effects_var, instance, link, model, data
    ):
        self.base_value = base_value
        self.out_value = out_value
        self.effects = effects
        self.effects_var = effects_var
        assert isinstance(instance, Instance)
        self.instance = instance
        assert isinstance(link, Link)
        self.link = link
        assert isinstance(model, Model)
        self.model = model
        assert isinstance(data, Data)
        self.data = data


def ensure_not_numpy(x):
    if isinstance(x, bytes):
        return x.decode()
    elif isinstance(x, np.str):
        return str(x)
    elif isinstance(x, np.generic):
        return float(x.item())
    else:
        return x


def verify_valid_cmap(cmap):
    assert (
        isinstance(cmap, str)
        or isinstance(cmap, list)
        or str(type(cmap)).endswith("unicode'>")
    ), "Plot color map must be string or list! not: " + str(type(cmap))
    if isinstance(cmap, list):
        assert len(cmap) > 1, "Color map must be at least two colors."
        _rgbstring = re.compile(r"#[a-fA-F0-9]{6}$")
        for color in cmap:
            assert bool(_rgbstring.match(color)), "Invalid color found in CMAP."

    return cmap


def visualize(
    e,
    plot_cmap="RdBu",
    figsize=(20, 3),
    show=True,
    ordering_keys=None,
    ordering_keys_time_format=None,
    text_rotation=0,
):
    plot_cmap = verify_valid_cmap(plot_cmap)
    if isinstance(e, AdditiveExplanation):
        return AdditiveForceVisualizer(e, plot_cmap=plot_cmap).data
    elif isinstance(e, Explanation):
        return SimpleListVisualizer(e).data
    elif (
        isinstance(e, Sequence) and len(e) > 0 and isinstance(e[0], AdditiveExplanation)
    ):
        return AdditiveForceArrayVisualizer(
            e,
            plot_cmap=plot_cmap,
            ordering_keys=ordering_keys,
            ordering_keys_time_format=ordering_keys_time_format,
        ).data
    else:
        assert (
            False
        ), "visualize() can only display Explanation objects (or arrays of them)!"


try:
    # register the visualize function with IPython
    ip = get_ipython()
    svg_formatter = ip.display_formatter.formatters["text/html"]
    svg_formatter.for_type(Explanation, lambda x: visualize(x).data)
    old_list_formatter = svg_formatter.for_type(list)

    def try_list_display(e):
        if (
            isinstance(e, Sequence)
            and len(e) > 0
            and isinstance(e[0], AdditiveExplanation)
        ):
            return visualize(e).data
        else:
            return str(e) if old_list_formatter is None else old_list_formatter(e)

    svg_formatter.for_type(list, try_list_display)
except:
    pass


class SimpleListVisualizer:
    def __init__(self, e):
        assert isinstance(
            e, Explanation
        ), "SimpleListVisualizer can only visualize Explanation objects!"

        # build the json data
        features = {}
        for i in filter(lambda j: e.effects[j] != 0, range(len(e.data.group_names))):
            features[i] = {
                "effect": e.effects[i],
                "value": e.instance.group_display_values[i],
            }
        self.data = {
            "outNames": e.model.out_names,
            "base_value": e.base_value,
            "link": str(e.link),
            "featureNames": e.data.group_names,
            "features": features,
            "plot_cmap": e.plot_cmap.plot_cmap,
        }


class AdditiveForceVisualizer:
    def __init__(self, e, plot_cmap="RdBu"):
        assert isinstance(
            e, AdditiveExplanation
        ), "AdditiveForceVisualizer can only visualize AdditiveExplanation objects!"

        # build the json data
        features = {}
        for i in filter(lambda j: e.effects[j] != 0, range(len(e.data.group_names))):
            features[i] = {
                "effect": ensure_not_numpy(e.effects[i]),
                "value": ensure_not_numpy(e.instance.group_display_values[i]),
            }
        self.data = {
            "outNames": e.model.out_names,
            "baseValue": ensure_not_numpy(e.base_value),
            "outValue": ensure_not_numpy(e.out_value),
            "link": str(e.link),
            "featureNames": e.data.group_names,
            "features": features,
            "plot_cmap": plot_cmap,
        }


class AdditiveForceArrayVisualizer:
    def __init__(
        self, arr, plot_cmap="RdBu", ordering_keys=None, ordering_keys_time_format=None
    ):
        assert isinstance(
            arr[0], AdditiveExplanation
        ), "AdditiveForceArrayVisualizer can only visualize arrays of AdditiveExplanation objects!"

        # order the samples by their position in a hierarchical clustering
        if all([e.model.f == arr[1].model.f for e in arr]):
            clustOrder = hclust_ordering(np.vstack([e.effects for e in arr]))
        else:
            assert (
                False
            ), "Tried to visualize an array of explanations from different models!"

        # make sure that we put the higher predictions first...just for consistency
        if sum(arr[clustOrder[0]].effects) < sum(arr[clustOrder[-1]].effects):
            np.flipud(clustOrder)  # reverse

        # build the json data
        clustOrder = np.argsort(clustOrder)  # inverse permutation
        self.data = {
            "outNames": arr[0].model.out_names,
            "baseValue": ensure_not_numpy(arr[0].base_value),
            "link": arr[0].link.__str__(),
            "featureNames": arr[0].data.group_names,
            "explanations": [],
            "plot_cmap": plot_cmap,
            "ordering_keys": list(ordering_keys)
            if hasattr(ordering_keys, "__iter__")
            else None,
            "ordering_keys_time_format": ordering_keys_time_format,
        }
        for (ind, e) in enumerate(arr):
            self.data["explanations"].append(
                {
                    "outValue": ensure_not_numpy(e.out_value),
                    "simIndex": ensure_not_numpy(clustOrder[ind]) + 1,
                    "features": {},
                }
            )
            for i in filter(
                lambda j: e.effects[j] != 0 or e.instance.x[0, j] != 0,
                range(len(e.data.group_names)),
            ):
                self.data["explanations"][-1]["features"][i] = {
                    "effect": ensure_not_numpy(e.effects[i]),
                    "value": ensure_not_numpy(e.instance.group_display_values[i]),
                }
