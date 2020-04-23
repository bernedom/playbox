#!/usr/bin/env python3

import pytest
import playbox


def test_audio_retrival_by_number_if_number_is_present():
    # set up
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/my/audio/foo.ogg")

    uri = library.getAudio("12345")
    assert uri == "file:///my/audio/foo.ogg"
    assert library.hasAudio("12345")


def test_audio_retrieval_by_number_if_number_is_not_present():
    library = playbox.AudioLibrary()
    assert not library.hasAudio("12345")
    with pytest.raises(KeyError):
        library.getAudio("12345")


def test_if_audio_added_as_path_then_is_converted_to_uri():
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "/my/audio/foo.ogg")

    assert "file:///my/audio/foo.ogg" == library.getAudio("12345")


def test_if_audio_added_as_relative_path_is_converted_to_uri():
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "./somefile.ogg")

    assert library.getAudio("12345").startswith("file://")


def test_registering_of_spotify_track_by_url():
    library = playbox.AudioLibrary()
    library.registerSpotifyAudio(
        "12345", "https://open.spotify.com/track/1zB4vmk8tFRmM9UULNzbLB")

    assert library.getAudio("12345") == "spotify:track:1zB4vmk8tFRmM9UULNzbLB"


def test_malfolrmed_spotify_url_raises_exception():
    library = playbox.AudioLibrary()
    with pytest.raises(Exception):
        library.registerSpotifyAudio(
            "12345", "https://open.anyweb.com/track/1zB4vmk8tFRmM9UULNzbLB")
