#!/usr/bin/env python3

import pytest
import playbox

from mpd import MPDClient
import mpd
from unittest.mock import MagicMock, patch


@patch('mpd.MPDClient.connect')
def test_player_connects_if_not_already_connected(mock_mpd_connect):

    player = playbox.Player(playbox.AudioLibrary())
    player.isConnected = MagicMock(return_value=False)
    player.connect()
    mock_mpd_connect.assert_called_once()


@patch('mpd.MPDClient.connect')
def test_player_does_not_connect_if_already_connected(mock_mpd_connect):

    player = playbox.Player(playbox.AudioLibrary())
    player.isConnected = MagicMock(return_value=False)
    player.connect()
    mock_mpd_connect.assert_called_once()
