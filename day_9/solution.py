# Sliding window solutions

input_arr = [int(line) for line in open('input.txt').read().split('\n')]

def last_valid_idx(arr):
   def check_two_sum(num):
      for i in num_set:
         target = num - i
         if target in num_set:
            return True
      return False

   start = end = 0
   num_set = set()

   while end < len(arr):
      if end - start + 1 <= 25:
         num_set.add(arr[end])
      else:
         if not check_two_sum(arr[end]):
            return arr[end]
         num_set.remove(arr[start])
         num_set.add(arr[end])
         start += 1
      end += 1
   
   return arr[-1]

def contiguous_set_sum(arr, target):
   start = end = 0
   curr_sum = 0

   while end < len(arr):
      if curr_sum == target:
         contiguous_set = arr[start:end]
         return max(contiguous_set) + min(contiguous_set)
         
      if curr_sum > target:
         curr_sum -= arr[start]
         start += 1
      else:
         curr_sum += arr[end]
         end += 1
   return -1

idx = last_valid_idx(input_arr) #57195069
print(contiguous_set_sum(input_arr, idx)) #7409241