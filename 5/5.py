from pathlib import Path
import re


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('5.in')
	data = open(input_dir).read().split('\n')
	return data


def get_seat_number(seat_num):
	row = seat_num[:7]
	row_bin = row.replace("F", "0").replace("B", "1")
	row_value = int(row_bin, 2)
	col = seat_num[7:]
	col_bin = col.replace("L", "0").replace("R", "1")
	col_value = int(col_bin, 2)
	return row_value * 8 + col_value


def main():
	data = get_data()
	seat_values = [get_seat_number(i) for i in data]
	#  return max(seat_values) Answer for part 1
	sorted_seat_values = sorted(seat_values)
	for i in range(127*8+7):
		if i-1 in sorted_seat_values and i+1 in sorted_seat_values and i not in sorted_seat_values:
			return i
	return -1


if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 5 is {result}")
