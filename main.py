__author__ = '21224'

from percentage import get_percentage,get_percentage_all_chars
from SFCoder import get_table,code,decode

file = open('text.txt','r')
text = file.readline()
# text = 'aaaabbcd'
# text = 'ab     c'
# text = 'aaaabbcd'

alpha = get_percentage(text)
table = get_table(alpha)
code_text = code(text,table)
decoded_text = decode(code_text,table)

alpha2 = get_percentage_all_chars(text)
table2 = get_table(alpha2)
code_text2 = code(text,table2)
decoded_text2 = decode(code_text2,table2)

# print("Only alpha chars:")
# print(table)
# print(code_text)
# print(decoded_text)
# print()

# print("All chars(including whitespace")
# print(table2)
# print(code_text2) 
# print(decoded_text2)

import hamming
import copy

hamming_binary_string = hamming.code_hamming(code_text2)
hamming_binary_string_copy = copy.deepcopy(hamming_binary_string)

noised_hamming = hamming.random_noise(hamming_binary_string_copy)
error_decoded = hamming.decode_hamming(copy.deepcopy(noised_hamming))

for i in range(len(hamming_binary_string)):
    print(hamming_binary_string[i],noised_hamming[i],error_decoded[i])



