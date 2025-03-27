from datetime import datetime
import pandas as pd
import re


def preprocessing(chats_content: list[str]) -> pd.DataFrame:

    date_pattern = r"^\d{4}년 \d{1,2}월 \d{1,2}일 [가-힣]+ \d{1,2}:\d{1,2}"
    content_pattern = r", [가-힣a-zA-Z]+ : .*"

    for i, _ in enumerate(chats_content):
        chats_content[i] = chats_content[i].strip('\ufeff').strip('\n')

    i=1
    while i<len(chats_content):
        if (not re.search(date_pattern, chats_content[i])):
            chats_content[i - 1] += ' ' + chats_content[i]
            chats_content.pop(i)
            i -= 1

        i += 1

    i=0
    while i<len(chats_content):
        if (not re.search(date_pattern+content_pattern, chats_content[i])):
            chats_content.pop(i)
            i -= 1

        i += 1


    date, name, context = [], [], []

    for idx, value in enumerate(chats_content):
        
        date.append(value[:value.index(', ')])
        name.append(value[value.index(', ')+2:value.index(':', value.index(':') + 1)-1])
        context.append(value[value.index(':', value.index(':') + 1)+2:])


    map(str, context)

    for idx, value in enumerate(date):
        value = value.replace('오전', "AM")
        value = value.replace('오후', "PM")

        date[idx] = datetime.strptime(value, "%Y년 %m월 %d일 %p %I:%M")

    return pd.DataFrame({"date":date, "name":name, "context":context})