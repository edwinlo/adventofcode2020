from collections import defaultdict

# Parse input.txt
input_arr = [line.split('\n') for line in open('input.txt').read().split('\n\n')]

def sum_distinct_question_groups(arr):
   counts = 0
   for group in arr:
      s = set()
      for person in group:
         for q in person:
            s.add(q)
      counts += len(s)
   return counts

def sum_same_question_groups(arr):
   counts = 0
   for group in arr:
      d = defaultdict(int)
      for person in group:
         for q in person:
            d[q] += 1
      
      for key, val in d.items():
         if val == len(group):
            counts += 1
   return counts

if __name__ == '__main__':
   print(sum_distinct_question_groups(input_arr)) #6768
   print(sum_same_question_groups(input_arr)) #3489