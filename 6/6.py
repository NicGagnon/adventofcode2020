from pathlib import Path
from collections import Counter


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('6.in')
	data = open(input_dir).read().split('\n')
	all_data, group_data = [], []
	for i in data:
		if i:
			group_data.append(i)
		else:
			all_data.append(group_data.copy())
			group_data.clear()
	return all_data


def or_count_yes(group_info):
	unique_let = set(let for group in group_info for let in group)
	return len(unique_let)

def all_count_yes(group_info):
	character_count = Counter("".join([group for group in group_info]))
	all_answered = [k for k, v in character_count.items() if v == len(group_info)]
	return len(all_answered)

def main():
	data = get_data()
	all_yes = sum([all_count_yes(i) for i in data])
	return all_yes

if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 6 is {result}")
