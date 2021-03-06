"""Base class for test harness TestCases."""

from typing import Any
from unittest import TestCase as BaseTestCase

from simple_test.runner import Runner


class TestCase(BaseTestCase):
    """Base class for test harness TestCases."""

    def __init__(self, runner: Runner, **_: Any) -> None:
        super().__init__()

        self.runner = runner
