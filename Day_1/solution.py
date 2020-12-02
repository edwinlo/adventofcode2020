# Read input.txt
input_text = open("input.txt")
input_arr = []

for line in input_text:
   input_arr.append(int(line))

# Part 1
def two_sum_multiply(nums):
   target = 2020
   hash_set = set()

   for num in nums:
      diff = target - num
      if diff in hash_set:
         return num * diff
      hash_set.add(num)
   
   return -1

# Part 2
def three_sum_multiply(nums):
   target = 2020
   nums.sort()

   for i in range(len(nums)-2):
      # a + b + c = 2020
      start, end = i+1, len(nums)-1

      while start < end:
         a = nums[start]
         b = nums[end]
         c = nums[i]

         if a + b + c == target:
            return a * b * c
         elif a + b + c > target:
            end -= 1
         else:
            start += 1

   return -1
         
if __name__ == '__main__':
   print(two_sum_multiply(input_arr))   # 969024
   print(three_sum_multiply(input_arr)) # 230057040