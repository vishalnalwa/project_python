def func_a():
    print('you entered a')

def func_b():
    print('you entered b')

def func_c():
        print('you entered c')

option = input("enter option (a,b,c)\n")
if option == 'a' :
  func_a()
elif option == 'b' :
  func_b ()
elif option == 'c' :
  func_c()
else :
  print("please enter a valid choice")
