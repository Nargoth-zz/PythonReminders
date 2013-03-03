import sys
import os

def List(dir):
  print 'Print list of filenames in dir' 
  filenames = os.listdir(dir)
  print filenames
  for filename in filenames:
    path = os.path.join(dir, filename) #join dir and filename, considering system specific writing
    print path
    print os.path.abspath(path) #obtain an absolute path

def main():
  if os.path.exists(sys.argv[1]): #check if a file / path exists
    List(sys.argv[1])
  else:
    print sys.argv[1], 'does not exist'

  os.mkdir('./newdir') #create a new directory 

  import commands
  import shutil
 
  filename = './newdir/test.txt' 
  cmd = 'touch ' + filename
  print 'about to do this:', cmd
  (status, output) = commands.getstatusoutput(cmd) #execute external commands 

  if status:
    sys.stderr.write('there was an error:', output)
    sys.exit()

  print output 
  
  source = './newdir/test.txt'
  dest = './newdir/copyoftest.txt' 
  shutil.copy(source, dest) #copy files from source to dest

if __name__ == '__main__':
  main()
