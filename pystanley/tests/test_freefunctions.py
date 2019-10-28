# Copyright Claudio Mattera 2019.
# Copyright Center for Energy Informatics 2018.
# Distributed under the MIT License.
# See accompanying file License.txt, or online at
# https://opensource.org/licenses/MIT

from datetime import datetime, timezone

import pandas as pd
from pandas.util.testing import assert_series_equal

import pystanley


def test_parse_readings() -> None:
    path = "/some/path"
    readings = [
        [1484006400000000000, 12],
        [1491004800000000000, -34],
        [1491523200000000000, 53]
    ]

    expected = pd.Series(
        [12, -34, 53],
        index=pd.to_datetime([
                1484006400000,
                1491004800000,
                1491523200000,
            ],
            unit="ms",
            utc=True
        ),
        name=str(path)
    )

    actual = pystanley._parse_readings(path, readings)

    assert_series_equal(actual, expected)


def test_to_nanos_timestamp() -> None:
    expected = 1491004800000000000
    actual = pystanley._to_nanos_timestamp(datetime(2017, 4, 1, tzinfo=timezone.utc))

    assert expected == actual


def test_intertwine_series() -> None:
    a = pd.Series([1, 2, 3, 4], index=[1, 3, 4, 9])
    b = pd.Series([5, 6, 7, 8], index=[2, 3, 8, 9])

    expected = pd.Series([1, 5, 2, 3, 7, 4], index=[1, 2, 3, 4, 8, 9])

    actual = pystanley.intertwine_series((i for i in [a, b]))

    assert_series_equal(actual, expected)
