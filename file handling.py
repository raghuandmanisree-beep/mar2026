
file=open("demo.txt",mode="w+")
w_data=file.write("family is my everything")
print(file.tell)

r_data=file.read()
print(r_data)

file.close()