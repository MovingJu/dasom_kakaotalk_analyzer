class Kbg_errors(Exception):
    """Kbg의 에러클래스, 확장 계획 아직 없음"""
    
    def __init__(self, message='뭔가 잘못됐습니다. 다시 실행해주세요.'):
        """Kbg의 에러클래스, 확장 계획 아직 없음"""
        
        super().__init__(message)