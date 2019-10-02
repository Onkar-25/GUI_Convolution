import sys

from tkinter import*
root=Tk()
root.title("CONVOLUTION")  # adding title to GUI window
#root.geometry("600x600")

#Creating display for input x[n]
frame=Frame(root)       
frame.pack()
a=Label(frame,text="x[n]=",font=30)   
a.pack(side=LEFT)
num=StringVar()
operator=""
txtDisplay=Entry(frame,textvariable=num,bd=20,insertwidth=2,font=30)
txtDisplay.pack(side=RIGHT)

 #Creating display for input h[n]
frame2=Frame(root) 
frame2.pack()
b=Label(frame2,text="h[n]=",font=30)
b.pack(side=LEFT)
num1=StringVar()
txtDisplay1=Entry(frame2,textvariable=num1,bd=20,insertwidth=2,font=30)
txtDisplay1.pack(side=RIGHT)

#Creating display for output linear convolution
frame3=Frame(root)  
frame3.pack()
c=Label(frame3,text="Lconv",font=30)
c.pack(side=LEFT)
num2=StringVar()
txtDisplay2=Entry(frame3,textvariable=num2,bd=20,insertwidth=2,font=30)
txtDisplay2.pack(side=LEFT)

#Creating display for output circular Convolution
frame4=Frame(root)
frame4.pack()
d=Label(frame4,text="Cconv",font=30)
d.pack(side=LEFT)
num3=StringVar()
txtDisplay3=Entry(frame4,textvariable=num3,bd=20,insertwidth=2,font=30)
txtDisplay3.pack(side=LEFT)



#Code For Linear Convolution
y=0
def lconv():
    global y
    a=num.get()
    b=num1.get()
    x=[]
    c=list(a)
    print(a)
    print(c)
    del(c[0])
    del(c[len(c)-1])
    for i in range(len(c)):
        if c[i]=='-':
            c[i+1]=-int(c[i+1])
            c[i+1]= str(c[i+1])
    for i in c:
        if i=='-':
            c.remove(i)

    for i in range(len(c)):
        if c[ i]==',':
            y=0
        else:
            y=y+1
            if y==2:
                x[v-1]=x[v-1]+c[i]
            else:
                x.append(c[i])
                v=len(x)
            
    print(x)          
    d=list(b)
    del(d[0])
    del(d[len(d)-1])
    for i in range(len(d)):
        if d[i]=='-':
            d[i+1]=-int(d[i+1])
            d[i+1]= str(d[i+1])
    for i in d:
        if i=='-':
            d.remove(i)
    h=[]
    w=0
    for i in range(len(d)):
        if d[ i]==',':
            w=0
        else:
            w=w+1
            if w==2:
                h[p-1]=h[p-1]+d[i]
            else:
               h.append(d[i])
               p=len(h)
    print(h)
    m=len(x)
    n=len(h)
    y=[]
    for i in range(m+n-1):
        y.append(0)
        for j in range(m):
            if ((i-j)>=0 and (i-j)<n):
                y[i]=y[i]+int(x[j])*int(h[i-j])
    s=str(y)
    num2.set(s)
    
    
#Code For Circular Convolution
def circonv():
    a=num.get()
    b=num1.get()
    x=[]
    c=list(a)
    print(x)
    del(c[0])
    del(c[len(c)-1])
    print(len(c))
    print(c)
    for i in range(len(c)):
        if c[ i]==',' or c[i]=='-':
            if c[i]=='-':
                c[i+1]=-int(c[i+1])
        else:
            x.append(c[i])
    print(x)
    d=list(b)
    del(d[0])
    del(d[len(d)-1])
    h=[]
    for i in range(len(d)):
        if d[ i]==',' or d[i]=='-':
            if d[i]=='-':
                d[i+1]=-int(d[i+1])
        else:
            h.append(d[i])
    print(h)
    m=len(x)
    n=len(h)
    if (m-n)>0:
        for i in range(m-n):
            h.append(0)
    elif (m-n)<0:
        for i in range(n-m):
            x.append(0)
    else:
        pass
    print(x)
    print(h)
    N=len(x)  
    y=[]
    for i in range(N):
        y.append(0)
        for j in range(N):
            if (i-j)>=0:
                n=i-j
            else:
                n=i-j+N
            y[i]=y[i]+int(x[j])*int(h[n])
    s=str(y)
    num3.set(s)
    
tframe=Frame(root)
tframe.pack(side=TOP)

#Creating Buttons
button1=Button(tframe,padx=16,activebackground='red',pady=16,text="Linear Convolution",fg="black",bd=10,command=lconv)
button1.pack(side=LEFT)

button2=Button(tframe,padx=16,activebackground='red',pady=16,text="Circular Convolution",fg="black",bd=10,command=circonv)
button2.pack(side=LEFT)
root.mainloop()
