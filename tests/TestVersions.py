from nose.tools import assert_equal, assert_not_equal, assert_raises, raises, with_setup
from nose.plugins.attrib import attr

from unittest import TestCase
import os, shutil, json, sys

sys.path.insert(0, ".")
from TestMaker.core import TestMaker

class TestVersions(TestCase):
    def setUp(self):
        "set up test fixtures"
        pass

    def teardown(self):
        "tear down test fixtures"
        pass

    def test_create(self):
        m = TestMaker(filename="/Users/idm/Code/psyc85-f12-final/conf/fall-final.json")
        m.load_questions()

    @attr('online')
    def test_false(self):
        assert False
