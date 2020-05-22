"""
Module Description
"""

from typing import List
from pathlib import Path

from paths import GAME_PATH, PLUGIN_PATH


DOWNLOADS = PLUGIN_PATH / "round_end_sound/download/download.txt"


class _Sounds:
    def __init__(self, download_file: Path):
        self._sounds = []
        self.download_file = download_file
        self.last_mtime = download_file.stat().st_mtime

    def check_sound(self, sound: str) -> bool:
        """
        This method checks if the sound file is
        physically on the server.
        """
        return Path(GAME_PATH, sound).exists()

    def check_mtime(self) -> bool:
        return self.download_file.stat().st_mtime != self.last_mtime

    def update_if_required(self) -> None:
        if self.check_mtime():
            with self.download_file.open() as fd:
                self._sounds = [
                    Path(sound)
                    for sound in map(str.strip, fd)
                    if self.check_sound(sound)
                ]

    @property
    def sounds(self) -> List[str]:
        self.update_if_required()
        return [str(Path(*sound.parts[1:])) for sound in self._sounds]

    @property
    def download_table(self) -> List[str]:
        return [str(sound) for sound in self._sounds]


_sounds = _Sounds(DOWNLOADS)
SOUNDS = _sounds.sounds
DOWNLOAD_TABLE = _sounds.download_table
