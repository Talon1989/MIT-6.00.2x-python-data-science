num1 = 8  #  00001000
num2 = 24  # 00011000


print('8 & 24 : ', 8 & 24)  #  AND       00001000  need both to 1 to set 1
print('8 | 24 : ', 8 | 24)  #  0R        00011000  just 1 to set 1
print('8 ^ 24 : ', 8 ^ 24)  #  XOR       00010000  1 changes to 1, 2 changes to 0
print('~ 8 : ', ~ 8)        # OR NOT     11110111  inverts all 0 and 1
print('8 << 3: ', 8 << 3)  # LEFT SHIFT 01000000  shift all 1 over 3 places left