# to do:: 시작시, 사용자가 직접 입력한 경우, preprocess하고 저장해서 실행하는 코드 만들기.

import pandas as pd
import glob

import libs, datas

def main()->None:
    """전역변수의 사용을 줄이기 위해 정의한 메인 함수"""

    kbg_classes = ['필수 기능만', '사무적인 채팅방 기능', '잡담하는 채팅방 기능']


    files = glob.glob(datas.where_csv + '/*')
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
    for idx, value in enumerate(kbg_classes):
        print(f"{idx} : {value}")
    
    user_input_classes = input('>>> ')
    user_input_classes = libs.is_input_valid(user_input_classes, kbg_classes)
    if user_input_classes == -1:
        raise libs.Kbg_errors('입력이 유효하지 않습니다!')
    

    if user_input == len(files_name) - 1:
        print('채팅 로그를 입력해주세요!')
        user_txt = input()
        df = libs.preprocessing(user_txt)
    
    else:
        path = files[user_input]
        df = pd.read_csv(path)


    print('카카오톡 분석기 실행됨!')
    execute_kbg(df, user_input, user_input_classes)

    return


def execute_kbg(df: pd.DataFrame, user_input: int, user_input_classes: int) -> None:
    """재귀 형태로 카카오톡 분석기를 계속 실행시킬 함수"""

    def inner():
        user_input = input("$ ")
        if user_input == '\\break':
            return
        
        print('Uhaha')

        inner()

    print('\\break 를 입력하면 종료됩니다.')
    inner()

    return


if __name__ == "__main__":  

    try: 
        main()
        exit()

    except libs.Kbg_errors as e:
        print(e)
        exit()

    except ValueError:
        print('파일이 이상합니다 다시 확인해주세요!')
        exit()

    except Exception as e:
        print('예측하지 못한 에러 발생!:', e)
        exit()