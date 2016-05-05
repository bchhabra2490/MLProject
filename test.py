from Tkinter import Frame, Tk, BOTH, Text, Menu,Label,LEFT,X,N,Button,Entry,RIGHT,PhotoImage, END
import tkFileDialog 
import tkMessageBox as mbox
import os
import csv


class Example(Frame):
  
    def __init__(self, parent,theta,m,attr):
        Frame.__init__(self, parent)   
        self.theta=theta
        self.m=m
        self.attr=attr
        self.parent = parent        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Property Rate Prediction System")
        self.pack(fill=BOTH, expand=1)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        wel = Label(self, text="Welcome to property rate predictor", font=("Helvetica", 30))
        wel.place( x=200,y=150)
        fileMenu = Menu(menubar)       
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)


        menubar.add_cascade(label="File", underline=0, menu=fileMenu)       
        
        L1 = Label(self, text="Size of property")
        L1.place( x=20,y=30)
        E1 = Entry(self, bd =5)
        E1.place( x=150,y=30)

        L2 = Label(self, text="Swimming pool")
        L2.place( x=20,y=60)
        E2 = Entry(self, bd =5)
        E2.place( x=150,y=60)

        L3 = Label(self, text="type")
        L3.place( x=20,y=90)
        E3 = Entry(self, bd =5)
        E3.place( x=150,y=90)

        L4 = Label(self, text="Interior")
        L4.place( x=20,y=120)
        E4 = Entry(self, bd =5)
        E4.place( x=150,y=120)

        L5 = Label(self, text="Lawn")
        L5.place( x=20,y=150)
        E5 = Entry(self, bd =5)
        E5.place( x=150,y=150)

        L6 = Label(self, text="View")
        L6.place( x=20,y=180)
        E6 = Entry(self, bd =5)
        E6.place( x=150,y=180)


        L7 = Label(self, text="Locality")
        L7.place( x=20,y=210)
        E7 = Entry(self, bd =5)
        E7.place( x=150,y=210)

        L8 = Label(self, text="Bathrooms")
        L8.place( x=20,y=240)
        E8 = Entry(self, bd =5)
        E8.place( x=150,y=240)

        L9 = Label(self, text="Parking")
        L9.place( x=20,y=270)
        E9 = Entry(self, bd =5)
        E9.place( x=150,y=270)

        cal=Button(self, text="Calculate", command=lambda:self.cal(filename,E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),E9.get()))
        cal.place( x=100,y=300)

        exit=Button(self, text="Calculate", command=self.onExit)
        cal.place( x=200,y=300)

    def cal(self,filename,size,pool,typ,interior,lawn,view,locality,bathrooms,parking):
            #all the alculation goes here
            ##room,type,interior,lawn,swimming,view,locality,bathrooms,parking,price
            newdata=[]
            newdata.append(size)
            newdata.append(typ)
            newdata.append(interior)
            newdata.append(lawn)
            newdata.append(pool)
            newdata.append(view)
            newdata.append(locality)
            newdata.append(bathrooms)
            newdata.append(parking)
            res=hypo(newdata,self.theta,self.m,self.attr)
            self.onInfo(res)

    def onExit(self):
        self.quit()    
    def onInfo(self,res):
        mbox.showinfo("Result", "Predicted price is "+str(res))
def normalise(data,m,attr):
    mean=[]
    std=[]
    for i in range(attr):
        mean.append(0)
        for j in range(m):
            mean[i]=mean[i]+float(int(data[j][i]))
        mean[i]=mean[i]/m
    for i in range(attr):
        std.append(0)
        sigma=0
        for j in range(m):
            sigma=sigma+(float(int(data[j][i]))-mean[i])**2
        sigma=sigma/m
        std[i]=sigma**0.5
    for i in range(m):
        for j in range(attr):
            data[i][j]=(float(int(data[i][j]))-mean[j])/std[j]      
def hypo(data,theta,m,attr):
    ans=float(theta[0])
    for i in range(attr-1):
        ans=ans+float(data[i])*theta[i+1]
    return ans
def updateTheta(data,theta,m,attr):
    alpha=0.001
    for i in range(attr):
        sigma=0
        for j in range(m):
            if i==0:
                sigma=sigma+hypo(data[j],theta,m,attr)-float(data[j][attr])
            else:
                sigma=sigma+(hypo(data[j],theta,m,attr)-float(data[j][attr]))*float(data[j][i-1])
        theta[i]=theta[i]-(alpha*sigma)/m       
def costFunction(data,theta,m,attr):
    sigma=0.0
    for i in range(m):
        sigma=sigma+(hypo(data[i],theta,m,attr)-float(data[i][attr]))**2
    cost=sigma/(2*m)
    return cost
def minCost(data,theta,m,attr):
    lastCost=costFunction(data,theta,m,attr)
    updateTheta(data,theta,m,attr)
    newCost=costFunction(data,theta,m,attr)
    while lastCost>newCost:
        lastCost=costFunction(data,theta,m,attr)
        updateTheta(data,theta,m,attr)
        newCost=costFunction(data,theta,m,attr)
def main():
    print "calculating..."
    filename='house.csv'
    f = open(filename, 'rb') # opens the csv file
    data=[]
    try:
        reader = csv.reader(f)  # creates the reader object
        for row in reader:   # iterates the rows of the file in orders
            data.append(row)
    finally:
        f.close()
    theta=[]
    m=len(data)
    attr=len(data[0])-1
    normalise(data,m,attr)
    for i in range(attr+1):
        theta.append(1)
    minCost(data,theta,m,attr)
    newdata=[]
    root = Tk()
    ex = Example(root,theta,m,attr)
    root.geometry("450x350+300+300")
    root.mainloop()  
if __name__ == '__main__':
    main()  