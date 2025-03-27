def dict_printer(dict1: dict):
    """딕셔너리를 카분기의 형태에 맞게 출력해주는 함수."""
    
    for idx in range(len(dict1)):
        print(f"{tuple(dict1.keys())[idx]} : {tuple(dict1.values())[idx]}")

    return