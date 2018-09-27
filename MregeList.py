# A function to merge two lists into one


def merge(list_1, list_2):

    # set method used to only show unique elements in list

    merged_list = set(list_1 + list_2)

    print(merged_list)


merge([2, 3, 4], [4, 5, 6, 7])
