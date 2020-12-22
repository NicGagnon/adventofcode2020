from pathlib import Path


def get_data():
	current_dir = Path(__file__).parent
	input_dir = current_dir.joinpath('7.in')
	rules = open(input_dir).read().split('\n')
	return rules

def process_rule_part_one(rule):
	outer_bag, inner_bags = rule.split(' bags contain ')
	return {outer_bag: [" ".join(bag.split()[1:3]) for bag in inner_bags.split(',') if bag != "no other bags."]}

def create_rule_map_part_one(rules):
	rule_map = {}
	#  while this looks bad, it's actually only O(n*m)
	for rule in rules:  # O(n) n being number of rules
		for outer_bag, inner_bag in rule.items():  # O(1)
			for bag in inner_bag:  # O(m) m being rule of bags inside another bag
				if bag in rule_map:
					rule_map[bag].append(outer_bag)
				else:
					rule_map[bag] = [outer_bag]
	return rule_map


def count_bags_part_one(rule_map, target_bag):
	if target_bag not in rule_map:
		return [target_bag]
	else:
		og_list = [target_bag]
		for bag in rule_map[target_bag]:
			og_list.extend(count_bags_part_one(rule_map, bag))
		return og_list

def process_rule_part_two(rules):
	all_rules_map = {}
	for rule in rules:
		outer_bag, inner_bags = rule.split(' bags contain ')
		all_rules_map[outer_bag] = [{" ".join(bag.split()[1:3]): bag.split()[0]} for bag in inner_bags.split(',') if bag != "no other bags."]
	return all_rules_map

def count_bags_part_two(rule_map, target_bag, mult):
	if len(rule_map[target_bag]) == 0:
		return int(mult)
	else:
		return int(mult) + int(mult) * sum([count_bags(rule_map, k, v) for bag in rule_map[target_bag] for k, v in bag.items()])



def main():
	data = get_data()
	rule_map = process_rule_part_two(data)
	total_gold_bags = count_bags_part_two(rule_map, "shiny gold", 1)
	return total_gold_bags - 1

if __name__ == "__main__":
	result = main()
	print(f"Solution for Day 7 is {result}")
