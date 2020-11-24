#!/usr/bin/env python3

import pytest
import playbox

from mpd import MPDClient
import mpd
from unittest.mock import MagicMock, patch


@patch('mpd.MPDClient.connect')
@patch('mpd.MPDClient.fileno', **{'return_value.raiseError.side_effect': mpd.base.ConnectionError()})
def test_player_connects_if_not_already_connected(mock_mpd_connect, mock_mpd_fileno):

    player = playbox.Player(playbox.AudioLibrary())
    player.connect()
    mock_mpd_connect.assert_called_once()
