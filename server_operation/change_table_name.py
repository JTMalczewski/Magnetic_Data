# Read in the file
with open('for_tests.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('measurements', 'for_tests')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)