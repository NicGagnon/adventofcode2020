from pathlib import Path


def get_data():
    current_dir = Path(__file__).parent
    input_dir = current_dir.joinpath('1.in')
    data = open(input_dir).read().split(',')
    return data


def do_stuff(data):
    pass


def main():
    data = get_data()
    result = do_stuff(data)
    return result


if __name__ == "__main__":
    result = main()
    print(f"Solution for Day 1 is {result}")
