# Bank transactions sorting function
def filter_by_state(to_sort: list = [], state: str='EXECUTED') -> list:
    finaly_list = []
    for i in range(len(to_sort)):
        if to_sort[i].get(state, "") != "":
            finaly_list.append(to_sort[i])
    return finaly_list
