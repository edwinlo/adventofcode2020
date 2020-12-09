from collections import defaultdict
from re import findall, match

# gives [color bag, bag1, bag2 ..]
input_txt = [line.strip('.').split('contain') for line in open('input.txt').read().split('\n')]

def build_graph_pt_1(arr):
   graph = defaultdict(set)
   for line in arr:
      src_bag = match('([\w ]+bag)', line[0]).group()
      dest_bags = findall('\d ([\w ]+bag)', line[1])
      for bag in dest_bags:
         graph[src_bag].add(bag)
   return graph

def shiny_bag_colors(graph):
   """
   Run DFS for each node trying to find a path to shiny bag
   - accounts for cycles & disconnected graphs
   """
   def dfs(curr, visited):
      if curr in visited:
         return False
      if curr == "shiny gold bag":
         return True
         
      visited.add(curr)
      for bag in graph[curr]:
         if dfs(bag, visited):
            return True
      return False

   counts = 0
   bags = list(graph.keys())
   for bag in bags:
      if bag != 'shiny gold bag' and dfs(bag, set()):
         counts += 1

   return counts

def build_graph_pt_2(arr):
   graph = defaultdict(set)
   for line in arr:
      src_bag = match('([\w ]+) bag', line[0]).group()
      dest_bags = findall('(\d+) ([\w ]+bag)',line[1])
      for bag in dest_bags:
         bag_count = int(bag[0])
         bag_name = bag[1]
         graph[src_bag].add((bag_count, bag_name))
   return graph

def shiny_bag_count(graph):
   """
   Run DFS for shiny bag node until no bags are left
   - accumulate number of bags in path
   - assume that there can't be cycles
   """
   def dfs(curr):
      count = 0
      for i, bag in graph[curr]:
         count += i + (i * dfs(bag))
      return count
   return dfs("shiny gold bag")

graph_pt_1 = build_graph_pt_1(input_txt)
print(shiny_bag_colors(graph_pt_1)) #224

graph_pt_2 = build_graph_pt_2(input_txt)
print(shiny_bag_count(graph_pt_2)) #1488
           