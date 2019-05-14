money = int(input("請輸入今年收入淨額 : "))
if(money>=2000000):
    print("付稅金額 : " + str(money * 0.3) , end=" 元\n") 
elif(money>=1000000):
    print("付稅金額 : " + str(money * 0.21) , end=" 元\n") 
elif(money>=600000):
    print("付稅金額 : " + str(money * 0.13) , end=" 元\n") 
elif(money>=300000):
    print("付稅金額 : " + str(money * 0.06) , end=" 元\n") 
else:
    print("付稅金額 : " + str(money * 0) , end=" 元\n") 
    
