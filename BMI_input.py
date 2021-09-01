from BMI_health import BMI

print("健康管理アプリケーションへようこそ。")
name = input("名前を入力してください。:")
height = float(input("身長(m)を入力してください。:"))
weight = float(input("体重(kg)を入力してください。:"))

person = BMI(name)

while True :
    print("**********メニュー**********")
    obj = input("1)BMI指数計算   2)標準体重計算   3)肥満度計算   9)終了:")
    try :
        if obj == "1" :
            person.BMI_Index(height, weight)
        elif obj == "2" :
            person.Nomal_Weight()
        elif obj == "3" :
            person.Degree_of_obesity()
        elif obj == "9" :
            print("\nありがとうございました。\n")
            break
        else :
            print("正しい数字を入力してください。")
            continue
    except Exception as e :
        print("エラーになりました。エラー内容は下記の通りです。")
        print(e)

