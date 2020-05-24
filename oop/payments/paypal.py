from ecommerce import database
import sys

def main():
    print("inside main...")
    db = database.Database()


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
