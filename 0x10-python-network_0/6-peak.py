#!/usr/bin/python3
"""Find Peak in integerlist."""

def find_peak(list_of_integers):
	if not list_of_integers:
		return None
	return max(list_of_integers)
