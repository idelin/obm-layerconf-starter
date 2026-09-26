import json
import sys
from . import ConfigError, resolve


def main():
    try:
        result = resolve(json.load(sys.stdin))
    except ConfigError as error:
        json.dump({"error": error.code, "key": error.key, "chain": error.chain}, sys.stdout)
        sys.stdout.write("\n")
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
