import pytest
import os
from rrc_statewide_api import RRCStatewideParser
from rrc_statewide_api.utils import construct_api_number, format_district

def test_api_number_construction():
    assert construct_api_number(105, 12345) == "105-12345"
    assert construct_api_number("105", "12345") == "105-12345"

def test_district_formatting():
    assert format_district(1) == "01"
    assert format_district("1") == "01"
    assert format_district("8A") == "8A"

def test_parser_init():
    # Just testing instantiation doesn't crash
    parser = RRCStatewideParser("dummy.dbf")
    assert parser.dbf_path == "dummy.dbf"
    assert parser.encoding == "iso-8859-1"
