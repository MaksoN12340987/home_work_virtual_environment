# Bank transactions sorting function
def filter_by_state(to_sort: list = [], state: str='EXECUTED') -> list:
    '''Принимает список словарей и ключ: state (по умолчанию 'EXECUTED'). 
       Возвращает новый список словарей, содержащий словари соответствующих ключу'''
    finaly_list = []
    for i in range(len(to_sort)):
        if to_sort[i].get(state, "") != "":
            finaly_list.append(to_sort[i])
    return finaly_list


# Sort list by date
def sort_products_by_quantity(operation_list: list = [], date: bool=False) -> list:
    '''Принимает список словарей и параметр сортировки (по умолчанию — убывание). 
       Функция возвращаtn новый список, отсортированный по дате (date)'''
    for i in range(len(operation_list)):
        if not operation_list[i].get("quantity", False):
            item = operation_list.pop(ist_product[i])
    operation_list.sort(key=lambda operation_list: operation_list[date], reverse=ascending)
    return ist_product

