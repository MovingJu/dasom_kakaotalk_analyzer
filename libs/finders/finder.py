from datetime import datetime
import pandas as pd

import libs

def type_seper(func):
    def wrapper(df, user, key_val='name', search_val='context'):
        
        if type(user) == str:
            return func(df, user, key_val, search_val)
        if type(user) == tuple:
            return finder_tuple(df, user, key_val, search_val)
        if type(user) == list:
            return finder_tuple(df, user, key_val, search_val)
        else:
            raise libs.Kbg_errors("올바른 인풋 타입이 아닙니다.")
        
    return wrapper

@type_seper
def finder(df: pd.DataFrame, user, key_val, search_val) -> dict[str : int]:

    result = {}

    for idx, value in enumerate(df[search_val].values):
        if user in value:
            if df[key_val].values[idx] in result.keys():
                result[df[key_val].values[idx]] += 1
                continue
            else:
                result[df[key_val].values[idx]] = 1
                continue
    return result

def finder_tuple(df: pd.DataFrame, user: tuple, key_val='name', search_val='context') -> dict[str : int]:

    result = {}
    passing_column = []

    for i in user:
        for idx, value in enumerate(df[search_val].values):
            if idx in passing_column:
                continue

            if i in value:
                if df[key_val].values[idx] in result.keys():
                    result[df[key_val].values[idx]] += 1
                    continue
                    
                else:
                    result[df[key_val].values[idx]] = 1
                    passing_column.append(idx)
                    continue
    return result

if __name__ == "__main__":
    pass