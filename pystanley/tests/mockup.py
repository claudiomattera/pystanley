# Copyright Claudio Mattera 2019.
# Copyright Center for Energy Informatics 2018.
# Distributed under the MIT License.
# See accompanying file License.txt, or online at
# https://opensource.org/licenses/MIT

import typing

from pystanley.types import JsonType
from pystanley.transport import TransportInterface


class DummyTransportInterface(TransportInterface):
    """docstring for DummyTransportInterface"""
    def __init__(
                self,
                result: typing.Text,
            ) -> None:
        super(DummyTransportInterface, self).__init__()

        self.result = result

    async def post_data(
                self,
                data: JsonType,
            ) -> None:
        self.received_post_data = data

    async def fetch(
                self,
                params: typing.Dict[typing.Text, typing.Text]
            ) -> typing.Text:

        self.received_fetch_params = params

        return self.result
