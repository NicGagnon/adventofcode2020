from pathlib import Path
import re


def get_data():
    current_dir = Path(__file__).parent
    input_dir = current_dir.joinpath('4.in')
    data = open(input_dir).read().split('\n')
    passport_master_list = []
    ind_passport = {}
    for i in data:
        if i:
            for d in i.split():
                ind_passport[d.split(":")[0]] = d.split(":")[1]
        else:
            passport_master_list.append(ind_passport.copy())
            ind_passport.clear()
    return passport_master_list


def validate_passport(pass_data):
    if len(pass_data.keys()) == 7:
        if "cid" not in pass_data.keys():
           return True
    return len(pass_data.keys()) == 8

def validate_passport_verbose(pass_data):
    if not 1920 <= int(pass_data.get('byr', 0)) <= 2002:
        return False
    if not 2010 <= int(pass_data.get('iyr', 0)) <= 2020:
        return False
    if not 2020 <= int(pass_data.get('eyr', 0)) <= 2030:
        return False
    if not (pass_data.get('hgt', "fake")[-2:] == "cm" or pass_data.get('hgt', "fake")[-2:] == "in"):
        return False
    if pass_data.get('hgt', "fake")[-2:] == "cm":
        if not 150 <= int(pass_data.get('hgt', "fake")[:-2]) <= 193:
            return False
    else:
        if not 59 <= int(pass_data.get('hgt', "fake")[:-2]) <= 76:
            return False
    regex_results = re.search("^#[0-9a-f]{6}", pass_data.get('hcl', "fake"))
    if regex_results is None:
        return False
    if pass_data.get('ecl', "") not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return len(pass_data.get('pid', "fake")) == 9



def main():
    data = get_data()
    valid_passport_count = [validate_passport_verbose(passport_data) for passport_data in data].count(True)
    return valid_passport_count


if __name__ == "__main__":
    result = main()
    print(f"Solution for Day 4 is {result}")
