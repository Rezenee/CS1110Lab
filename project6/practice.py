import random
with open("words.txt", 'r') as f:
    dict1 = {}
    with open('words.txt') as f:
        for line in f:
            key, value = line.strip().split(':')
            values = value.split(',')
            dict1[key] = [word.strip() for word in values]

print(dict1)
print(f"len(dict['school']) == {len(dict1['school'])}")


