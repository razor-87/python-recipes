# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2020-01-15 11:37:48
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-26 17:58:51
"""
pytest --cov-report term --cov=.
pytest --cov=.
pytest --durations=10                          # list of the slowest 10 test durations.
pytest --ff                                    # run the failures first and then the rest of the tests
pytest --ignore */*/file.py
pytest --instafail                             # if pytest-instafail is installed, show errors and failures instantly instead of waiting until the end of test suite.
pytest --lf                                    # only re-run the failures
pytest --markers                               # show available markers
pytest --maxfail=2                             # stop after two failures
pytest --maxfail=2 -rf                         # exit after 2 failures, report fail info.
pytest --showlocals                            # show local variables in tracebacks
pytest --tb=line                               # only one line per failure
pytest --tb=long                               # the default informative traceback formatting
pytest --tb=native                             # the Python standard library formatting
pytest --tb=no                                 # no tracebak output
pytest --tb=short                              # a shorter traceback format
pytest --traceconfig                           # find out which py.test plugins are active in your environment.
pytest -h --fixtures
pytest -k "TestClass and not test_one"         # only run tests with names that match the "string expression"
pytest -l                                      # (shortcut)
pytest -m slowest                              # run tests with decorator @pytest.mark.slowest or slowest = pytest.mark.slowest; @slowest
pytest -n 4                                    # send tests to multiple CPUs
pytest -q test_sample.py                       # omit filename output
pytest -x                                      # stop after first failure
pytest -x --pdb                                # drop to PDB on first failure, then end test session
pytest test_sample.py --collect-only           # collects information test suite
pytest test_sample.py -v                       # outputs verbose messages
pytest test_server.py::TestClass::test_method  # cnly run tests that match the node ID
"""
import pytest

# pytest.ini
# [pytest]
# markers =
#     webtest: mark a test as a webtest.

# conftest.py
# pytest_plugins = ["pytester", "aiohttp.pytest_plugin", "pytest_mock"]

# @pytest.fixture(scope='')
# @pytest.fixture(autouse=True)
# @pytest.fixture(params=[])
# @pytest.yield_fixture(scope='')
# @pytest.mark.parametrize
# @pytest.mark.skipif
# @pytest.mark.asyncio
# @pytest.mark.xfail


def test(capsys):
    out, err = capsys.readouterr()
    with capsys.disabled(): ...

def test(monkeypatch): ...

def test(tmpdir): ...

with pytest.raises('Error'): ...

# Test using parametrize
@pytest.mark.parametrize(('n', 'expected'), [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    pytest.mark.xfail((1, 0)),
    pytest.mark.xfail(reason="some bug")((1, 0)),
    pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
])
def test_increment(n, expected):
    assert n + 1 == expected
