def skipchar(string, skip, index=0):
   if len(string)<=index:
      return string
   if string[index]==skip:
      string = string[:index]+string[index+1:]
   return skipchar(string, skip, index+1)

print(skipchar("back","a"))
