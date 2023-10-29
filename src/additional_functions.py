def matching_letters(list_word: list[str]) -> list:
    final_list = list()
    for word in list_word:
        if word == '':
            final_list.append(word)
        elif word[0] == word[-1]:
            final_list.append(word)
    return final_list


def max_numbers(list_numbers: list[int]) -> int:
    max_number = 0
    for one in range(len(list_numbers)):
        for two in range(len(list_numbers)):
            if one == two:
                continue
            elif list_numbers[one] * list_numbers[two] > max_number:
                max_number = list_numbers[one] * list_numbers[two]
    return max_number
