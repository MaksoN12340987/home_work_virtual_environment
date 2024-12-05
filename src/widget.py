
def mask_account_card(to_mask: str | None) -> int:
    '''Принимает строку с именем держателя и номером карты и возвращает индекс первой цифры номера'''
    index = 0
    temp = ""
    
    for i in range(len(to_mask)):
        if to_mask[i] == " ":
            if temp.isalpha():
                index = i
                temp = ""
                i += 1
        temp += to_mask[i]
    
    return index + 1
