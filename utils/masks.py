# Functional part
def get_mask_card_number(card_number: [int] = None) -> [str]:
    """"""
    number_to_string = str(card_number)
    out_format = ""
    split = 3
    for i in range(len(number_to_string)):
        if i in [6, 7, 8, 9 ,10, 11]:
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
