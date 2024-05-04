import os

os.system("PropertyGen.exe source/property")
os.system("move property.xml source/root/property.xml")
