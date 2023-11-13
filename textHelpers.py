import os

# return a text file as a string
def txtToString(fileName): 
  with open(fileName, 'r') as file:
    stringFile = file.read()
  
  return stringFile

# write a byte string to a text file
def byteStringToTxt(string, newFileName):
  with open(newFileName, 'wb') as file:
    file.write(string)

# write a string to a text file
def stringToTxt(string, newFileName):
  with open(newFileName, 'w') as file:
    file.write(string)

# get text file size in bytes
def txtFileSize(fileName):
  return os.path.getsize(fileName)