# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2020-01-15 11:37:48
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-15 20:20:14
import pytest

# In order to create a reusable marker.
# content of pytest.ini
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
