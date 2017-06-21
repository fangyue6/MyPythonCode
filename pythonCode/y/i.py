# for i in range(1,10):
# 	f=open("D:/y_error___.csv", "ab+")
# 	f.write(str(i)+"\n")
# 	f.close()
files=["y_error.txt","y_error_129_160.txt","y_error_161_190.txt","y_error_191_222.txt","y_error_final.txt"]
index=[]
for fi in files:
	f=open(fi,"r")
	for i in f:
		index.append(i.strip())
for i in index:
	print(i)