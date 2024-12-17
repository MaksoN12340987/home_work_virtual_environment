import src.widget

if __name__ == '__main__':
    test_1 = "Visa Platinum 7000792289606361"
    test_2 = "Счет 73654108430135874305"

    print(src.widget.mask_account_card(test_1))
    print(src.widget.mask_account_card(test_2))
