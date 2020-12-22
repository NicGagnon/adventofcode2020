from pathlib import Path


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('9.in')
	data = [int(i) for i in open(input_dir).read().split('\n')]
	return data


def two_sum(preample, target):
	sum_dict = {}
	for i in preample:
		sum_dict[target - i] = i
	for i in preample:
		if i in sum_dict:
			return True
	return False


def get_weakness(data, offset=25):
	idx = offset
	while True:
		preample = data[idx-offset: idx]
		target = data[idx]
		if two_sum(preample, target):
			idx += 1
		else:
			return idx

def get_contiguous_range(data, max_index):
	target_value = data[max_index]
	for step in range(2, max_index):
		for i in range(max_index):
			subset_range = data[i: i+step]
			if sum(subset_range) == target_value:
				return subset_range



def main():
	data = get_data()
	result = get_weakness(data)
	contiguous_list = get_contiguous_range(data, result)
	min_value, max_value = min(contiguous_list), max(contiguous_list)
	return min_value + max_value

if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 9 is {result}")
