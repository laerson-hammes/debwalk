from colorama import (  # type: ignore
    Fore,
    init
)
from typing import Optional
import enum


class Errors(enum.Enum):

    INFO: str = f"{Fore.YELLOW}[!]"
    SUCCESS: str = f"{Fore.GREEN}[+]"
    FAIL: str = f"{Fore.RED}[-]"


class Log():

    def __init__(self, /, *, debug: bool = True, rtr = True) -> None:
        self.debug: bool = debug
        self.rtr: bool = rtr
        if self.debug:
            init(autoreset=True)

    def check(self, message: str, error: str) -> Optional[str]:
        if self.debug:
            if self.rtr:
                return f"{Errors[error.upper()].value} {message.upper()}"
            print(f"{Errors[error.upper()].value} {message.upper()}")
        return None
