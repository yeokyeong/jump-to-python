## calculator class
class calculator:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def add(self):
        return self.x+self.y;
    def substract(self):
        return self.x - self.y ;

    def multiple(self):
        return self.x * self.y ;




cal_1 = calculator(3,5)
cal_2 = calculator(10,20)

print(cal_1.add(),cal_1.substract(),cal_1.multiple())
print(cal_2.add(),cal_2.substract(),cal_2.multiple())

##class inheritance
class calculator_advanced(calculator):
    def divide(self):
        return self.x % self.y;
cal_3 = calculator_advanced(10,20)
print(cal_3.add(),cal_3.divide())

##연산자 오버로딩
class teacher:
    def __init__(self,name):
        self.name = name;
    def __add__(self, other):
        print("%s 선생님은 %s 학생을 가르칩니다." % (self.name,other.name))

    def angry(self, other):
        print("%s 선생님은 %s 학생에게 화가났습니다." % (self.name, other.name))

class student:
    def __init__(self, name):
        self.name = name;

teacher01 = teacher("김떙떙")
student01 = student("안떙떙")

teacher01 + student01
teacher01.angry(student01)

##module