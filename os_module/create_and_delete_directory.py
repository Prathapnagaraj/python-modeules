__author__ = 'pbillava'
import os

file_name="example.txt"
folder="myexaple"
if folder not in os.listdir(os.getcwd()):
    os.makedirs(folder)

file_path=os.path.join(folder,file_name)
f=open(file_path,'wt')
try:
    f.write("Hello world")
except:
    pass
finally:
    f.close()

print "list folders"
print os.listdir(os.getcwd())
print "listing file in ", folder
print os.listdir(folder)

print "removing "
os.unlink(file_path)
os.rmdir(folder)
print os.listdir(os.getcwd())