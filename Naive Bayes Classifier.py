import sys
import math

#read data

f=open("breast_cancer.data")
data=[]
i=0
l=f.readline()

while(l!=''):
	a=l.split()
	l2=[]
	for j in range(0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f.readline()
rows=len(data)
cols=len(data[0])
f.close()

# read labels

f=open("breast_cancer.trainlabels.0")
trainlabels={}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l !=''):
	a=l.split()
	trainlabels[int(a[1])]=int(a[0])
	l =f.readline()
	n[int(a[0])]+=1

#calculating mean of data
mean0=[]
for j in range(0,cols,1):
	mean0.append(0)
mean1=[]
for j in range(0,cols,1):
	mean1.append(0)
for i in range(0,rows,1):
	if(trainlabels.get(i)!=None and  trainlabels[i]==0):
		for j in range(0,cols,1):
			mean0[j]=mean0[j]+data[i][j]
	if(trainlabels.get(i)!=None and trainlabels[i]==1):		
		for j in range(0,cols,1):
			mean1[j]=mean1[j]+data[i][j]

for j in range(0,cols,1):
	mean0[j]=mean0[j]/n[0]
	mean1[j]=mean1[j]/n[1]


#calculating standard deviation

stdev0=[]
stdev0.append(0)
stdev1=[]
stdev1.append(0)

sqstdev0=[]
for j in range(0,cols,1):
        sqstdev0.append(0)
sqstdev1=[]
for j in range(0,cols,1):
        sqstdev1.append(0)
for i in range(0,rows,1):
        if(trainlabels.get(i)!=None and  trainlabels[i]==0):
                for j in range(0,cols,1):
                        sqstdev0[j]=(mean0[j]-data[i][j])**2
        if(trainlabels.get(i)!=None and trainlabels[i]==1):
                for j in range(0,cols,1):
                        sqstdev1[j]=(mean1[j]-data[i][j])**2
                        
for j in range(0,cols,1):
        stdev0.append(0)
        stdev1.append(1)
        stdev0[j]=(sqstdev0[j]/n[0])**0.5
        stdev1[j]=(sqstdev1[j]/n[1])**0.5
		
pr0=[]
for j in range(0,cols,1):
        pr0.append(0)
pr1=[]
for j in range(0,cols,1):
        pr1.append(0)
for i in range(0,rows,1):
        if(trainlabels.get(i)==None):
                pr0=0
                pr1=0
                for j in range(0,cols,1):
                        pr0=((mean0[j]-data[i][j])/stdev0[j])**2
                        pr1=((mean1[j]-data[i][j])/stdev1[j])**2
                if(pr0<pr1):
                        print("0",i)
                else:
                        print("1",i)
