from selenium_remote.main import main

def test_message():
    assert main() == 'This is a test'