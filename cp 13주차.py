class Beverage :
    def __init__(self):
        self.menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def calculate(self, menu, quantity):
        total_price = 0

        if menu == "커피" :
            total_price = self.menu['커피'] * quantity
        if menu == "녹차" :
            total_price =self.menu['녹차'] * quantity
        if menu == "아이스티":
            total_price =  self.menu['아이스티'] * quantity
        return total_price

user_input_1 = input("메뉴를 입력하세요")
user_input_2 = int(input("수량을 입력하세요"))

print("사용자가 입력한 입력 값 1번은 ",user_input_1)
print("사용자가 입력한 입력 값 2번은 ",user_input_2)

total_price = Beverage()

print(total_price.calculate(user_input_1, user_input_2))


