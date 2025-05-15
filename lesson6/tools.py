def calculate_bmi(height:int, weight:int)->float:
    if height < 120 or height > 220:
            raise Exception(f'輸入的身高: {height} 公分 不在 120 ~ 220 範圍內')
    height /= 100

    if weight < 30.0 or weight > 200.0:
            raise Exception(f'輸入的體重: {weight:.2f} 公斤 不在 30 ~ 200 範圍內')
    
    bmicalculate = weight / height ** 2
    return bmicalculate

def get_state(bmi:float)->str:
    if bmi < 18.5:
        message = '你的體重過輕'
    elif bmi < 24:
        message = '你的體重正常'
    elif bmi < 27:
        message = '你的體重稍微過重'
    elif bmi < 30:
        message = '你已經輕度肥胖'
    elif bmi < 35:
        message = '你已經中度肥胖'
    else:
        message ='你已經重度肥胖'
    return message