import sys

def Cat(filename):
  f = open(filename, 'rU') #rU to ignore dos / unix file endings
  for line in f:
     print line, #Trailing comma inhibits newline through print

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()
