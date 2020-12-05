# Parse input.txt
input_file = open('input.txt')
input_arr = [line for line in input_file]

def parse_seat_ids(passes):
   def decode_boarding_pass(p):
      row_lower, row_upper = 0, 127
      col_lower, col_upper = 0, 7

      for c in p:
         mid_row = row_lower + (row_upper - row_lower)//2
         mid_col = col_lower + (col_upper - col_lower) // 2
         if c == "F":
            row_upper = mid_row
         elif c == "B":
            row_lower = mid_row + 1
         elif c == "L":
            col_upper = mid_col
         else:
            col_lower = mid_col + 1   

      return row_upper * 8 + col_upper
   
   return [decode_boarding_pass(p) for p in passes]

def find_missing_seat(pass_ids):
   # find the seat id(s) that are +1/-1 existing in the list, then return middle seat id
   pass_ids.sort()

   for i in range(1, len(pass_ids)):
      if pass_ids[i] - pass_ids[i-1] == 2:
         return pass_ids[i-1] + 1
   
   return None

if __name__ == '__main__':
   print(max(parse_seat_ids(input_arr)))                 # 978
   print(find_missing_seat(parse_seat_ids(input_arr)))   # 727