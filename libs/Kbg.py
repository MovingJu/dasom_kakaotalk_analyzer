import pandas as pd

import libs

class Kbg:
    """모든 클래스에 대해 상속 받는 클래스
    모든 채팅방의 공통기능을 구현한 곳이자 카카오톡 분석기의 필수기능이 있는 곳"""

    def __init__(self, df: pd.DataFrame):
        self._df = df
        self._commands = {
            "\\cry": self.cry,
            "\\swear": self.swear,
            "\\laugh": self.laugh,
            "\\help": self.help
        }
        return

    def execute_command(self, user_input):
        try: 
            self._commands[user_input[0]]()
            return
        except:
            raise libs.Kbg_errors('그런 명령어는 없습니다. \\help로 사용가능한 명령어 보기')
        
    def execute_text(self, user_input):
        libs.dict_printer(libs.finder(self._df, user_input[0]))
        return

    def cry(self):
        cry_tuple = ("ㅠㅠ", "ㅜㅜ", "ㅠㅜ", "ㅜㅠ")
        libs.dict_printer(libs.finder(self._df, cry_tuple))
        return

    def swear(self):
        swear_tuple = ('ㅅㅂ', 'ㅂㅅ', 'ㅗ', 'ㅗㅗ', '엎드려', '탈퇴', '죽이겠습니다','지리는데','지린다','구라','깝치','ㅈ까','억텐','🖕','ㄲㅈ','ㄷㅊ','대가리')
        libs.dict_printer(libs.finder(self._df, swear_tuple))
        return

    def laugh(self):
        laugh_tuple = ('ㅋㅋ','zz','ㅋㅎ','ㅋㄹ','ㅎㅋ','ㄹㅋ')
        libs.dict_printer(libs.finder(self._df, laugh_tuple))
        return
    
    def help(self):
        print('이 클래스가 지원하는 명령어: ')
        for i in self._commands.keys():
            print(i)