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


@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.clear')
def test_player_plays_back_file_from_library(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.handleToken("12345")
    mock_mpd_clear.assert_called_once()
    mock_mpd_next.assert_called_once()
    mock_mpd_add.assert_called_once()
    mock_mpd_play.assert_called_once()


@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.clear')
def test_player_does_not_play_back_unregistered_file(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.handleToken("12345")
    mock_mpd_clear.assert_not_called()
    mock_mpd_next.assert_not_called()
    mock_mpd_add.assert_not_called()
    mock_mpd_play.assert_not_called()


@patch('mpd.MPDClient.stop')
def test_stop_token_calls_mpc_stop(mock_mpd_stop):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerStop("99999")
    player.handleToken("99999")
    mock_mpd_stop.assert_called_once()


@patch('mpd.MPDClient.next')
def test_next_token_calls_mpc_next(mock_mpd_next):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerNext("99999")
    player.handleToken("99999")
    mock_mpd_next.assert_called_once()


@patch('mpd.MPDClient.previous')
def test_previous_token_calls_mpc_previous(mock_mpd_previous):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerPrevious("99999")
    player.handleToken("99999")
    mock_mpd_previous.assert_called_once()


@patch('mpd.MPDClient.pause')
def test_pause_token_calls_mpc_pause(mock_mpd_pause):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerPause("99999")
    player.handleToken("99999")
    mock_mpd_pause.assert_called_once()


@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.pause')
def test_repeated_pause_token_toggles_mpc_pause_and_play(mock_mpd_pause, mock_mpd_play):
    library = playbox.AudioLibrary()
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerPause("99999")
    player.handleToken("99999")
    player.handleToken("99999")
    mock_mpd_pause.assert_called_once()
    mock_mpd_play.assert_called_once()


@patch('mpd.MPDClient.clear')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.pause')
def test_to_play_with_same_token_result_in_two_play_calls_to_mpd_when_paused(mock_mpd_pause, mock_mpd_play, mock_mpd_add, mock_mpd_next, mock_mpd_clear):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")

    player = playbox.Player(library)
    player.registerPause("99999")
    player.connect = MagicMock(return_value=True)
    player.handleToken("12345")
    player.handleToken("99999")
    player.handleToken("12345")
    mock_mpd_pause.assert_called_once()
    assert mock_mpd_play.call_count == 2


@patch('mpd.MPDClient.clear')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.play')
def test_multiple_calls_to_play_with_same_token_result_in_only_one_play_call_to_mpd(mock_mpd_play, mock_mpd_add, mock_mpd_next, mock_mpd_clear):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.handleToken("12345")
    player.handleToken("12345")
    mock_mpd_clear.assert_called_once()
    mock_mpd_next.assert_called_once()
    mock_mpd_add.assert_called_once()
    mock_mpd_play.assert_called_once()


@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.clear')
def test_multiple_calls_to_play_with_different_token_result_in_two_play_calls_to_mpd(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")
    library.registerAudio("45678", "/some/other/file/foo.ogg")
    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.handleToken("12345")
    player.handleToken("45678")
    assert mock_mpd_play.call_count == 2


@patch('mpd.MPDClient.stop')
@patch('mpd.MPDClient.play')
@patch('mpd.MPDClient.add')
@patch('mpd.MPDClient.next')
@patch('mpd.MPDClient.clear')
def test_multiple_calls_to_play_with_same_token_result_in_two_plays_if_stop_was_called_in_between_call_to_mpd(mock_mpd_clear, mock_mpd_next, mock_mpd_add, mock_mpd_play, mock_mpd_stop):
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/some/file/foo.ogg")

    player = playbox.Player(library)
    player.connect = MagicMock(return_value=True)
    player.registerStop("99999")
    player.handleToken("12345")
    player.handleToken("99999")
    player.handleToken("12345")
    mock_mpd_clear.call_count = 2
    mock_mpd_next.call_count = 2
    mock_mpd_add.call_count = 2
    mock_mpd_stop.call_count = 2
    assert mock_mpd_play.call_count == 2
