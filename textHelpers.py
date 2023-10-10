# return a text file as a string
def txtToString(fileName): 
  with open(fileName, 'r') as file:
    stringFile = file.read()
  
  return stringFile

# write a string to a text file
def stringToTxt(string, newFileName):
  with open(newFileName, 'w') as file:
    file.write(string)