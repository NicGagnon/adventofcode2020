from pathlib import Path


def get_data():
    current_dir = Path(__file__).parent
    input_dir = current_dir.joinpath('2.in')
    data = open(input_dir).read().split('\n')
    return data


def validate_policy(data):
    policies_passed = 0
    for policy in data:
        rule, name, password = policy.split()
        lend, hend = rule.split('-')
        if int(lend) <= password.count(f"{name[0]}") <= int(hend):
            policies_passed += 1
    return policies_passed


def validate_position_policy(data):
    policies_passed = 0
    for policy in data:
        rule, name, password = policy.split()
        fpos, spos = rule.split('-')
        if (password[int(fpos)-1] == name[0] and password[int(spos)-1] != name[0]) or\
                (password[int(fpos)-1] != name[0] and password[int(spos)-1] == name[0]):\
                    policies_passed += 1
    return policies_passed


def main():
    data = get_data()
    result = validate_position_policy(data)
    return result


if __name__ == "__main__":
    result = main()
    print(f"Solution for Day 2 is {result}")
