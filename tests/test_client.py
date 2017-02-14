import pytest

from pydial import DialClient

class TestSetup(object):
    def test_dummy(self):
        client = DialClient('dummy_url')
