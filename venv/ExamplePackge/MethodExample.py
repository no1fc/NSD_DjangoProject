class Circie:
    #메서드 내에 전체적으로 사용할
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius**2 * Circie.pi

myCircle = Circie(5)
print(myCircle.area())

