# python -m app
from .app import (
    Log,
    Errors
)


if __name__ == "__main__":
    log = Log()
    print(log.check("Anything...", Errors.SUCCESS.name))
    print(log.check("Anything...", Errors.FAIL.name))
    print(log.check("Anything...", Errors.INFO.name))
