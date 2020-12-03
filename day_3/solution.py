# Read from input.txt
input_arr = [line for line in open("input.txt")]  # input already good as is

def collision_count(arr, right=3, down=1):
   M, N = len(arr), len(arr[0])  # M rows, N columns
   cur_row = cur_col = 0         # Start at top left (0,0)

   collisions = 0

   while cur_row < M:
      if arr[cur_row][cur_col] == '#':
         collisions += 1

      # Update row and col
      cur_row = cur_row + down
      cur_col = (cur_col + right) % (N - 1)
   
   return collisions

def slope_combos(arr):
   slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

   res = 1

   for slope in slopes:
      res *= collision_count(arr, slope[0], slope[1])
   
   return res

if __name__ == '__main__':
   print(collision_count(input_arr))   # 211
   print(slope_combos(input_arr)) #3584591857
