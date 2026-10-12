from fretboardgtr.fretboard import FretBoard, FretBoardConfig
from fretboardgtr.notes_creators import ScaleFromName
from fretboardgtr.constants import ModeName, WHITE

config_text_color_white = {
    "fretted_notes": {
        "text_color": WHITE,
    },
}

TUNING = ['G', 'C', 'E', 'A']

def C_major():
    config_open_color_scale = {
        "general": {
            "open_color_scale": True,
        },
        "open_notes": {
            "text_color": WHITE,
        },
    }

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_scale)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
    major_c = ScaleFromName(root="C", mode=ModeName.MAJOR).build()
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/ukulele/C_Major.svg", format="svg")


def chords():
    config_chords = {
        "general": {
            "first_fret": 0,
            "last_fret": 5,
            "fret_width": 50,
        },
    }

    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_chords)

    # chords: E
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [4, 4, 4, 2]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/ukulele/chords/E.svg", format="svg")

    # chords: Em
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 4, 3, 2]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/ukulele/chords/Em.svg", format="svg")

    # chords: E7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [1, 2, 0, 2]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/ukulele/chords/E7.svg", format="svg")

    # chords: Em7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 0, 2]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/ukulele/chords/Em7.svg", format="svg")

    # chords: A
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 1, 0, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/ukulele/chords/A.svg", format="svg")

    # chords: Am
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 0, 0, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/ukulele/chords/Am.svg", format="svg")

    # chords: A7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 1, 0, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/ukulele/chords/A7.svg", format="svg")

    # chords: Am7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 0, 0, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/ukulele/chords/Am7.svg", format="svg")

    # chords: D
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 2, 2, 0]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/ukulele/chords/D.svg", format="svg")

    # chords: Dm
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 2, 1, 0]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/ukulele/chords/Dm.svg", format="svg")

    # chords: D7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 2, 2, 3]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/ukulele/chords/D7.svg", format="svg")

    # chords: Dm7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 2, 1, 3]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/ukulele/chords/Dm7.svg", format="svg")

    # chords: C
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 0, 0, 3]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/ukulele/chords/C.svg", format="svg")

    # chords: C7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 0, 0, 1]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/ukulele/chords/C7.svg", format="svg")

    # chords: Cmaj7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 0, 0, 2]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/ukulele/chords/Cmaj7.svg", format="svg")

    # chords: Cadd9
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 0, 3]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/ukulele/chords/Cadd9.svg", format="svg")

    # chords: G
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 3, 2]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/ukulele/chords/G.svg", format="svg")

    # chords: G7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 1, 2]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/ukulele/chords/G7.svg", format="svg")

    # chords: Gmaj7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 2, 2]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/ukulele/chords/Gmaj7.svg", format="svg")

    # chords: Gsus4
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [0, 2, 3, 3]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/ukulele/chords/Gsus4.svg", format="svg")

    # chords: F
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 0, 1, 0]
    fretboard.add_fingering(fingering, root="F")
    fretboard.export("output/ukulele/chords/F.svg", format="svg")

    # chords: Fm
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [1, 0, 1, 3]
    fretboard.add_fingering(fingering, root="F")
    fretboard.export("output/ukulele/chords/Fm.svg", format="svg")

    # chords: B7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 3, 2, 2]
    fretboard.add_fingering(fingering, root="B")
    fretboard.export("output/ukulele/chords/B7.svg", format="svg")

    # chords: Bm7
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING, vertical=True)
    fingering = [2, 2, 2, 2]
    fretboard.add_fingering(fingering, root="B")
    fretboard.export("output/ukulele/chords/Bm7.svg", format="svg")

if __name__ == "__main__":
    C_major()
    chords()
