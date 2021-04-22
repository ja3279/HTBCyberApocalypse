import re
import sys

name_of_file = sys.argv[1]

letters = 'abcdef'
digits = '0123456789'

keys = [x+y for x in letters for y in letters] + [x+y for x in digits for y in digits] + [x+y for x in letters for y in digits] +  [x+y for x in digits for y in letters]

flag_part = 'CHTB{'

text_in_string = ''

line_count = 0

with open(name_of_file,'r') as f:
        for line in f:
            text_in_string += line.strip('\n')
            line_count += 1

text_in_string = bytes.fromhex(text_in_string)

for key in keys:
    key_bytes = bytes.fromhex(key*26*line_count)
    xor_line = bytes([x^y for (x,y) in zip(text_in_string,key_bytes)])
    result = xor_line.decode('utf-8',errors='replace')
    if flag_part in result: 
        flag = re.findall(r"CHTB\{\w*\}",result)
        print(flag)
        print(key)
        break;
