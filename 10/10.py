from pathlib import Path
from collections import Counter, defaultdict


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('10.in')
	data = [int(i) for i in open(input_dir).read().split('\n')]
	return data

def calc_jumps(data):
	diff_list = []
	sorted_data = sorted(data)
	for idx in range(1, len(sorted_data)):
		diff_list.append(sorted_data[idx] - sorted_data[idx-1])
	distribution = Counter(diff_list)
	return distribution



def calc_efficient_jumps(data):
	sorted_data = sorted(data)
	counts = defaultdict(int, {0: 1})
	for a in sorted_data[1:]:
		# number of ways to reach i'th adapter
		# from previous three possible ones
		counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
	return counts[sorted_data[-1]]


def main():
	data = get_data()
	data += [0, max(data)+3]
	result = calc_efficient_jumps(data)
	#  result = jumps.get(1) * jumps.get(3) part one
	return result

if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 10 is {result}")
