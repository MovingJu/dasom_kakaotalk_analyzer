def is_input_valid(user_input: str, li0: list[str]) -> int:
    """유저의 입력값이 리스트 안에 있는지 판단하는 함수"""

    try:
        user_input = int(user_input)
        if user_input >= len(li0):
            return -1
        else:
            return user_input

    except ValueError:
        for idx, val in enumerate(li0):
            if user_input == val:
                return idx
        else:
            return -1
    
    except Exception:
        return -1