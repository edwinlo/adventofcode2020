# Read from input.txt

input_file = open("input.txt")
input_arr = []

for line in input_file:
   args = line.split(' ')
   counts = args[0].split('-')
   letter = args[1][0]
   password = args[2]
   input_arr.append((int(counts[0]), int(counts[1]), letter, password))

def count_valid_passwords(arr):
   res = 0
   for line in arr:
      curr_num_letter = 0
      min_count, max_count, letter, password = line
      for c in password:
         if c == letter:
            curr_num_letter += 1
         if curr_num_letter > max_count:
            break
      
      if min_count <= curr_num_letter <= max_count:
         res += 1

   return res

def count_valid_password_2(arr):
   res = 0
   for line in arr:
      i, j, letter, password = line
      # indices are 1 index'ed
      if password[i-1] == letter and password[j-1] == letter or password[i-1] != letter and password[j-1] != letter:
         continue 
      res += 1

   return res

if __name__ == "__main__":
   print(count_valid_passwords(input_arr))   # 586
   print(count_valid_password_2(input_arr))  # 352