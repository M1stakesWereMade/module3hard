def calculate_structure_sum(data_structure):
    total_sum = 0
    
    def process_item(item):
        nonlocal total_sum
        if isinstance(item, (list, tuple, set)):
            for i, sub_item in enumerate(item):
                process_item(sub_item)
        elif isinstance(item, dict):
            for key in item:
                process_item(key)
                process_item(item[key])
        elif isinstance(item, int) or isinstance(item, float):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
    
    process_item(data_structure)
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)