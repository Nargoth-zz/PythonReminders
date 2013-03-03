import sys

def Cat(filename):
  f = open(filename, 'rU') #rU to ignore dos / unix file endings
  lines = f.readlines()
  print lines

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()
