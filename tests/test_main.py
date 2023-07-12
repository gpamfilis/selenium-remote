"""
Here live thy tests.
"""
from selenium_remote.main import main


def test_message():
    """
    This is a basic test.
    """
    assert main() == "This is a test"
