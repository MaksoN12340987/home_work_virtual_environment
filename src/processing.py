# Bank transactions sorting function
def filter_by_state(to_sort: list = [], state: str = "EXECUTED") -> list:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключу"""
    finaly_list = []
    for i in range(len(to_sort)):
        if to_sort[i].get(state, "") != "":
            finaly_list.append(to_sort[i])
    return finaly_list


# Sort list by date
def sort_by_date(operation_list: list = [], date: bool = True) -> list:
    """Принимает список словарей и параметр сортировки (по умолчанию "True" — убывание).
    Функция возвращаtn новый список, отсортированный по дате (date)"""
    operation_list.sort(key=lambda operation_list: operation_list["date"][:9], reverse=date)
    return operation_list
