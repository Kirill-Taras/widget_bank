def card_type_number(user_input: str) -> str:
    split_str = user_input.split(" ")
    if len(split_str[-1]) == 16:
        return (
               f"{' '.join(split_str[0:len(split_str) - 1])} "
               f"{split_str[-1][0:4]} "
               f"{split_str[-1][4:6]}** **** "
               f"{split_str[-1][-4:]}"
               )
    elif len(split_str[-1]) == 20:
        return f"{' '.join(split_str[0:len(split_str) - 1])} **{split_str[-1][-4:]}"
    else:
        return "Неверный номер счета или карты"
