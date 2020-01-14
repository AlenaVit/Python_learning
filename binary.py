# for i in range (386, 388):
#     print("{0:>2} in binary is {0:>08b}".format(i))

# for i in range (29):
#     print("{0:>2} in hex {0:>02x}".format(i))
#
#
# x = 0x20
# y = 0x0a
# print(x)
# print(y)
# print(x * y)


# for i in range(0,17):

powers = []
for power in range (15, -1, -1):
    powers.append (2 ** power)

print(powers)

x = int(input("Enter a number: "))
for power in powers:
    print(x // power, end='')
    x %= power
