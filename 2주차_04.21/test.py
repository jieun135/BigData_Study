class FourCal:
    def setdata(self,first,second): # 메서드의 메개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.
        self.first = first #메서드의 수행문 a.first = first 로 해석된다. 
        self.second = second #메서드의 수행문
    def add(self): #add메서드가 호출된다. 
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
        
class More(FourCal): # 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
    pass

a = FourCal()
b = FourCal()
c = More()

a.setdata(4,2)
b.setdata(3,7) # 클래스로 만든 객체의 객체 변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.
c.setdata(4,2)

print(a.add())
print(b.mul())
print(c.mul())
# print(b.second)

