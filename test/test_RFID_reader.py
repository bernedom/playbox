#!/usr/bin/env python3

import pytest
import playbox
from unittest.mock import MagicMock


@pytest.fixture
def construct_rfid_reader():
    player = playbox.Player()
    player.connect = MagicMock()
    #mocker.patch.object(playbox.Player, 'connect', autospec=True)
    reader = playbox.RFID_Reader(player)
    player.connect.assert_called_once()
    return reader


def test_RFID_Reader_construction(construct_rfid_reader):
    reader = construct_rfid_reader
    assert not reader.hasDeviceAqcuired()
    assert reader.device_id == ''
