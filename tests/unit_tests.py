from os import path
from unittest import TestCase, TestLoader, TestSuite, TextTestRunner
import sys

ROOT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__), '..'
    )
)
sys.path.append(ROOT_FOLDER)

from app.lib.twin_chatter import TwinChatter


class TwinChatterResponseTests(TestCase):
    def setUp(self):
        self.twin_chatter = TwinChatter()

    def test(self):
        ...


if __name__ == '__main__':
    test_loader = TestLoader()
    test_suite = TestSuite()
    test_runner = TextTestRunner()

    test_suite.addTest(
        test_loader.loadTestsFromTestCase(TwinChatterResponseTests)
    )

    test_runner.run(test_suite)
