
def index_search_recursive(v, start, end):
    if start > end:
        return False
    else:
        middle = (start + end) // 2
        if v[middle] == middle:
            return True
        else:
            if v[middle] > middle:
                return index_search_recursive(v, start, middle - 1)
            else:
                return index_search_recursive(v, middle + 1, end)


def index_search(v):
    return index_search_recursive(v, 0, len(v) - 1)


# Search index
v = [-2, -1, 0, 2, 4, 6, 7, 8]
print(index_search(v))
