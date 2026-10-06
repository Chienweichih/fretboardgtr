import copy
import os
from pathlib import Path

from fretboardgtr.fretboard import FretBoard, FretBoardConfig
from fretboardgtr.notes_creators import ScaleFromName
from fretboardgtr.constants import ModeName, WHITE

OUTPUTS_ARTIFACT_FOLDER = Path(__file__).parent / "output" / "ukulele"

config_text_color_white = {
    "fretted_notes": {
        "text_color": WHITE,
    },
}

config_open_color_scale = {
    "general": {
        "open_color_scale": True,
        "last_fret": 17,
    },
    "open_notes": {
        "text_color": WHITE,
    },
}

TUNING = ['G', 'C', 'E', 'A']

def remove_test_file(path: Path):
    if path.exists():
        os.remove(str(path))

def export_file(fretboard, subdir="", filename=""):
    os.makedirs(OUTPUTS_ARTIFACT_FOLDER, exist_ok=True)
    tmp_file = OUTPUTS_ARTIFACT_FOLDER / subdir / filename
    remove_test_file(tmp_file)
    assert not tmp_file.exists()
    fretboard.export(tmp_file)
    assert tmp_file.exists()


def C_major():
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_scale)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
    major_c = ScaleFromName(root="C", mode=ModeName.MAJOR).build()
    fretboard.add_notes(scale=major_c)
    export_file(fretboard, "C_Major.svg")


def _chord(filename, ROOT, fingering):
    config_chords = copy.deepcopy(config_open_color_scale)
    config_chords["general"]["last_fret"] = 4

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_chords)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fretboard.add_fingering(fingering, root=ROOT)
    export_file(fretboard, "chords", filename)

def chord():
    _chord("F.svg",     "F", [2, 0, 1, 0])
    _chord("F7.svg",    "F", [2, 3, 1, 2])
    _chord("Fmaj7.svg", "F", [2, 3, 1, 3])
    _chord("Fadd9.svg", "F", [0, 0, 1, 0])
    _chord("D.svg",     "D", [2, 2, 2, 0])
    _chord("Dm.svg",    "D", [2, 2, 1, 0])
    _chord("D7.svg",    "D", [2, 2, 2, 3])
    _chord("Dm7.svg",   "D", [2, 2, 1, 3])
    _chord("E.svg",     "E", [4, 4, 4, 2])
    _chord("Em.svg",    "E", [0, 4, 3, 2])
    _chord("E7.svg",    "E", [1, 2, 0, 2])
    _chord("Em7.svg",   "E", [0, 2, 0, 2])
    _chord("C.svg",     "C", [0, 0, 0, 3])
    _chord("C7.svg",    "C", [0, 0, 0, 1])
    _chord("Cmaj7.svg", "C", [0, 0, 0, 2])
    _chord("Csus4.svg", "C", [0, 0, 1, 3])
    _chord("A.svg",     "A", [2, 1, 0, 0])
    _chord("Am.svg",    "A", [2, 0, 0, 0])
    _chord("A7.svg",    "A", [0, 1, 0, 0])
    _chord("Am7.svg",   "A", [0, 0, 0, 0])
    _chord("B.svg",     "B", [4, 3, 2, 2])
    _chord("Bm.svg",    "B", [4, 2, 2, 2])
    _chord("B7.svg",    "B", [2, 3, 2, 2])
    _chord("Bmaj7.svg", "B", [4, 3, 2, 1])
    _chord("G.svg",     "G", [0, 2, 3, 2])
    _chord("Gm.svg",    "G", [0, 2, 3, 1])
    _chord("G7.svg",    "G", [0, 2, 1, 2])
    _chord("Gm7.svg",   "G", [0, 2, 1, 1])


if __name__ == "__main__":
    C_major()
    chord()
