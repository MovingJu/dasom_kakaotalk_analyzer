# reference:: https://github.com/Tanat05/korcen-ml  <- 모델 참고해서 욕설 탐지 만들기!

import pandas as pd
import glob
import sys

import libs, datas

def main()->None:
    """전역변수의 사용을 줄이기 위해 정의한 메인 함수"""

    files_name = files.copy()
    if (len(files) == 0):
        raise libs.Kbg_errors('파일이 없습니다!!')
    for idx, value in enumerate(files):
        files_name[idx] = value[value.rindex('/') + 1:value.rindex('.')]
    files_name.append('직접 txt파일 넣기')


    print("다음 파일 중 하나를 골라주세요")
    for idx, value in enumerate(files_name):
        print(f"{idx} : {value}")

    user_input = input('>>> ')
    user_input = libs.is_input_valid(user_input, files_name)
    if user_input == -1:
        raise libs.Kbg_errors('입력이 유효하지 않습니다!')
    

    print("어떤 기능들을 사용할지 알려주세요")
    for idx, value in enumerate(kbg_classes_keys):
        print(f"{idx} : {value}")
    
    user_input_classes = input('>>> ')
    user_input_classes = libs.is_input_valid(user_input_classes, kbg_classes_keys)
    if user_input_classes == -1:
        raise libs.Kbg_errors('입력이 유효하지 않습니다!')
    

    if user_input == len(files_name) - 1:
        lines = []
        print("채팅기록을 입력하세요! \\stop으로 입력 종료하기")
        while True:
            line = input()
            if line == "\\stop": 
                break
            lines.append(line)
        df = libs.preprocessing(lines)
    
    else:
        path = files[user_input]
        df = pd.read_csv(path)


    print('카카오톡 분석기 실행됨!')
    execute_kbg(df, user_input_classes)

    return


def execute_kbg(df: pd.DataFrame, user_input_classes: int) -> None:
    """재귀 형태로 카카오톡 분석기를 계속 실행시킬 함수"""

    def inner():
        user = input("찾을 문자 혹은 명령어 입력 $ ").strip().split('--')
        if user[0] == '\\stop':
            return
        
        try:
            if user[0][0] == '\\':
                malloc.execute_command(user)
            else:
                malloc.execute_text(user)

        except libs.Kbg_errors as e:
            print(e)
            

        inner()

    malloc = kbg_classes_values[user_input_classes](df)
    del df

    print('\\stop 을 입력하면 종료됩니다.')
    inner()

    return


if __name__ == "__main__":  

    try: 

        kbg_classes_keys = ['필수 기능만', '사무적인 채팅방 기능', '잡담하는 채팅방 기능']
        kbg_classes_values = [libs.Kbg, libs.Formal, libs.Casual]

        files = glob.glob(datas.where_csv + '/*')
        main()
        exit()

    except libs.Kbg_errors as e:
        print(e)
        exit()

    except ValueError:
        print('파일이 이상합니다 다시 확인해주세요!')
        exit()

    # except Exception as e:
    #     print('예측하지 못한 에러 발생!:', e)
    #     exit()