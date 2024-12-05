import pytest
from utils.random_delay import random_wait
from unittest.mock import patch

def test_random_wait(monkeypatch):
    """
    Mock test the time.sleep function, to verify behavior without waiting.
    Assert that time.sleep is called with expected arguments.
    """
    min_wait = 1
    max_wait = 2

    # mock time.sleep function
    mock_sleep = patch('time.sleep').start()
    random_wait(min_wait, max_wait)

    # assert time.sleep was called once with arg within expected range
    mock_sleep.assert_called_once()
    args, kwargs = mock_sleep.call_args
    assert min_wait <= args[0] <= max_wait



