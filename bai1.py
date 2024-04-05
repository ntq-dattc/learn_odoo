list_data = [[1, 5], [3, 6], [8, 10], [15, 18], [17, 22], [18, 25]]
def merge_value_overlap(list_data):
    for index, data in enumerate(list_data):
        i = 0
        start1 = data[0]
        end1 = data[1]
        while i < len(list_data):
            if i == index:
                break
            start2 = list_data[i][0]
            end2 = list_data[i][1]
            if (start1 >= start2 and start1 <= end2) or (end1 >= start2 and end1 <= end2):
                list_data[index] = [min(start1, start2), max(end1, end2)]
                list_data[i] = [0, 0]
            i += 1
    return list(filter(lambda data: data != [0, 0], list_data))


print(merge_value_overlap(list_data))