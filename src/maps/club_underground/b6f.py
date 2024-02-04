# -*- coding: utf-8 -*-
"""
This module contains the functions needed to
register this map to the global map list, as
well as the moves needed to perform a full
run-through of the map.

Assuming no enemies, obviously.
"""

from src.run.gameInput import press_keys_list
import src.state as state

map_name: str = "Club Underground B6F"


# Register map.
def register():
	"""
	Registers the map to the global map list.
	"""

	import src.maps.maps as maps

	# The full name contains "- Otherworld" at the end.
	# But it's *probably* not important lol.
	maps.register(map_name)


def start(reverse):
	"""
	When ran normally, it starts with the player positioned
	right upon the end-point teleport point. To account for
	it starting once you've teleported there.

	|regular|

	If reversed, it assumes you're standing in the stairs
	leading down to the last floor, on your left side when
	facing the stairs.

	|reverse|

	.. |regular| image:: https://raw.githubusercontent.com/frigvid/mgcg/master/img/map/b6f_regular.png
		:alt: Regular start position

	.. |reverse| image:: https://raw.githubusercontent.com/frigvid/mgcg/master/img/map/b6f_reverse.png
		:alt: Reverse start position

	:param reverse: Whether to reverse inputs or not.
	"""

	pc_moves = [
		# End-point teleport room.
		["left", 7], ["down", 2],
		# Sleep for teleport.
		("sleep", 10),
		# First hall, end-point entrance.
		["down", 5], ["left", 26],
		# Second hall, down to crossroad.
		["down", 7],
		# Second hall, down dead-end and back.
		["down", 8], ["up", 7],
		# Second hall, down to crossroad.
		["right", 17],
		# Second hall, down dead-end and back.
		["right", 25], ["left", 25],
		# Second hall, down crossroad.
		["down", 11], ["up", 5], ["left", 9], ["down", 17],
		# Third hall, to crossroad.
		["right", 7], ["down", 14], ["up", 14], ["right", 7],
		# Fourth hall, up to traps
		["up", 5], ["right", 5], ["up", 9], ["down", 6], ["right", 8],
		# Fifth hall
		["down", 16], ["left", 12], ["down", 6], ["right", 8],
		# Entrance to second floor
		["up", 2],
		# Wait for teleportation
		("sleep", 10),
		# Then go up to the second floor, or down to the third.
		["up", 1]
	]

	if reverse:
		# pc_moves_reversed = reversed(pc_moves)
		press_keys_list(reversed(pc_moves), reverse=True)
		state.run_done = True
		state.run_count += 1
	else:
		press_keys_list(pc_moves)
		state.run_done = True
		state.run_count += 1
