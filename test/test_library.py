#!/usr/bin/env python3

import pytest
import playbox


def test_song_retrival_by_number_if_number_is_present():
    # set up
    library = playbox.AudioLibrary()
    library.registerAudio("12345", "file:///my/song/foo.mp3")

    uri = library.getAudio("12345")
    assert uri == "file:///my/song/foo.mp3"
