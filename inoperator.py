def count_matching_items(collection: list, items: list) -> int:
    counter = 0
    for i in items:
        if i in collection:
            counter += 1
    return counter