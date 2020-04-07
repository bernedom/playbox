#!/usr/bin/env python3

import pytest
import playbox


def test_RFID_Reader_setup(mocker):
    mocker.patch('playbox.Player.Player.connect', autospec=True)
    #mocker.patch.object(playbox.Player, 'connect', autospec=True)
    reader = playbox.RFID_Reader.RFID_Reader()
    playbox.Player.Player.connect.assert_called_once()
