from jsonwriter import writejson
fw=open(input('file:'),'r')
m=fw.readlines()
fw.close()
fw=open('labels.txt','w')
w=[]
for i in m:
    f=i.find(r'_(')
    if f+1:
        w.append(i[f+3:i.find(r'")')]+'\n')

fw.writelines(set(w))
fw.close()
print('success to write labels at labels.txt')
writejson('labels.txt')
