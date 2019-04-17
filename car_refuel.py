#python3 

import sys


def compute_min_refills(distance, tank, stops):
	refuels = 0
	position = 0
	stops = list(reversed(stops))
	print(stops)
	
	if distance <= tank: return refuels
	for s in stops:
		if abs(position-s) < tank:
			position = s
			refuels += 1
			distance -= s
			if distance <= tank: return refuels
	return -1	

if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
