
#Author:Anliu
import shutil,os
with open("test01","w",encoding="utf-8") as f1:
    f1.write("This is a test test01")

with open("test02","w",encoding="utf-8") as f2:
    f2.write("THis is a test test02")

#shutil.copymode("test01","test02")
shutil.make_archive("test02","tar",r"c:\\",".")
shutil. unpack_archive()