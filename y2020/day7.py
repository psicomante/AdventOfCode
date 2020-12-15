# --- Day 7: Handy Haversacks ---

from typing import NamedTuple, Dict, List
import re

TEST_INPUT1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

# first regex pass
rgx1 = r"(.*?) bags contain (?:(.*)\.)"

# second regex pass, retrieve contained bags
rgx2 = r"([0-9]+) (.*?) bags?,?"

class BagNode(NamedTuple):
    color: str
    contains: Dict[str, int]
    contained_in: List[str]

def getnode(name: str, graph: Dict[str, BagNode]):
  if name in graph:
    n = graph[name]
  else:
    n = BagNode(name, {}, [])
    graph[name] = n
  
  return n

def build_graph(input_text):
  bags_list = re.findall(rgx1, input_text)

  graphbags = {}

  for line in bags_list:
    colorname = line[0]
    n = getnode(colorname, graphbags)

    contained_bags = re.findall(rgx2, line[1])

    for cbag in contained_bags:
      colorbag_contained = cbag[1]
      qty = cbag[0]
      n.contains[colorbag_contained] = int(qty)

      cbagnode = getnode(colorbag_contained, graphbags)
      cbagnode.contained_in.append(colorname)

  return graphbags

def traverse_graph_back(start, g):
  running = True
  list_containers = set({})
  queue = [start]

  while running:
    nname = queue.pop(0)

    if nname in g:
      [queue.append(el) for el in g[nname].contained_in]
      [list_containers.add(el) for el in g[nname].contained_in]

    if len(queue) == 0:
      running = False

  return list_containers

def traverse_graph_forward(nname, g):
  running = True
  num_bags_contained = 1

  if nname in g:
    for n, qty in g[nname].contains.items():
      num_bags_contained += traverse_graph_forward(n,g) * qty

  return num_bags_contained


graphtest1 = build_graph(TEST_INPUT1)
testresult1 = traverse_graph_back("shiny gold", graphtest1)
assert len(testresult1) == 4

with open('./input/d7.txt') as file:
    data = file.read()
graph1 = build_graph(data)
result1 = traverse_graph_back("shiny gold", graph1)
print("How many bag colors can eventually contain at least one shiny gold bag?", len(result1))

TEST_INPUT2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

graphtest2 = build_graph(TEST_INPUT2)
testresult2 = traverse_graph_forward("shiny gold", graphtest2) - 1
assert testresult2 == 126

print("How many individual bags are required inside your single shiny gold bag?", traverse_graph_forward("shiny gold", graph1) - 1)