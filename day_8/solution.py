input_arr = [line.split(' ') for line in open('input.txt').read().split('\n')]

def find_start_of_loop(arr, program_counter=0):
   """
   Record all the previous indice in set, return index if next index is in set
   """
   prev_indices = set()
   path = []
   accumlator = 0

   while program_counter < len(arr):
      inst = arr[program_counter]
      opcode = inst[0]
      operand = int(inst[1])

      if program_counter in prev_indices:
         break

      prev_indices.add(program_counter)
      path.append((program_counter, opcode, operand))

      if opcode == 'jmp':
         program_counter += operand
      else:
         program_counter += 1
      
      if opcode == 'acc':
         accumlator += operand

   return (accumlator, program_counter, path)

def fix_broken_program(arr):
   _, _, path = find_start_of_loop(arr)

   for inst in path:
      i, opcode, operand = inst
      temp = arr[i]

      # Replace broken inst
      if opcode == 'jmp':
         arr[i] = ('nop', operand)
      elif opcode == 'nop':
         arr[i] = ('jmp', operand)
      else:
         continue

      _, new_pc, _ = find_start_of_loop(arr, i)

      if new_pc == len(arr):
         break
      arr[i] = temp

   # Find accumulated value
   acc, _, _ = find_start_of_loop(arr)

   return acc

if __name__ == '__main__':
   print(find_start_of_loop(input_arr)[0])  # 1489
   print(fix_broken_program(input_arr))   # 1539