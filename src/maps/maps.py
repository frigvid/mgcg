# -*- coding: utf-8 -*-
"""
This contains functions to register maps,
and get the map list.

Though there's nothing stopping you from
just accessing state directly. But eh.
"""

import src.state as state


def register(name):
	# Check if the name already exists in the list
	if name not in state.maps:
		# Add the name to the list
		state.maps.append(name)
		# Sort the list alphabetically
		state.maps.sort()
		# Return True to indicate successful registration
		return True
	else:
		# Return False to indicate that the name already exists
		return False


def get_maps():
	# Return the sorted map list
	return state.maps
