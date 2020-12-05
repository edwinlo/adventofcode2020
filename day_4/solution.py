import re

# Parse input.txt
input_file = open('input.txt')
passports_arr = input_file.read().split('\n\n')

passports = []
for line in passports_arr:
   ele = re.split(' |\n', line)
   passports.append(dict([(x[0], x[1]) for x in (s.split(':') for s in ele)]))

def check_valid_passport(passports):
   res = 0
   for p in passports:
      field_set = set(p)
      if (len(field_set) == 8) or (len(field_set) == 7 and 'cid' not in field_set):
         res += 1
   return res

def check_valid_passport_w_data(passports):
   res = 0
   for p in passports:
      fields = dict(p)
      valid = False

      if (len(fields) == 8) or (len(fields) == 7 and 'cid' not in fields):
         if int(fields['byr']) > 2002 or int(fields['byr']) < 1920:
            continue

         if int(fields['iyr']) > 2020 or int(fields['iyr']) < 2010:
            continue

         if int(fields['eyr']) > 2030 or int(fields['eyr']) < 2020:
            continue
         
         if not re.fullmatch('(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in', fields['hgt']):
            continue

         if not re.fullmatch('#[a-f|0-9]{6}', fields['hcl']):
            continue
            
         if fields['ecl'] not in set(['amb','blu','brn','gry','grn','hzl','oth']):
            continue

         if not re.fullmatch('[0-9]{9}', fields['pid']):
            continue

         res += 1

   return res

if __name__ == '__main__':
   print(check_valid_passport(passports))    # 264
   print(check_valid_passport_w_data(passports)) # 224