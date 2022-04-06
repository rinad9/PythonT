
# for every letter in blablabla:
#   Do something
from unittest import result


for letter in "Giraffe Academy":
    print(letter)

friends = [ "Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")


# 2 raised to the 3rd power
print(2**3)

# Exponent Function bu for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result =result * base_num
    return result

print(raise_to_power(3, 4))
