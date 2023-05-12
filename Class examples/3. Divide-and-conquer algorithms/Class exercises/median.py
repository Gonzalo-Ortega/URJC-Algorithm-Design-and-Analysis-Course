# Median from two vectors
# (Sorted arrays smell to binary search)

def median_recursive(v1, start_1, end_1, v2, start_2, end_2):
    if start_1 == end_1 and start_2 == end_2:
        return min(v1[start_1], v2[start_2])
    elif start_1 == end_1 - 1 and start_2 == end_2 - 1:
        # Median form two element vectors
        if v1[end_1] < v2[end_2]:
            return v1[end_1]
        elif v1[end_1] > v2[end_2]:
            return v2[end_2]
        else:
            pass # incomplete

    else: # General case:
        middle_1 = (start_1 + end_1) // 2
        middle_2 = (start_2 + end_2) // 2
        if v1[middle_1] == v2[middle_2]:
            return v1[middle_1]
        elif v1[middle_1] < v2[middle_2]:
            return median_recursive(v1, middle_1, end_1, v2, start_2, middle_2)






def median(v1, v2):
    return median_recursive(v1, 0, len(v1) - 1, v2, 0, len(v2) - 1)


def main():
    v1 = [1, 2, 3, 4, 6, 7, 8, 9]
    v2 = [0, 5, 9, 11, 12, 13, 14, 15]

    print(median(v1, v2))