import sys

if __name__ == '__main__':
    file_name = 'test'
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Usage: python create_empty_file [filename]")
    print("Creating " + file_name + "in python dir...")
    with open("Python/" + file_name + ".py", 'w'):
        pass
  
    print("Done!")