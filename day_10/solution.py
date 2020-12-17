from collections import defaultdict

input_arr = [int(line) for line in open('input.txt').read().split('\n')]

def adapter_chain_diff(arr):
   sorted_arr = [0] + sorted(arr)
   one_jolts = 0
   three_jolts = 1

   for i in range(1, len(sorted_arr)):
      diff = sorted_arr[i] - sorted_arr[i-1]
      if diff == 1:
         one_jolts += 1
      elif diff == 3:
         three_jolts += 1

   return one_jolts * three_jolts

def possible_adapter_arrangements(arr):
   """
   Modifed climb the stairs DP problem
   """
   sorted_arr = [0] + sorted(arr)
   dp = defaultdict(int)
   nums_set = set(sorted_arr)

   dp[0] = 1    # Base case

   for i in range(1, len(sorted_arr)):
      curr = sorted_arr[i]
      for j in range(1,4):
         if curr - j in nums_set:
            dp[curr] += dp[curr-j]

   return dp[sorted_arr[-1]]

print(adapter_chain_diff(input_arr))  #2070
print(possible_adapter_arrangements(input_arr)) #24179327893504