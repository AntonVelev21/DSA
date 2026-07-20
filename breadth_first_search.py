from collections import deque


graph = {}
graph['you'] = ['alice', 'bob', 'clarie']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['clarie'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

checked_people = {}

def is_mago_seller(name):
    return name[-1] == 'm'

search_queue = deque()
search_queue += graph['you']

while search_queue:
    current_person = search_queue.popleft()
    if current_person not in checked_people:
        if is_mago_seller(current_person):
            print(f'The mango seller is {current_person}')
            break
        else:
            checked_people[current_person] = True
            search_queue += graph[current_person]


