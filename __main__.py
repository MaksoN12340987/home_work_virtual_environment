import src.widget, src.processing

if __name__ == "__main__":
    
    print(src.widget.mask_account_card(test_1))
    print(src.widget.mask_account_card(test_2))


    print(src.processing.filter_by_state(test_3, "CANCELED"))
    print(src.processing.sort_by_date(test_3, False))
