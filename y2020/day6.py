#!/usr/bin/env python3
# --- Day 6: Custom Customs ---

TEST_INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def count_diff_yeses(groups):
  diff_answ = 0
  for group in groups:
    people = group.split("\n")
    answers = {an for per in people for an in per}
    diff_answ += len(answers)
  
  return diff_answ

def count_all_answered(groups):
  all_answ = 0
  for group in groups:
    answers_group = group.split("\n")

    answ_dict = {}
    partial_all_answ = 0
    people_count = len(answers_group)
    for person in answers_group:
      for answ in person:
        answ_dict[answ] = answ_dict.get(answ, 0) + 1

    all_answ += list(answ_dict.values()).count(people_count)
    #print(people_count, answ_dict, all_answ)
  return all_answ

test1 = count_diff_yeses(TEST_INPUT.split("\n\n"))
assert(test1 == 11)

with open('./input/d6.txt') as file:
    data = file.read().split("\n\n")

print("What is the sum of those counts?", count_diff_yeses(data))

test2 = count_all_answered(TEST_INPUT.split("\n\n"))
print(test2)
assert(test2 == 6)

with open('./input/d6.txt') as file:
    data = file.read().split("\n\n")

print("For each group, count the number of questions to which everyone answered yes. What is the sum of those counts?", count_all_answered(data))
