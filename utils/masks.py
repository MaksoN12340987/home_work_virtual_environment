# Functional part
def get_mask_card_number(card_number: [int] = None) -> [str]:
    """принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    number_to_string = str(card_number)
    out_format = ""
    split = 3

    for i in range(len(number_to_string)):
        if i in [6, 7, 8, 9, 10, 11]:
            out_format += "*"
            if i == split:
                out_format += " "
                split += 4
        else:
            out_format += number_to_string[i]
            if i == split:
                out_format += " "
                split += 4
    return out_format


def get_mask_account(bank_account: [int] = None) -> [str]:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    number_to_string = str(card_number)
    out_format = ""

    for i in range(len(number_to_string)):
        if i in [0, 1]:
            out_format += "*"
        else:
            out_format += number_to_string[i]
    return out_format
