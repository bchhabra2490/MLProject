import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,preprocessing,linear_model
print("wokinr")
def get_data(name):
    data=pd.read_csv(name)
    #for singlefeet,singleprice in list(zip(data['square_feet'],x.append([float(singlefeet)]),y.append(float(singleprice))))
    room=[]
    typ=[]
    locality=[]
    interior=[]
    lawn=[]
    swimming=[]
    view=[]
    bathrooms=[]
    parking=[]
    price=[]
    for r,t,l,i,law,s,v,b,park,pri in list(zip(data['room'],data['type'],data['locality'],data['interior'],data['lawn'],data['swimming'],data['view'],data['bathrooms'],data['parking'],data['price'])):
        room.append(float(r))
        typ.append(int(t))
        locality.append(float(l))
        interior.append(int(i))
        lawn.append(int(law))
        swimming.append(int(s))
        view.append(float(v))
        bathrooms.append(int(b))
        parking.append(int(park))
        price.append(float(park))
    return room,typ,locality,interior,lawn,swimming,view,bathrooms,parking,price

def normalise(x):
    print("normalising")
    #del(list)
    meanr=[]
    stdr=[]
    xr=x
    num=x.shape[0]
    for i in range(num):
        m=mean(x[:,i])
        s=std(x[:,i])
        meanr.appned(m)
        stdr.append(s)
        xr[:,i]=(xr[:,i]-m)/s
    return xr,meanr,stdr

   
room=[]
typ=[]
loaclity=[]
interior=[]
lawn=[]
swimming=[]
view=[]
bathrooms=[]
parking=[]
price=[]
mean=[]
standard_deviation=[]
attributes=9
att=np.zeros( (2,9) )
final=np.zeros( (2,9) )
room,typ,locality,interior,lawn,swimming,view,bathrooms,parking,price=get_data('house.csv')
#att = [[[] for i in range(attributes)] for i in range(2)]
j=0
for i in range(2):
	j=0
	att[i][j]=(room[i])
	j=j+1
	att[i][j]=(locality[i])
	j=j+1
	att[i][j]=(interior[i])
	j=j+1
	att[i][j]=(typ[i])
	j=j+1
	att[i][j]=(lawn[i])
	j=j+1
	att[i][j]=(swimming[i])
	j=j+1
	att[i][j]=(view[i])
	j=j+1
	att[i][j]=(bathrooms[i])
	j=j+1
	att[i][j]=(parking[i])
#qw=np.array(att)
#print(att)
final,mean,standard_deviation=normalise(att)
print(final)