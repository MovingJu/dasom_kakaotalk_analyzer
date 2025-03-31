import libs

class Formal(libs.Kbg):
    """사무적인 대화가 오가는 채팅방을 위한 기능들을 묶어놓은 곳"""

    def __init__(self, df):
        libs.Kbg.__init__(self, df)
        self._commands['\\gongji'] = self.gongji
        self._commands['\\image'] = self.image

    def gongji(self):
        libs.dict_printer(libs.finder(self._df, "톡게시판"))
        return
    
    def image(self):
        image_tuple = ('.png', '.jpg', '.pdf')
        libs.dict_printer(libs.finder(self._df, image_tuple))
        return
    