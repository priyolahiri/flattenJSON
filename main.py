import json
import sys


def flatten(nested_data: dict) -> dict:
    """
    Meta-function for flattening
    Flattens a given dict with nested structure to a flat dict with no
    hierarchy
    :param nested_data: dict we want to flatten
    :return: the flattened dict
    """
    flattened_dict = {}

    def _construct_key(old_key: str, new_key: str) -> str:
        """
        Concatenates old_key, separator '.', and new_key
        :param old_key: original key
        :param new_key: new key
        :return: the final key
        """
        if old_key:
            return u"{}{}{}".format(old_key, ".", new_key)
        else:
            return new_key

    def _flatten(object_, key):
        """
        The actual flatting happens here and this takes care of recursion when there
        are multiple levels of dicts
        Calls itself for dict objects within other types assigns the object_ to
        the corresponding key in the global flattened_dict
        Exits if a list of list like object is encountered
        :param object_: the object
        :param key: the key
        """
        if not object_:
            flattened_dict[key] = object_
        elif isinstance(object_, dict):
            for object_key in object_:
                _flatten(
                    object_[object_key],
                    _construct_key(
                        key,
                        object_key))
        elif isinstance(object_, (list, set, tuple)):
            raise Exception("List objects are not allowed.")
        else:
            flattened_dict[key] = object_

    _flatten(nested_data, None)
    return flattened_dict


if __name__ == '__main__':
    try:
        json_data = json.load(sys.stdin)
    except ValueError:
        raise Exception("Invalid JSON")
    print(json.dumps(flatten(json_data)))
