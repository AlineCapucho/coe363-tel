import os

def txt_to_str(file_name): 
  """return a txt file as a string"""
  with open(file_name, 'r') as file:
    str = file.read()
  
  return str

def txt_to_byte(file_name): 
  """return a txt file as bytes"""
  with open(file_name, 'rb') as file:
    bytes = file.read()
  
  return bytes

def byte_to_txt(str, file_name):
  """write bytes to a txt file"""
  with open(file_name, 'wb') as file:
    file.write(str)

def str_to_txt(str, file_name):
  """write a string to a txt file"""
  with open(file_name, 'w') as file:
    file.write(str)

def get_txt_size(file_name):
  """get txt file size in bytes"""
  return os.path.getsize(file_name)
