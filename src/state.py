# -*- coding: utf-8 -*-
"""
This serves as a simplistic, bastardized and
pretty ugly state-management. In the sense
that this contains "global" variables.
"""

# Game details.
game_name: str = ""
"""
This is the name of the window of the application
to capture and send inputs to.
"""

# Run state variables.
run_done: bool = False
"""
This variable is used as a flag to tell when
a run is done. False means it's on-going, and
True means it's done.
"""

run_count: int = 0
"""
This is a counter variable used to keep track
of how many runs have been done in total.
"""

stop_flag: bool = False
"""
This is a boolean to tell the process if it
should exit or not.
"""

run_reverse: bool = False
"""
This is the boolean to use in map function
arguments to toggle whether it'll be done
in reverse or not.

Should make the logic a bit simpler,
hopefully.
"""

# GUI stuff
maps = []
"""
This is the global list for map choices
used in the GUI presented to the user.
"""

runs_wanted: int = 0
"""
User-defined amount of runs to do.
"""

map_selected: str = ""
"""
Selected map to run.
"""

exit_on_finish: bool = False
"""
If to exit upon completing amount of runs wanted.
"""
