def card_type_number(type_card: str, number_card: str) -> str:
    return f"{type_card} {number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"

