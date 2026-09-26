import datetime
def CurrentTimeReturnSay():
    Hour = datetime.datetime.now().hour
    if Hour<5 :
        return "좋은 하루 되세요."
    if Hour<12 :
        return "좋은 아침입니다."
    if Hour<18:
        return "좋은 오후입니다."
    if Hour<22 :
        return "좋은 저녁입니다."
    else :
        return "좋은 밤입니다."