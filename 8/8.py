from pathlib import Path


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('8.in')
	rules = open(input_dir).read().split('\n')
	return rules

def compiler(inst):
	acc, idx = 0, 0
	visited = {}
	while idx != len(inst):
		visited[idx] = True
		op, arg = inst[idx].split()
		if op == "acc":
			acc += int(arg)
			idx += 1
		elif op == "jmp":
			idx += int(arg)
		else:
			idx += 1

		if idx in visited:
			return False, acc
	return True, acc

def perm(dataset):
	all_datasets = []
	for idx in range(len(dataset)-1):
		op, arg = dataset[idx].split()
		if op == "nop":
			temp_data = dataset.copy()
			temp_data[idx] = f"jmp {arg}"
			all_datasets.append(temp_data)
		elif op == "jmp":
			temp_data = dataset.copy()
			temp_data[idx] = f"nop {arg}"
			all_datasets.append(temp_data)
		else:
			continue
	return all_datasets


def main():
	data = get_data()
	all_datasets = perm(data)
	for dataset in all_datasets:
		success_flag, acc = compiler(dataset)
		if success_flag:
			return acc
	return -1

if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 8 is {result}")
