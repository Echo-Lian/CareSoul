list = []
with open('.env', 'r') as file:
    for line in file:
        list.append(line.split("=")[0])

print(list)
