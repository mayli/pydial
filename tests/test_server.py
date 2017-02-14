import pytest

from pydial import DialServer, SSDPServer

class TestSetup(object):
    def test_dummy(self):
        dial_server = DialServer()
        ssdp_server = SSDPServer('dummy_url', 'localhost')
