l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)

for i in range(0, 10, 2):
    print(i)


for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
