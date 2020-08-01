class fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return fraction(newnum,newden)

a=fraction(2,3)
b=fraction(4,5)
f3=a+b
print(f3)