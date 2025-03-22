import pandas as pd

import libs

class Kbg:
    """모든 클래스에 대해 상속 받는 클래스
    모든 채팅방의 공통기능을 구현한 곳이자 카카오톡 분석기의 필수기능이 있는 곳"""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.commands = {
            "\\cry": self.cry,
            "\\swear": self.swear,
            "\\laugh": self.laugh
        }
        return

    def execute_command(self, user_input):
        try: 
            self.commands[user_input]()
            return
        except:
            raise libs.Kbg_errors('그런 명령어는 없습니다.')
        
    def execute_text(self, user_input):

        return

    def cry(self):
        print('ㅠㅠ')
        return

    def swear(self):
        print('*$&%#')
        return

    def laugh(self):
        print('kiki')
        return