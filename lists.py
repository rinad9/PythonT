lucky_numbers = [4, 8, 15, 16, 23 ,42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[0])
print(friends[1:3])
friends[1] = "Mike"
print(friends[1])

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Oscar"))

print(friends.count("Jim"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)


# Tuples -- they are non changable once created
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])






