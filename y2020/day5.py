#!/usr/bin/env python3
# --- Day 5: Binary Boarding ---

def highestSeatId():
  return 0

def bsptraverse(tree, idxa, idxb, lsymbol):
  for i in tree:
    m = (idxa + idxb) // 2
    #print(i, m, idxa, idxb)
    if i == lsymbol:
      idxb = m
    else:
      idxa = m + 1

  #print(idxa, idxb)

  return idxa if tree[len(tree) - 1] == lsymbol else idxb


def bsptraverse_comp(treestring):
  return bsptraverse(treestring[0:7], 0, 127, "F") * 8 + bsptraverse(treestring[7:10], 0, 7, "L")

with open('./input/d5.txt') as file:
    data = file.read().splitlines()

assert(bsptraverse_comp('FBFBBFFRLR') == 357)
assert(bsptraverse_comp('BFFFBBFRRR') == 567)
assert(bsptraverse_comp('FFFBBBFRRR') == 119)
assert(bsptraverse_comp('BBFFBBFRLL') == 820)

maxseat = 0
for treerepr in data:
  seat = bsptraverse_comp(treerepr)
  maxseat = seat if seat > maxseat else maxseat

print("What is the highest seat ID on a boarding pass?", maxseat)

seatarray = [0] * 1023
for treerepr in data:
  seat = bsptraverse_comp(treerepr)
  seatarray[seat] = 1

seatid = 0
for s in list(range(1, 1022)):
  if seatarray[s-1] == seatarray[s+1] and seatarray[s] == 0 and seatarray[s-1] == 1:
    seatid = s
    break;

print("What is the ID of your seat? ", seatid)
