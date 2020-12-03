from pathlib import Path


def get_data():
    current_dir = Path(__file__).parent
    input_dir = current_dir.joinpath('3.in')
    data = open(input_dir).read().split('\n')
    return data


def calc_trees(topo_map, x_step, y_step):
    x,y = 0, 0
    tree_count = 0
    while y < len(topo_map):
        if topo_map[y][x] == "#":
            tree_count += 1
        y += y_step
        x = (x + x_step) % len(topo_map[0])
    return tree_count


def create_matrix(data):
    topo_map = [[square for square in row] for row in data]
    return topo_map


def main():
    data = get_data()
    topography_map = create_matrix(data)
    x_steps, y_steps = [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]
    total_trees = 1
    for xs, ys in zip(x_steps, y_steps):
        total_trees *= calc_trees(topography_map, xs, ys)
    return total_trees


if __name__ == "__main__":
    result = main()
    print(f"Solution for Day 3 is {result}")
