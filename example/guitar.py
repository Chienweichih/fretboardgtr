import copy
import os
from pathlib import Path

from fretboardgtr.fretboard import FretBoard, FretBoardConfig
from fretboardgtr.notes_creators import ScaleFromName, NotesContainer
from fretboardgtr.constants import ModeName, WHITE, BLACK

OUTPUTS_ARTIFACT_FOLDER = Path(__file__).parent / "output" / "guitar"

config_text_color_white = {
    "fretted_notes": {
        "text_color": WHITE,
    },
}

config_open_color_scale = {
    "general": {
        "open_color_scale": True,
        "last_fret": 22,
    },
    "open_notes": {
        "text_color": WHITE,
    },
}

config_dont_show_open_notes = {
    "open_notes": {
        "radius": 0,
        "stroke_width": 0,
        "fontsize": 0,
    },
}

major_c = ScaleFromName(root="C", mode=ModeName.MAJOR).build()

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


def _C_major(filename, SCALE=[]):
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_scale)
    fretboard = FretBoard(config=fretboard_config)
    if not SCALE:
        fretboard.add_notes(scale=major_c)
    else:
        fretboard.add_scale(SCALE, root="C")
    export_file(fretboard, filename)

def C_major():
    _C_major("C_Major.svg")
    # _C_major("C_Major_scale.svg",
    #          [[0, 1, 3, 5, 7, 8, 10], [7, 8, 10], [7, 9, 10, 12], [9, 10, 12], [10, 12, 13, 15], [12, 13, 15, 17, 19, 20, 22]])


def _pentatonic(filename, ROOT, first_fret, last_fret):
    config_pentatonic = {
        "general": {
            "fret_width": 50,
            "fretted_colors": {
                "minor_second": BLACK,
                "major_second": BLACK,
                "minor_third": BLACK,
                "major_third": BLACK,
                "perfect_fourth": BLACK,
                "diminished_fifth": BLACK,
                "perfect_fifth": BLACK,
                "minor_sixth": BLACK,
                "major_sixth": BLACK,
                "minor_seventh": BLACK,
                "major_seventh": BLACK,
            },
        },
    }
    config_pentatonic["general"]["first_fret"] = first_fret
    config_pentatonic["general"]["last_fret"] = last_fret

    if ROOT == "C":
        pentatonic_scale = ScaleFromName(root=ROOT, mode=ModeName.MAJOR_PENTATONIC).build()
    else:
        pentatonic_scale = ScaleFromName(root=ROOT, mode=ModeName.MINOR_PENTATONIC).build()

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic)
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fretboard.add_notes(scale=pentatonic_scale)
    export_file(fretboard, "pentatonic", filename)

def pentatonic():
    _pentatonic("C_C.svg",  "C", 12, 15)
    _pentatonic("C_A.svg",  "C", 2, 6)
    _pentatonic("C_G.svg",  "C", 4, 8)
    _pentatonic("C_E.svg",  "C", 7, 10)
    _pentatonic("C_D.svg",  "C", 9, 13)
    # _pentatonic("Am_C.svg", "A", 12, 15)
    # _pentatonic("Am_A.svg", "A", 2, 6)
    # _pentatonic("Am_G.svg", "A", 4, 8)
    # _pentatonic("Am_E.svg", "A", 7, 10)
    # _pentatonic("Am_D.svg", "A", 9, 13)


def _CAGED(filename, first_fret, last_fret, TUNING, SCALE=[]):
    config_CAGED = copy.deepcopy(config_open_color_scale)
    config_CAGED["general"]["fret_width"] = 50
    config_CAGED["general"]["last_fret"] = last_fret
    if first_fret != 0:
        config_CAGED["general"]["first_fret"] = first_fret
        config_CAGED["open_notes"] = copy.deepcopy(config_dont_show_open_notes["open_notes"])

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_CAGED)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    if not SCALE:
        fretboard.add_notes(scale=major_c)
    else:
        fretboard.add_scale(SCALE, root="C")
    export_file(fretboard, "CAGED", filename)

def CAGED():
    scale_chords_C_C = [[], [3], [2], [0], [1], [0]]
    scale_chords_C_A = [[], [3], [5], [5], [5], [3]]
    scale_chords_C_G = [[8], [7], [5], [5], [5], [8]]
    scale_chords_C_E = [[8], [10], [10], [9], [8], [8]]
    scale_chords_C_D = [[], [], [10], [12], [13], [12]]
    scale_chords_A_A = [[], [0], [2], [2], [2], [0]]
    scale_chords_A_G = [[5], [4], [2], [2], [2], [5]]
    scale_chords_A_E = [[5], [7], [7], [6], [5], [5]]
    scale_chords_A_D = [[], [], [7], [9], [10], [9]]
    scale_chords_A_C = [[], [12], [11], [9], [10], [9]]

    _CAGED("C.svg", 0, 3,  ['E', 'A', 'D', 'G', 'B', 'E'])
    _CAGED("A.svg", 2, 6,  ['E', 'A', 'D', 'G', 'B', 'E'])
    _CAGED("G.svg", 4, 8,  ['E', 'A', 'D', 'G', 'B', 'E'])
    _CAGED("E.svg", 7, 10, ['E', 'A', 'D', 'G', 'B', 'E'])
    _CAGED("D.svg", 9, 13, ['E', 'A', 'D', 'G', 'B', 'E'])
    _CAGED("Chords/C_C.svg", 0, 3,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_C_C)
    _CAGED("Chords/C_A.svg", 2, 6,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_C_A)
    _CAGED("Chords/C_G.svg", 4, 8,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_C_G)
    _CAGED("Chords/C_E.svg", 7, 10, ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_C_E)
    _CAGED("Chords/C_D.svg", 9, 13, ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_C_D)
    # _CAGED("Chords/A_A.svg", 0, 3,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_A_A)
    # _CAGED("Chords/A_G.svg", 1, 5,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_A_G)
    # _CAGED("Chords/A_E.svg", 4, 7,  ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_A_E)
    # _CAGED("Chords/A_D.svg", 6, 10, ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_A_D)
    # _CAGED("Chords/A_C.svg", 9, 12, ['E', 'A', 'D', 'G', 'B', 'E'], scale_chords_A_C)
    _CAGED("EFG.svg", 0, 3,  ['E', 'A', 'D'])
    _CAGED("GA.svg",  2, 5,  ['E', 'A', 'D'])
    _CAGED("GAB.svg", 3, 7,  ['E', 'A', 'D'])
    _CAGED("ABC.svg", 5, 8,  ['E', 'A', 'D'])
    _CAGED("BCD.svg", 7, 10, ['E', 'A', 'D'])
    _CAGED("CDE.svg", 8, 12, ['E', 'A', 'D'])


def _chord(filename, ROOT, fingering):
    config_chords = copy.deepcopy(config_open_color_scale)
    config_chords["general"]["fret_width"] = 50
    config_chords["general"]["last_fret"] = 5

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_chords)
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fretboard.add_fingering(fingering, root=ROOT)
    export_file(fretboard, "chords", filename)

def chord():
    _chord("C.svg",     "C", [None, 3, 2, 0, 1, 0])
    _chord("C7.svg",    "C", [None, 3, 2, 3, 1, 0])
    _chord("Cmaj7.svg", "C", [None, 3, 2, 0, 0, 0])
    _chord("Cadd9.svg", "C", [None, 3, 2, 0, 3, 0])
    _chord("A.svg",     "A", [None, 0, 2, 2, 2, 0])
    _chord("Am.svg",    "A", [None, 0, 2, 2, 1, 0])
    _chord("A7.svg",    "A", [None, 0, 2, 0, 2, 0])
    _chord("Am7.svg",   "A", [None, 0, 2, 0, 1, 0])
    _chord("B.svg",     "B", [None, 2, 4, 4, 4, 2])
    _chord("Bm.svg",    "B", [None, 2, 4, 4, 3, 2])
    _chord("B7.svg",    "B", [None, 2, 1, 2, 0, 2])
    _chord("Bm7.svg",   "B", [None, 2, 0, 2, 0, 2])
    _chord("G.svg",     "G", [3, 2, 0, 0, 0, 3])
    _chord("G7.svg",    "G", [3, 2, 0, 0, 0, 1])
    _chord("Gmaj7.svg", "G", [3, 2, 0, 0, 0, 2])
    _chord("Gsus4.svg", "G", [3, 3, 0, 0, 1, 3])
    _chord("E.svg",     "E", [0, 2, 2, 1, 0, 0])
    _chord("Em.svg",    "E", [0, 2, 2, 0, 0, 0])
    _chord("E7.svg",    "E", [0, 2, 0, 1, 0, 0])
    _chord("Em7.svg",   "E", [0, 2, 0, 0, 0, 0])
    _chord("F.svg",     "F", [1, 3, 3, 2, 1, 1])
    _chord("Fm.svg",    "F", [1, 3, 3, 1, 1, 1])
    _chord("F7.svg",    "F", [1, 3, 1, 2, 1, 1])
    _chord("Fmaj7.svg", "F", [None, None, 3, 2, 1, 0])
    _chord("D.svg",     "D", [None, None, 0, 2, 3, 2])
    _chord("Dm.svg",    "D", [None, None, 0, 2, 3, 1])
    _chord("D7.svg",    "D", [None, None, 0, 2, 1, 2])
    _chord("Dm7.svg",   "D", [None, None, 0, 2, 1, 1])


def _chord_on_fret(filename, SCALE):
    config_fret = copy.deepcopy(config_open_color_scale)
    config_fret["general"]["last_fret"] = 13
    config_fret["general"]["fret_width"] = 50

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_fret)
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fretboard.add_notes(scale=SCALE)
    export_file(fretboard, "chord_on_fret", filename)

def chord_on_fret():
    _chord_on_fret("C.svg",     NotesContainer(root= 'C', notes = ['C', 'E', 'G']))
    _chord_on_fret("Cm.svg",    NotesContainer(root= 'C', notes = ['C', 'Eb', 'G']))
    _chord_on_fret("Cdim.svg",  NotesContainer(root= 'C', notes = ['C', 'Eb', 'Gb']))
    _chord_on_fret("Csus2.svg", NotesContainer(root= 'C', notes = ['C', 'D', 'G']))
    _chord_on_fret("Csus4.svg", NotesContainer(root= 'C', notes = ['C', 'F', 'G']))
    _chord_on_fret("Caug.svg",  NotesContainer(root= 'C', notes = ['C', 'E', 'G#']))


if __name__ == "__main__":
    C_major()
    pentatonic()
    CAGED()
    chord()
    chord_on_fret()
