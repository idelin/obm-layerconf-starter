"""A small flat configuration overlay utility."""
import copy


class ConfigError(Exception):
    def __init__(self, code, key=None, chain=None):
        self.code, self.key, self.chain = code, key, chain or []
        super().__init__(code)


def resolve(document):
    values = {key: copy.deepcopy(spec["default"])
              for key, spec in document["schema"].items() if "default" in spec}
    for layer in document.get("layers", []):
        for operation in layer["ops"]:
            if operation["op"] == "set":
                values[operation["key"]] = copy.deepcopy(operation["value"])
    return {"values": values}
