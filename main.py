class Widget():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
    def print_info(self):
        print(f'Напис: {self.text}')
        print(f'Розташування: {self.x, self.y}')

class Button(Widget):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.is_clicked = False
    
    def click(self):
        self.is_clicked = True
        print('Ви зареєстровані')

btn = Button('Брати участь', 100, 100)
btn.print_info()

while True:
    
    question = input('Хочете зареєструватися? (так / ні): ').lower().strip()
    if question == 'так':
        btn.click()
        break
    elif question == 'ні':
        print('А шкода!')
        break
    elif question.__contains__('print') or question.__contains__("hack"):
        print('Хаха, Гарна спроба.')
    else:
        print("Помилка")
