dec = 500

print(bin(dec)[2:], "in binary.")
print(bin(dec).replace("0b",""), "in binary.")

print(oct(dec)[2:], "in octal.")
print(hex(dec)[2:].upper(), "in hexadecimal.")



num="00001010101111"
print(num.lstrip('0'))
# bin to dec
print(int(num,2))