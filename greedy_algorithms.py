states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'ut', 'nv'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()

states_covered = set()

def find_the_best_station(radio_stations: dict):
    biggest_count = 0
    best_station = None
    for station, states in stations.items():
        total_count_of_uncovered_states = len(states.difference(states_covered))
        if total_count_of_uncovered_states > biggest_count:
            best_station = station
            biggest_count = total_count_of_uncovered_states
    return best_station


while len(states_covered) < len(states_needed):
    best_station = find_the_best_station(stations)
    for s in stations[best_station]:
        states_covered.add(s)
    final_stations.add(best_station)
    stations.pop(best_station)

print(final_stations)