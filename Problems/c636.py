while True:
  try:
    year=int(input())
    an=["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
    print(an[((year-1+int(year<0))%12)])
  except:
    break
