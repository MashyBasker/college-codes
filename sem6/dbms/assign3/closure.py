from typing import List, Tuple, Dict
from itertools import combinations

def parse_input():
    """ Parses the input file and returns the set of relations and the functional dependencies"""
    input_list = open("./input.txt").read().split("\n")
    relations = input_list[0].split(",")
    func_dep = {}
    for i in range(1, len(input_list)):
        sp = input_list[i].split(" -> ")
        l, r = sp[0], sp[1]
        ls, rs = "", ""
        if ',' in l:
            ls = l.split(",")
        else:
            ls = l
        if ',' in r:
            rs = r.split(",")
        else:
            rs = r
        func_dep[tuple(ls)] = tuple(rs)
    return relations, func_dep

def generate_subset(relations: List[str]):
    subsets = []
    n = len(relations)
    for i in range(n+1):
        subsets.extend(combinations(relations, i))
    return subsets

r, f = parse_input()
# print(s)



