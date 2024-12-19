import pytest

import src.widget, src.processing

assert src.widget.mask_account_card(card_number) == "Visa Platinum 7000 79** **** 6361"