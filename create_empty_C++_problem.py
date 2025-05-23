import sys

if __name__ == '__main__':
    file_name = 'Empty'
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: python create_empty_file [filename]")
    print("Creating " + file_name + "in python dir...")
    with open("C++/" + file_name + ".cpp", 'w'):
        pass
  
    print("Done!")