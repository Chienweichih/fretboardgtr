from fretboardgtr.fretboard import FretBoard, FretBoardConfig
from fretboardgtr.notes_creators import ScaleFromName
from fretboardgtr.constants import ModeName, WHITE

config_text_color_white = {
    "fretted_notes": {
        "text_color": WHITE,
    },
}

config_open_color_scale = {
    "general": {
        "open_color_scale": True,
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

config_pentatonic_all = {
    "general": {
        "first_fret": 2,
        "last_fret": 15,
    },
}

config_pentatonic_1 = {
    "general": {
        "first_fret": 5,
        "last_fret": 8,
    },
}

config_pentatonic_2 = {
    "general": {
        "first_fret": 7,
        "last_fret": 10,
    },
}

config_pentatonic_3 = {
    "general": {
        "first_fret": 9,
        "last_fret": 13,
    },
}

config_pentatonic_4 = {
    "general": {
        "first_fret": 12,
        "last_fret": 15,
    },
}

config_pentatonic_5 = {
    "general": {
        "first_fret": 2,
        "last_fret": 5,
    },
}

config_chords = {
    "general": {
        "first_fret": 0,
        "last_fret": 5,
        "fret_width": 50,
    },
}

# C major
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_open_color_scale)
fretboard = FretBoard(config=fretboard_config)
major_c = ScaleFromName(root="C", mode=ModeName.MAJOR).build()
fretboard.add_notes(scale=major_c)
fretboard.export("output/major_c.svg", format="svg")

# C major pentatonic
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_all)
fretboard = FretBoard(config=fretboard_config)
major_c_pentatonic = ScaleFromName(root="C", mode=ModeName.MAJOR_PENTATONIC).build()
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic.svg", format="svg")

# C major pentatonic 1
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_1)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic-1.svg", format="svg")

# C major pentatonic 2
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_2)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic-2.svg", format="svg")

# C major pentatonic 3
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_3)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic-3.svg", format="svg")

# C major pentatonic 4
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_4)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic-4.svg", format="svg")

# C major pentatonic 5
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_5)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=major_c_pentatonic)
fretboard.export("output/major_c_pentatonic-5.svg", format="svg")

# A minor pentatonic
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_all)
fretboard = FretBoard(config=fretboard_config)
minor_a_pentatonic = ScaleFromName(root="A", mode=ModeName.MINOR_PENTATONIC).build()
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic.svg", format="svg")

# A minor pentatonic 1
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_1)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic-1.svg", format="svg")

# A minor pentatonic 2
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_2)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic-2.svg", format="svg")

# A minor pentatonic 3
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_3)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic-3.svg", format="svg")

# A minor pentatonic 4
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_4)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic-4.svg", format="svg")

# A minor pentatonic 5
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_dont_show_open_notes | config_pentatonic_5)
fretboard = FretBoard(config=fretboard_config)
fretboard.add_notes(scale=minor_a_pentatonic)
fretboard.export("output/minor_a_pentatonic-5.svg", format="svg")


# chords: C major
fretboard_config = FretBoardConfig.from_dict(config_text_color_white | config_chords)
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, 3, 2, 0, 1, 0]
fretboard.add_fingering(fingering, root="C")
fretboard.export("output/chords/major_c.svg", format="svg")

# chords: A major
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, 0, 2, 2, 2, 0]
fretboard.add_fingering(fingering, root="A")
fretboard.export("output/chords/major_a.svg", format="svg")

# chords: G major
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [3, 2, 0, 0, 0, 3]
fretboard.add_fingering(fingering, root="G")
fretboard.export("output/chords/major_g.svg", format="svg")

# chords: E major
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [0, 2, 2, 1, 0, 0]
fretboard.add_fingering(fingering, root="E")
fretboard.export("output/chords/major_e.svg", format="svg")

# chords: D major
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, None, 0, 2, 3, 2]
fretboard.add_fingering(fingering, root="D")
fretboard.export("output/chords/major_d.svg", format="svg")

# chords: F major
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, None, 3, 2, 1, 1]
fretboard.add_fingering(fingering, root="F")
fretboard.export("output/chords/major_f.svg", format="svg")

# chords: A minor
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, 0, 2, 2, 1, 0]
fretboard.add_fingering(fingering, root="A")
fretboard.export("output/chords/minor_a.svg", format="svg")

# chords: E minor
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [0, 2, 2, 0, 0, 0]
fretboard.add_fingering(fingering, root="E")
fretboard.export("output/chords/minor_e.svg", format="svg")

# chords: D minor
fretboard = FretBoard(config=fretboard_config, vertical=True)
fingering = [None, None, 0, 2, 3, 1]
fretboard.add_fingering(fingering, root="D")
fretboard.export("output/chords/minor_d.svg", format="svg")
