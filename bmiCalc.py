cm = int(input('請輸入您的身高 => '))
kg = int(input('請輸入您的體重 => '))

def bmiCalc(cm, kg):
  # 計算式
  # BMI = 體重(公斤) / 身高2(公尺2)
  # 例如：一個52公斤的人，身高是155公分，則BMI為 :
  # 52(公斤)/1.552 ( 公尺2 )= 21.6
  # 體重正常範圍為  BMI=18.5～24
  BMI = float(kg / ((cm / 100) ** 2))
  print('BMI 指數 => ', format(BMI, '.2f'))
  scope(BMI)

def scope(range):
  if range < 18.5:
    print('體重太輕')
  elif 18.5 <= range < 24:
    print('體重剛好')
  elif 24 <= range < 27:
    print('體重過重')
  elif 24 <= range < 27:
    print('有點胖')
  elif 27 <= range < 30:
    print('中度肥胖')
  elif 30 <= range < 35:
    print('重度肥胖')
  elif range >= 35:
    print('你只是個肥仔')
  else:
    print('計算錯誤')

bmiCalc(cm, kg)