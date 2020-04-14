#!/usr/bin/env python3

import pytest
import playbox
from mpd import MPDClient


def test_player_connection_to_mpd(mocker):
    mocker.patch('mpd.MPDClient.connect')
    player = playbox.Player()
    player.connect()
    MPDClient.connect.assert_called_once()
