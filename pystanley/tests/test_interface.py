# Copyright Claudio Mattera 2019.
# Copyright Center for Energy Informatics 2018.
# Distributed under the MIT License.
# See accompanying file License.txt, or online at
# https://opensource.org/licenses/MIT

import json
from datetime import datetime, timezone
import asyncio

import pandas as pd
from pandas.util.testing import assert_series_equal

from pystanley import StanleyInterface
from .mockup import DummyTransportInterface


def test_fetch_readings() -> None:
    loop = asyncio.get_event_loop()

    start = datetime(2017, 1, 1, tzinfo=timezone.utc)
    end = datetime(2017, 10, 1, tzinfo=timezone.utc)
    path = "/some/path"

    transport_result = [
        {
            "path": str(path),
            "readings": [
                [1483228800000000000, 5.0],
                [1485907200000000000, 8.0],
                [1488326400000000000, 12.0],
                [1491004800000000000, -5.3]
            ]
        }
    ]

    expected_result = pd.Series(
        [5.0, 8.0, 12.0, -5.3],
        index=pd.to_datetime(
            [
                datetime(2017, 1, 1, tzinfo=timezone.utc),
                datetime(2017, 2, 1, tzinfo=timezone.utc),
                datetime(2017, 3, 1, tzinfo=timezone.utc),
                datetime(2017, 4, 1, tzinfo=timezone.utc),
            ],
            utc=True
        ),
        name=str(path)
    )

    expected_fetch_params = {
        "paths": path,
        "start": str(int(start.timestamp() * 10**9)),
        "end": str(int(end.timestamp() * 10**9)),
    }

    transport_interface = DummyTransportInterface(json.dumps(transport_result))
    stanley = StanleyInterface(transport_interface)

    result = loop.run_until_complete(
        stanley.fetch_readings(start, end, set([path]))
    )

    assert transport_interface.received_fetch_params == expected_fetch_params

    assert len(result) == 1
    assert list(result.keys())[0] == path
    assert_series_equal(list(result.values())[0], expected_result)


def test_post_readings() -> None:
    loop = asyncio.get_event_loop()

    path = "/some/path"
    series = pd.Series(
        [5.0, 8.0, 12.0, -5.3],
        index=pd.to_datetime(
            [
                datetime(2017, 1, 1, tzinfo=timezone.utc),
                datetime(2017, 2, 1, tzinfo=timezone.utc),
                datetime(2017, 3, 1, tzinfo=timezone.utc),
                datetime(2017, 4, 1, tzinfo=timezone.utc),
            ],
            utc=True
        ),
        name=str(path)
    )

    transport_result = ""

    expected_data = [
        {
            "path": str(path),
            "readings": [
                [1483228800000000000, 5.0],
                [1485907200000000000, 8.0],
                [1488326400000000000, 12.0],
                [1491004800000000000, -5.3]
            ]
        }
    ]

    transport_interface = DummyTransportInterface(transport_result)
    stanley = StanleyInterface(transport_interface)

    loop.run_until_complete(
        stanley.post_readings((path, series))
    )

    assert transport_interface.received_post_data == expected_data
