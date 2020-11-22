#!/usr/bin/env python3

import pytest
import playbox
from unittest.mock import MagicMock
import evdev


@pytest.fixture
def construct_rfid_reader():
    player = playbox.Player(MagicMock())
    # mocker.patch.object(playbox.Player, 'connect', autospec=True)
    reader = playbox.RFID_Reader(player)

    return reader


def test_RFID_Reader_construction(construct_rfid_reader):
    reader = construct_rfid_reader
    assert not reader.hasDeviceAqcuired()
    assert reader.device_id == ''


# @patch('evdev.list_devices', lambda *args: ['/dev/input/event20', '/dev/input/event19'])
# @patch('evdev.InputDevice')
# def test_RFID_Reader_aqcuire_device(input_device_class, construct_rfid_reader):
#     input_device_class = MagicMock()
#     mockinstance = input_device_class.return_value
#     mockinstance.path = '/dev/input/event20'
#     mockinstance.name = PropertyMock(return_value='mock device')
#     reader = construct_rfid_reader
#     reader.aqcuireDevice('mock device')
#     assert reader.hasDeviceAqcuired() == True
