class MyFirstClass:
    def __init__(self):
        print("I am a new instance of MyFirstClass")

    def hello(self):
        print('Hello from MyFirstClass')


class MySecondClass:
    def __init__(self):
        print("I am a new instance of MySecondClass")
    
    def hello(self):
        print('Hello from MyFirstClass')

class MyThirdClass:
    def __init__(self):
        print("I am a new instance of MyThirdClass")
    def hello(self):
        print('Hello from MyFirstClass')

def main():
    mfc = MyFirstClass()
    msc = MySecondClass()
    mtc = MyThirdClass()

if __name__ == '__main__':
    main()
