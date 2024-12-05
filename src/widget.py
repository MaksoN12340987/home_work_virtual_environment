import src.masks

def mask_account_card(to_mask: str = None) -> int:
    '''Принимает строку с именем держателя и номером карты и возвращает индекс первой цифры номера'''
    index = 0
    temp = ""
    
    for i in range(len(to_mask)):
        if to_mask[i] == " ":
            if temp.isalpha():
                temp = ""
                i += 1
                index = i
        temp += to_mask[i]
    index + 1
    
    if to_mask[:index] == "Счет ":
        return src.masks.get_mask_account(to_mask, index)
        print(to_mask[0:index])
    else:
        return src.masks.get_mask_card_number(to_mask, index)
