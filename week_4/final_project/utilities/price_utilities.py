def _find_first_number_index(str_):
    for i, char in enumerate(str_):
        if char.isdigit():
            return i
    return -1


def _find_last_number_index(str_):
    for i, char in reversed(list(enumerate(str_))):
        if char.isdigit():
            return i
    return -1


def get_float_price_from_str(price_str):
    l_num = _find_first_number_index(price_str)
    r_num = _find_last_number_index(price_str)
    price_str = price_str.replace(',', '.')

    return float(price_str[l_num:r_num+1])