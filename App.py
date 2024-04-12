import sys
from config import DB_DETAILS 

# def main():
#     print('Hello World!')

#     for arg in sys.argv:
#         print(arg)


def main():
    """Program takes at least one program"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print (db_details)


 

# main()

if __name__ == '__main__':
    main()