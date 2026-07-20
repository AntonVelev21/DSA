graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['c'] = {}
graph['c']['fin'] = 0
graph['fin'] = {}

costs = {}
infinity = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['c'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_the_lowest_node(nodes):
    lowest_cost = infinity
    lowest_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node


current_node = find_the_lowest_node(costs)
while current_node is not None:
    current_cost = costs[current_node]
    neighbors = graph[current_node]
    for n, c in neighbors.items():
        if current_cost + c < costs[n]:
            costs[n] = current_cost + c
            parents[n] = current_node

    processed.append(current_node)
    current_node = find_the_lowest_node(costs)


