#!/usr/bin/env python3

import pytest
import playbox

from mpd import MPDClient
from unittest.mock import MagicMock, patch


@patch('mpd.MPDClient.connect')
def test_player_connection_to_mpd(mock_mpd_connect):
    player = playbox.Player(playbox.AudioLibrary())
    player.connect()
    mock_mpd_connect.assert_called_once()


@patch('mpd.MPDClient.clear')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.play')
def test_player_plays_back_file_from_library(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")
    player = playbox.Player(library)
    player.play("12345")
    mock_mpd_clear.assert_called_once()
    mock_mpd_next.assert_called_once()
    mock_mpd_add.assert_called_once()
    mock_mpd_play.assert_called_once()


@patch('mpd.MPDClient.clear')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.play')
def test_player_does_not_play_back_unregistered_file(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.play("12345")
    mock_mpd_clear.assert_not_called()
    mock_mpd_next.assert_not_called()
    mock_mpd_add.assert_not_called()
    mock_mpd_play.assert_not_called()
