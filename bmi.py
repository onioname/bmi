#BMI 計算程式
height = input('請輸入您的身高(cm)： ')
weight = input('請輸入您的體重(kg)： ')
height = int(height)
weight = int(weight)
height = height / 100 #換算成公尺
bmi = weight / height / height
if bmi < 18.5:
    print('你的bmi值為', bmi, '屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi, '屬體重正常')
elif bmi >= 24 and bmi <27:
    print('你的bmi值為', bmi, '屬體重過重')
elif bmi >= 27 and bmi < 30:
    print('你的bmi值為', bmi, '屬輕度肥胖')
elif bmi >=30 and bmi < 35:
    print('你的bmi值為', bmi, '屬中度肥胖')
else:
    print('你的bmi值為', bmi, '屬重度肥胖')