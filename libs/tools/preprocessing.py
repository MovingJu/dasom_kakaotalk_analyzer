import pandas as pd

def preprocessing(chats_content: str) -> pd.DataFrame:
    """유저가 txt를 입력할시 전처리 해서 pandas.Dataframe으로 반환하는 함수"""
    validate_tuple = ('년', '월', '일', ':')

    for i, _ in enumerate(chats_content):
        chats_content[i] = chats_content[i].strip('\ufeff').strip('\n')

    i = 0

    while i<len(chats_content):
        for j in validate_tuple:
            if j not in chats_content[i] or not ('오전' in chats_content[i] or '오후' in chats_content[i]):
                chats_content[i - 1] += ' ' + chats_content[i]
                chats_content.pop(i)
                i -= 1

        i += 1

    i = 0
    while i<len(chats_content):
        try:
            chats_content[i].index(':', chats_content[i].index(':') + 1)
            i += 1
        
        except ValueError:
            chats_content.pop(i)
            i -= 1

    date, name, context = [], [], []

    for idx, value in enumerate(chats_content):
        
        try:

            date.append(value[:value.index(', ')])
            name.append(value[value.index(', ')+2:value.index(':', value.index(':') + 1)-1])
            context.append(value[value.index(':', value.index(':') + 1)+2:])

        except ValueError:
            continue

    map(str, context)

    return pd.DataFrame({"date":date, "name":name, "context":context})