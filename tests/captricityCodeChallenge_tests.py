from nose.tools import *
from captricityCodeChallenge import *

def test_match():
    urls = match('sample.log')
    assert_equal(urls[0], '/document')
    assert_equal(urls[-1], '/accounts/alice')
    assert_equal(urls[10], '/api/shreddr/job/12359')
    assert_equal(urls[-9], '/api/shreddr/shred')

# tests that urls contains the correct number of elements
def test_match_lines():
    urls = match('sample.log')
    assert_equal(len(urls), 106)

def test_parse_web_log_len():
    result = parseWebLog('sample.log', 10)
    assert_equal(len(result), 10)

def test_parse_web_log_result():
    result = parseWebLog('sample.log', 1)
    assert_equal(result[0][0], '/job/upload')
    assert_equal(result[0][1], 18)

def test_parse_web_log_large_n():
    result = parseWebLog('sample.log', 20)
    assert_equal(len(result), 15)

def test_parse_web_log_no_n():
    result = parseWebLog('sample.log')
    assert_equal(len(result), 15)

