class BMI :
    # 初期化メソッド
    def __init__(self, name):
        self.name = name

    # BMI指数計算
    def BMI_Index (self, height = 0, weight = 0) :
        self.height = height
        self.weight = weight
        index = self.weight / (self.height ** 2)
        self.BMI_Index = round(index, 1)
        if self.BMI_Index < 18.5 :
            print(f"BMI指数は{self.BMI_Index}です。{self.name}さんはやせています。\n")
        elif 18.5 <= self.BMI_Index < 25 :
            print(f"BMI指数は{self.BMI_Index}です。{self.name}さんはふつうです。\n")
        else :
            print(f"BMI指数は{self.BMI_Index}です。{self.name}さんはふとっています。\n")

    # 標準体重計算
    def Nomal_Weight(self) :
        nom_weight = self.height ** 2 * 22
        self.Nomal_Weight = round(nom_weight, 1)
        print(f"{self.name}さんの標準体重は{self.Nomal_Weight}です。\n")

    # 肥満度計算
    def Degree_of_obesity(self) :
        degree = (self.weight - self.Nomal_Weight) / self.Nomal_Weight * 100
        self.Degree_of_obesity = round(degree)
        if 10 <= self.Degree_of_obesity < 20 :
            print(f"肥満度は{self.Degree_of_obesity}％です。{self.name}さんは肥満気味です。\n")
        elif self.Degree_of_obesity >= 20 :
            print(f"肥満度は{self.Degree_of_obesity}％です。{self.name}さんは肥満です。\n")
        else :
            print(f"肥満度は{self.Degree_of_obesity}％です。{self.name}さんは肥満ではありません。\n")
            




