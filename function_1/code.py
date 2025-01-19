def dict_converter(chk_dct):
    input_line = list(map(int, chk_dct.split()))
    result = {i: i for i in input_line}
    return result
