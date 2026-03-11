
file=open("demo.txt",mode="w+")
w_data=file.write("family")
print(file.tell)

r_data=file.read()
print(r_data)

file.close()