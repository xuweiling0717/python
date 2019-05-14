month = input("請輸入月份 : ")
if(int(month) >= 13):
    print(month + " 月份不在範圍內!")
elif(int(month) >= 10):
    print(month +  " 月是冬天!")
elif(int(month) >= 7):
    print(month +  " 月是秋天!")
elif(int(month) >= 4):
    print(month +  " 月是夏天!")
else:
    print(month +  " 月是春天!")