class A:
    def showA(self):
        print("I am in class A")

class B(A):
    def showB(self):
        print("I am in class B")

class C(A):
    def showC(self):
        print("I am in class C")

class D(B, C):  
    def showD(self):
        print("I am in class D")

if __name__ == '__main__':
    obj = D()
    obj.showA()
    obj.showB()
    obj.showC()
    obj.showD()