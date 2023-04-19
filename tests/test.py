from unittest import TestCase
from main.app import (
    Log,
    Errors
)


class TestLog(TestCase):

    def test_check_with_debug_false(self):
        log = Log(debug=False)
        message: str = "test_check_with_debug_false"
        self.assertEqual(
            log.check(message, Errors.FAIL.name),
            None
        )

    def test_check_with_return(self):
        log = Log()
        message: str = "test_check_with_return"
        self.assertEqual(
            log.check(message, Errors.FAIL.name),
            f"{Errors.FAIL.value} {message.upper()}"
        )

    def test_check_with_rtr_false(self):
        log = Log(rtr=False)
        message: str = "test_check_with_rtr_false"
        self.assertEqual(
            log.check(message, Errors.FAIL.name),
            None
        )
