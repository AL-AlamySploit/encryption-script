import compileall
import os
os.system("clear")
print ("      Welcome   user        ")
encrypt = raw_input ("enrypt : ")
#compileall.compile_dir('')
A1 = compileall.compile_dir(encrypt)
print "[+]" + A1
