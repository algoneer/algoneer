import hashlib

hashfunc = hashlib.sha256
# a version prefix (for future use)
prefix = b"\1\0\0\0"


class Hasher(object):
    def __init__(self):
        self.digest = hashfunc()

    def add(self, value):
        if isinstance(value, str):
            v = value.encode("utf-8", "ignore")
        elif isinstance(value, (bytes)):
            v = str(value, errors="replace").encode("utf-8", "ignore")
        elif isinstance(value, (int, float, complex, bool)):
            v = bytes(str(value).encode("utf-8"))
        elif isinstance(value, (tuple, list)):
            for v in value:
                self.add(v)
            return
        elif isinstance(value, dict):
            for key, v in sorted(value.items(), key=lambda x: x[0]):
                self.add(key)
                self.add(v)
            return
        elif value is None:
            v = b"1bcdadabdf0de99dbdb747e951e967c5"
        else:
            raise AttributeError("Unhashable type: %s" % str(type(value)))

        self.digest.update(v)

    def digest(self):
        return self.digest


def get_hash(node, fields=None, exclude=[]):
    """
    Here we generate a unique hash for a given node in the syntax tree.
    """

    hasher = Hasher()

    def add_to_hash(value):

        if isinstance(value, dict):
            for key, v in sorted(value.items(), key=lambda x: x[0]):

                if (fields is not None and key not in fields) or (
                    exclude is not None and key in exclude
                ):
                    continue
                add_to_hash(key)
                add_to_hash(v)
        elif (
            isinstance(value, (tuple, list)) and value and isinstance(value[0], (dict))
        ):
            for i, v in enumerate(value):
                hasher.add(i)
                add_to_hash(v)
        else:
            hasher.add(value)

    add_to_hash(node)

    return prefix + hasher.digest.digest()
