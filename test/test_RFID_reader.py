#!/usr/bin/env python3

import pytest
import playbox
from unittest.mock import MagicMock


def test_RFID_Reader_setup():
    player = playbox.Player()
    player.connect = MagicMock()
    #mocker.patch.object(playbox.Player, 'connect', autospec=True)
    reader = playbox.RFID_Reader(player)
    player.connect.assert_called_once()
