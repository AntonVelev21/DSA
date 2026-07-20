voted_people = {}

while True:
    name = input()
    if name in voted_people:
        print(f'{name} already voted!')
    else:
        voted_people[name] = 'Yes'