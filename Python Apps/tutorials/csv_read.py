file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    print(f'{name.title()}')