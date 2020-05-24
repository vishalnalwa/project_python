import pyclass
import ecommerce.database
import sys

def main():
    print("inside main...")
    pc = pyclass.MyFirstClass()
    db = ecommerce.database.Database()
    print(sys.path)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
