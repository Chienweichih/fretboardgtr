from fretboardgtr.fretboard import FretBoard, FretBoardConfig
from fretboardgtr.notes_creators import ScaleFromName
from fretboardgtr.constants import ModeName, WHITE, BLACK

config_text_color_white = {
    "fretted_notes": {
        "text_color": WHITE,
    },
}

major_c = ScaleFromName(root="C", mode=ModeName.MAJOR).build()

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
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/C_Major.svg", format="svg")


def pentatonic():
    config_dont_show_open_notes = {
        "open_notes": {
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_pentatonic_1 = {
        "general": {
            "first_fret": 5,
            "last_fret": 8,
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

    config_pentatonic_2 = {
        "general": {
            "first_fret": 7,
            "last_fret": 10,
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

    config_pentatonic_3 = {
        "general": {
            "first_fret": 9,
            "last_fret": 13,
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

    config_pentatonic_4 = {
        "general": {
            "first_fret": 12,
            "last_fret": 15,
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

    config_pentatonic_5 = {
        "general": {
            "first_fret": 2,
            "last_fret": 5,
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

    major_c_pentatonic = ScaleFromName(root="C", mode=ModeName.MAJOR_PENTATONIC).build()

    # C major pentatonic 1
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_1)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c_pentatonic)
    fretboard.export("output/guitar/pentatonic/C_1.svg", format="svg")

    # C major pentatonic 2
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_2)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c_pentatonic)
    fretboard.export("output/guitar/pentatonic/C_2.svg", format="svg")

    # C major pentatonic 3
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_3)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c_pentatonic)
    fretboard.export("output/guitar/pentatonic/C_3.svg", format="svg")

    # C major pentatonic 4
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_4)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c_pentatonic)
    fretboard.export("output/guitar/pentatonic/C_4.svg", format="svg")

    # C major pentatonic 5
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_5)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c_pentatonic)
    fretboard.export("output/guitar/pentatonic/C_5.svg", format="svg")


    minor_a_pentatonic = ScaleFromName(root="A", mode=ModeName.MINOR_PENTATONIC).build()

    # A minor pentatonic 1
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_1)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=minor_a_pentatonic)
    fretboard.export("output/guitar/pentatonic/Am_1.svg", format="svg")

    # A minor pentatonic 2
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_2)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=minor_a_pentatonic)
    fretboard.export("output/guitar/pentatonic/Am_2.svg", format="svg")

    # A minor pentatonic 3
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_3)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=minor_a_pentatonic)
    fretboard.export("output/guitar/pentatonic/Am_3.svg", format="svg")

    # A minor pentatonic 4
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_4)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=minor_a_pentatonic)
    fretboard.export("output/guitar/pentatonic/Am_4.svg", format="svg")

    # A minor pentatonic 5
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_5)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=minor_a_pentatonic)
    fretboard.export("output/guitar/pentatonic/Am_5.svg", format="svg")


def CAGED():
    config_open_color_CAGED_C = {
        "general": {
            "open_color_scale": True,
            "first_fret": 0,
            "last_fret": 3,
        },
        "open_notes": {
            "text_color": WHITE,
        },
    }

    config_open_color_CAGED_A = {
        "general": {
            "open_color_scale": True,
            "first_fret": 2,
            "last_fret": 6,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_open_color_CAGED_GA = {
        "general": {
            "open_color_scale": True,
            "first_fret": 2,
            "last_fret": 5,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_open_color_CAGED_G = {
        "general": {
            "open_color_scale": True,
            "first_fret": 4,
            "last_fret": 8,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_open_color_CAGED_ABC = {
        "general": {
            "open_color_scale": True,
            "first_fret": 5,
            "last_fret": 8,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_open_color_CAGED_E = {
        "general": {
            "open_color_scale": True,
            "first_fret": 7,
            "last_fret": 10,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    config_open_color_CAGED_D = {
        "general": {
            "open_color_scale": True,
            "first_fret": 9,
            "last_fret": 13,
        },
        "open_notes": {
            "text_color": WHITE,
            "radius": 0,
            "stroke_width": 0,
            "fontsize": 0,
        },
    }

    TUNING = ['E', 'A', 'D']
    scale_GA = [[3, 5], [2, 3, 5], [2, 3, 5]]
    scale_ABC = [[5, 7, 8], [5, 7, 8], [5, 7]]
    scale_BCD = [[7, 8, 10], [7, 8, 10], [7, 9, 10]]

    # GA scale
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_GA)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
    fretboard.add_scale(scale_GA, root="C")
    fretboard.export("output/guitar/CAGED/GA.svg", format="svg")

    # ABC scale
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_ABC)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
    fretboard.add_scale(scale_ABC, root="C")
    fretboard.export("output/guitar/CAGED/ABC.svg", format="svg")

    # BCD scale
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_E)
    fretboard = FretBoard(config=fretboard_config, tuning=TUNING)
    fretboard.add_scale(scale_BCD, root="C")
    fretboard.export("output/guitar/CAGED/BCD.svg", format="svg")


    # CAGED C
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_C)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/CAGED/C.svg", format="svg")

    # CAGED A
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_A)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/CAGED/A.svg", format="svg")

    # CAGED G
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_G)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/CAGED/G.svg", format="svg")

    # CAGED E
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_E)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/CAGED/E.svg", format="svg")

    # CAGED D
    fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_CAGED_D)
    fretboard = FretBoard(config=fretboard_config)
    fretboard.add_notes(scale=major_c)
    fretboard.export("output/guitar/CAGED/D.svg", format="svg")

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
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [0, 2, 2, 1, 0, 0]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/guitar/chords/E.svg", format="svg")

    # chords: Em
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [0, 2, 2, 0, 0, 0]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/guitar/chords/Em.svg", format="svg")

    # chords: E7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [0, 2, 0, 1, 0, 0]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/guitar/chords/E7.svg", format="svg")

    # chords: Em7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [0, 2, 0, 0, 0, 0]
    fretboard.add_fingering(fingering, root="E")
    fretboard.export("output/guitar/chords/Em7.svg", format="svg")

    # chords: A
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 0, 2, 2, 2, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/guitar/chords/A.svg", format="svg")

    # chords: Am
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 0, 2, 2, 1, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/guitar/chords/Am.svg", format="svg")

    # chords: A7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 0, 2, 0, 2, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/guitar/chords/A7.svg", format="svg")

    # chords: Am7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 0, 2, 0, 1, 0]
    fretboard.add_fingering(fingering, root="A")
    fretboard.export("output/guitar/chords/Am7.svg", format="svg")

    # chords: D
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, None, 0, 2, 3, 2]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/guitar/chords/D.svg", format="svg")

    # chords: Dm
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, None, 0, 2, 3, 1]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/guitar/chords/Dm.svg", format="svg")

    # chords: D7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, None, 0, 2, 1, 2]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/guitar/chords/D7.svg", format="svg")

    # chords: Dm7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, None, 0, 2, 1, 1]
    fretboard.add_fingering(fingering, root="D")
    fretboard.export("output/guitar/chords/Dm7.svg", format="svg")

    # chords: C
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 3, 2, 0, 1, 0]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/guitar/chords/C.svg", format="svg")

    # chords: C7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 3, 2, 3, 1, 0]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/guitar/chords/C7.svg", format="svg")

    # chords: Cmaj7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 3, 2, 0, 0, 0]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/guitar/chords/Cmaj7.svg", format="svg")

    # chords: Cadd9
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 3, 2, 0, 3, 0]
    fretboard.add_fingering(fingering, root="C")
    fretboard.export("output/guitar/chords/Cadd9.svg", format="svg")

    # chords: G
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [3, 2, 0, 0, 0, 3]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/guitar/chords/G.svg", format="svg")

    # chords: G7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [3, 2, 0, 0, 0, 1]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/guitar/chords/G7.svg", format="svg")

    # chords: Gmaj7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [3, 2, 0, 0, 0, 2]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/guitar/chords/Gmaj7.svg", format="svg")

    # chords: Gsus4
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [3, 3, 0, 0, 1, 3]
    fretboard.add_fingering(fingering, root="G")
    fretboard.export("output/guitar/chords/Gsus4.svg", format="svg")

    # chords: F
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [1, 3, 3, 2, 1, 1]
    fretboard.add_fingering(fingering, root="F")
    fretboard.export("output/guitar/chords/F.svg", format="svg")

    # chords: Fmaj7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, None, 3, 2, 1, 0]
    fretboard.add_fingering(fingering, root="F")
    fretboard.export("output/guitar/chords/Fmaj7.svg", format="svg")

    # chords: B7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 2, 1, 2, 0, 2]
    fretboard.add_fingering(fingering, root="B")
    fretboard.export("output/guitar/chords/B7.svg", format="svg")

    # chords: Bm7
    fretboard = FretBoard(config=fretboard_config, vertical=True)
    fingering = [None, 2, 0, 2, 0, 2]
    fretboard.add_fingering(fingering, root="B")
    fretboard.export("output/guitar/chords/Bm7.svg", format="svg")

if __name__ == "__main__":
    C_major()
    pentatonic()
    CAGED()
    chords()
