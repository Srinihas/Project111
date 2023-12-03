import os as o, shutil as s

from_dir = "D:/Downloads"
to_dir = "D:/Uploads"

list = o.listdir(to_dir)
list1 = o.listdir(from_dir)

if list == []:
  x = "no files"
elif list != []:
  x = list 

if list1 == []:
  y = "no files"
elif list1 != []:
  y = list1 

print(f"Uploads folder has {x} in it")
print(f"Downloads folder has {y} in it")

ask = input("Is the above info correct? (input yes or no here:) ").strip().lower()

if ask == "yes":
  for i in list1:
    name, extension =  o.path.splitext(i)
    print(f"name of file is {name} and its file type is {extension}")
else:
  exit()