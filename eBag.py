import math


def assign_order(assembly_lines: dict, order: dict) -> str:
    potential_lines = {}
    order_type = order['type']

    for line, data in assembly_lines.items():
        if order['id'] in data['orders']:
            raise ValueError
        if order_type in data['supported_types'] and len(data['orders']) < data['capacity']:
            potential_lines[line] = data

    lowest_count = math.inf
    for line, data in potential_lines.items():
        if len(data['orders']) < lowest_count:
            lowest_count_lines = [line]
        elif len(data['orders']) == lowest_count:
            lowest_count_lines.append(line)

    order_line = sorted(lowest_count_lines, reverse=True)[0]
    assembly_lines[order_line]['orders'].append(order['id'])
    return order_line


def find_batch_pair(
    waiting_orders: list[dict],
    target_item_count: int,
    ) -> tuple[int, int] | None:

    orders_as_dict = {}
    for order in waiting_orders:
        order_count_needed = target_item_count - order['item_count']
        if order_count_needed in orders_as_dict and order['id'] != orders_as_dict[order_count_needed]:
            return (orders_as_dict[order_count_needed], order['id'])
        if order['item_count'] not in orders_as_dict:
            orders_as_dict[order['item_count']] = order['id']

    return None




assembly_lines = {
   "line-1": {
       "supported_types": {"regular"},
       "capacity": 2,
       "orders": [],
   },
   "line-2": {
       "supported_types": {"regular", "cold"},
       "capacity": 2,
       "orders": [],
   },
}


orders = [
    {"id": 201, "item_count": 6},
    {"id": 202, "item_count": 4},
    {"id": 203, "item_count": 8},
    {"id": 203, "item_count": 8},
    {"id": 206, "item_count": 8},
]


print(find_batch_pair(orders, 16))