"""
Module Description
"""

from engines.server import engine_server
from filters.players import PlayerIter
from players.helpers import edict_from_userid


def play_sound(userid, sound):
    client_command(userid, f"play {sound}")


def get_userids():
    yield from PlayerIter.iterator()


def client_command(userid, cmd):
    engine_server.client_command(edict_from_userid(userid), cmd)
