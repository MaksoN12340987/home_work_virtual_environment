# Проект домашней работы по реализации фукционала работы с банковскими данными

### В прокте реализована функция маскировки номера карты и номера счёта - mask_account_card

## Для работы потребуется виртуальное окружение poetry и python версии 3.13 и выше

### Пакет src:
В модуле widget.py создана функция mask_account_card, которая принимает строку с именем держателя и номером карты или номер счёта и возвращает Имя держателя и замаскированный номер карты или номер счёта
Формат передачи:
*"Visa Platinum 7000792289606361"*
"Счет 73654108430135874305"

*Формат вывода:*
"Visa Platinum 7000 79** **** 6361"
"Счет **4305"

## В разработке

В разработке находится функця filter_by_state, которая принимает список словарей и опционально значение для ключа **state** (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ **state**
 соответствует указанному значению.

Она будет располагаться в пакете src и вызываться в модуле main 

# Homework project on the implementation of functionality for working with bank data

### The project implements the function of masking the card number and account number - mask_account_card

## To work, you will need the poetry virtual environment and python version 3.13 and higher

### Src package:
In the widget.py module, the mask_account_card function is created, which accepts a string with the cardholder name and card number or account number and returns the Cardholder name and the masked card number or account number
*Transmission format:*
"Visa Platinum 7000792289606361"
"Account 73654108430135874305"

*Output format:*
"Visa Platinum 7000 79** **** 6361"
"Account **4305"

## In development

A filter_by_state function is in development, which takes a list of dictionaries and optionally a value for the **state** key (default 'EXECUTED'). The function returns a new list of dictionaries containing only those dictionaries whose **state** key

matches the specified value.

It will be located in the src package and called in the main module