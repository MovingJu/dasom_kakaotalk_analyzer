import libs

class Casual(libs.Kbg):
    """일상적인 대화가 오가는 채팅방을 위한 기능들을 묶어놓은 곳"""
    
    def __init__(self, df):
        libs.Kbg.__init__(self, df)
        self._commands['\\uhaha'] = self.uhaha


    def uhaha(self):
        print('uhaha')