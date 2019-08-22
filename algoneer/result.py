import abc


class Result(abc.ABC):
    pass


class DatasetVersionResult(Result):
    """
    Describes a result that applies to a given dataset version.
    """

    pass


class AlgorithmVersionResult(Result):
    """
    Describes a result that applies to a given algorithm version.
    """

    pass


class ModelResult(Result):
    """
    Describes a result that applies to a given model.
    """

    pass
