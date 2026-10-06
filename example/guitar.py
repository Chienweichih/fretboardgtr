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
    _C_major("C_Major_scale.svg",
             [[0, 1, 3, 5, 7, 8, 10], [7, 8, 10], [7, 9, 10, 12], [9, 10, 12], [10, 12, 13, 15], [12, 13, 15, 17, 19, 20, 22]])


def _pentatonic(filename, ROOT, pos):
    only_root_color = {
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
    }

    config_pentatonic = [
        # pos 1
        {
            "general": {
                "first_fret": 12,
                "last_fret": 15,
                "fretted_colors": only_root_color,
            },
        },
        # pos 2
        {
            "general": {
                "first_fret": 2,
                "last_fret": 6,
                "fretted_colors": only_root_color,
            },
        },
        # pos 3
        {
            "general": {
                "first_fret": 4,
                "last_fret": 8,
                "fretted_colors": only_root_color,
            },
        },
        # pos 4
        {
            "general": {
                "first_fret": 7,
                "last_fret": 10,
                "fretted_colors": only_root_color,
            },
        },
        # pos 5
        {
            "general": {
                "first_fret": 9,
                "last_fret": 13,
                "fretted_colors": only_root_color,
            },
        }
    ]

    if ROOT == "C":
        pentatonic_scale = ScaleFromName(root=ROOT, mode=ModeName.MAJOR_PENTATONIC).build()
    else:
        pentatonic_scale = ScaleFromName(root=ROOT, mode=ModeName.MINOR_PENTATONIC).build()

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic[pos - 1])
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=pentatonic_scale)
    export_file(fretboard, "pentatonic", filename)

def pentatonic():
    _pentatonic("C_C.svg",  "C", 1)
    _pentatonic("C_A.svg",  "C", 2)
    _pentatonic("C_G.svg",  "C", 3)
    _pentatonic("C_E.svg",  "C", 4)
    _pentatonic("C_D.svg",  "C", 5)
    _pentatonic("Am_C.svg", "A", 1)
    _pentatonic("Am_A.svg", "A", 2)
    _pentatonic("Am_G.svg", "A", 3)
    _pentatonic("Am_E.svg", "A", 4)
    _pentatonic("Am_D.svg", "A", 5)


def _CAGED(filename, pos, SCALE=[]):
    config_CAGED = [
        # pos 1
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 0,
                "last_fret": 3,
            },
            "open_notes": {
                "text_color": WHITE,
            },
        },
        # pos 2
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 2,
                "last_fret": 6,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 3
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 4,
                "last_fret": 8,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 4
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 7,
                "last_fret": 10,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 5
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 9,
                "last_fret": 13,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 6
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 0,
                "last_fret": 3,
            },
            "open_notes": {
                "text_color": WHITE,
            },
        },
        # pos 7
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 1,
                "last_fret": 5,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 8
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 4,
                "last_fret": 7,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 9
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 6,
                "last_fret": 10,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 10
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 9,
                "last_fret": 12,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 11
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 2,
                "last_fret": 5,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 12
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 5,
                "last_fret": 8,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        },
        # pos 13
        {
            "general": {
                "open_color_scale": True,
                "first_fret": 7,
                "last_fret": 10,
            },
            "open_notes": config_dont_show_open_notes["open_notes"],
        }
    ]

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_CAGED[pos - 1])
    if pos <= 10:
        fretboard = FretBoard(config=fretboard_config)
    else:
        TUNING = ['E', 'A', 'D']
        fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
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

    _CAGED("C.svg",          1)
    _CAGED("A.svg",          2)
    _CAGED("G.svg",          3)
    _CAGED("E.svg",          4)
    _CAGED("D.svg",          5)
    _CAGED("Chords/C_C.svg", 1,  scale_chords_C_C)
    _CAGED("Chords/C_A.svg", 2,  scale_chords_C_A)
    _CAGED("Chords/C_G.svg", 3,  scale_chords_C_G)
    _CAGED("Chords/C_E.svg", 4,  scale_chords_C_E)
    _CAGED("Chords/C_D.svg", 5,  scale_chords_C_D)
    _CAGED("Chords/A_A.svg", 6,  scale_chords_A_A)
    _CAGED("Chords/A_G.svg", 7,  scale_chords_A_G)
    _CAGED("Chords/A_E.svg", 8,  scale_chords_A_E)
    _CAGED("Chords/A_D.svg", 9,  scale_chords_A_D)
    _CAGED("Chords/A_C.svg", 10, scale_chords_A_C)
    _CAGED("GA.svg",         11)
    _CAGED("ABC.svg",        12)
    _CAGED("BCD.svg",        13)


def _chord(filename, ROOT, fingering):
    config_chords = {
        "general": {
            "first_fret": 0,
            "last_fret": 5,
            "fret_width": 50,
            "open_color_scale": True,
        },
        "open_notes": {
            "text_color": WHITE,
        },
    }

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
    config_fret = {
        "general": {
            "first_fret": 12,
            "last_fret": 18,
        },
    }

    TUNING = ['E', 'A', 'D', 'G', 'C']

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_fret)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
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
