from datetime import datetime
import pandas as pd

import libs

def parse_date_range(date_range: str, log_data: list):
    # 날짜 범위 파싱: "2025-02-24~2025-02-25"를 시작일과 종료일로 분리
    start_date_str, end_date_str = date_range.split('~')
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    result = {}

    # 각 로그 데이터 처리
    for log in log_data:
        # 로그 데이터에서 날짜, 이름, 내용 추출
        date_str, name, content = log.split(',')
        
        # 로그 데이터의 날짜를 datetime 객체로 변환
        log_date = datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M:%S")
        
        # 날짜가 범위 내에 있으면 딕셔너리에 추가
        if start_date <= log_date <= end_date:
            result[name] = content

    return result

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