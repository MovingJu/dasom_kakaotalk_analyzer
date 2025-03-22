class Kbg:
    """모든 클래스에 대해 상속 받는 클래스
    모든 채팅방의 공통기능을 구현한 곳이자 카카오톡 분석기의 필수기능이 있는 곳"""

    def __init__(self, path):
        self.path = path
        self.commands = {
            "\\cry": self.cry,
            "\\swear": self.swear,
            "\\laugh": self.laugh
        }
        
    def cry(self):
        print('ㅠㅠ')

    def swear(self):
        print('*$&%#')

    def laugh(self):
        print('kiki')