class Cat :
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def print_cat(self):
        print(f"Имя: {self.name}, Пол: {self.sex}, Возраст: {self.age}")
