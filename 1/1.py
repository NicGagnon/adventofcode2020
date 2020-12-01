from pathlib import Path


def get_data():
    current_dir = Path(__file__).parent
    input_dir = current_dir.joinpath('1.in')
    data = [int(i) for i in open(input_dir).read().split('\n')]
    return data


def mult_two_numbers(data):
    addition_mapping = {}
    for i in data:
        addition_mapping[2020-i] = i
    for i in data:
        if i in addition_mapping:
            return i * addition_mapping[i]
    return -1

def mult_three_numbers(data):
    addition_mapping = {}
    for i in data:
        addition_mapping[2020-i] = i
    for i in data:
        for j in data[1:]:
            if i + j in addition_mapping:
                return i * j * addition_mapping[i+j]
    return -1

def main():
    data = get_data()
    result = mult_three_numbers(data)
    return result


if __name__ == "__main__":
    result = main()
    print(f"Solution for Day 1 is {result}")
