"""
Originally from here:
https://github.com/srpg/round_end_sound

Code has been refactored but not tested yet
"""

import random

from events import Event
from stringtables.downloads import Downloadables

from .helper import play_sound, get_userids
from .sounds import DOWNLOAD_TABLE, SOUNDS


def load():
    set_download()


def set_download():
    downloadable = Downloadables()
    for sound in DOWNLOAD_TABLE:
        downloadable.add(sound)


@Event("round_end")
def round_end(args):
    for userid in get_userids():
        sound = random.choice(SOUNDS)
        play_sound(userid, sound)
