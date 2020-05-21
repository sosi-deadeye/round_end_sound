"""
Module Description
"""

from typing import List
from pathlib import Path

DOWNLOADS = Path(__file__).parent / "download/download.txt"
# SOUNDS_PATH = Path("sound")
# todo get sounds path from sourcepython
# looking in documentation helps....


class _Sounds:
    def __init__(self, download_file: Path):
        self._sounds = []
        self.download_file = download_file
        self.last_mtime = download_file.stat().st_mtime

    def check_sound(self, sound: str) -> bool:
        """
        # todo implement this function
        This method should check if the sound file is
        physically on the server
        """
        raise NotImplementedError

    def check_mtime(self):
        return self.download_file.stat().st_mtime != self.last_mtime

    def update_if_required(self):
        if self.check_mtime():
            with self.download_file.open() as fd:
                self._sounds = [Path(sound) for sound in map(str.strip, fd) if sound]

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
