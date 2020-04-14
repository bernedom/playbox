#!/usr/bin/env python3

import pytest
import playbox
from mpd import MPDClient
from unittest.mock import MagicMock, patch


@patch('mpd.MPDClient.connect')
def test_player_connection_to_mpd(mock_mpd_connect):
    player = playbox.Player()
    player.connect()
    mock_mpd_connect.assert_called_once()
