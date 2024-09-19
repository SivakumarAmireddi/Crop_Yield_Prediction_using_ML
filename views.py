from django.shortcuts import render
import mysql.connector as sql
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

#farmer
un=''
c=''
fem=''
fpwd=''
#investor
usn=''
em=''
pas=''
ph=''
#farmer login
fem=''
fpas=''

#investor
iem=''
ipas=''


def index(request):
    return render(request,'index.html')
def farmer(request):
    global un,c,fem,fpwd
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", passwd="Datapro", database="datapro")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():

            if key == 'fullname':
                un = value
            if key == 'country':
                c = value
            if key == 'email':
                fem = value
            if key == 'password':
                fpwd = value
        c = "insert into farmer ( username,country,email,pasword ) values('{}','{}','{}','{}')".format(un,c,fem,fpwd)
        cursor.execute(c)
        m.commit()
    return render(request,'farmer.html')
def investor(request):
    global usn,em,pas,ph
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", passwd="Datapro", database="datapro")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():

            if key == 'fullname':
                usn = value
            if key == 'email':
                em = value
            if key == 'password':
                pas = value
            if key == 'phone':
                ph = value
        c = "insert into investors ( username,email,pasword,mobile ) values('{}','{}','{}','{}')".format(usn,em,pas,ph)
        cursor.execute(c)
        m.commit()

    return render(request,'investor.html')
def flogin(request):
    global fem,fpas
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", passwd="Datapro", database="datapro")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "username":
                fem = value
            if key == "password":
                fpas = value
        c = "select * from farmer where email='{}' and pasword='{}'".format(fem,fpas)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'fmain.html')

    return render(request,'flogin.html')
def ilogin(request):
    global iem,ipas
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", passwd="Datapro", database="datapro")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "username":
                iem = value
            if key == "password":
                ipas = value
        c = "select * from investors where email='{}' and pasword='{}'".format(iem,ipas)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'imain.html')
    return render(request,'ilogin.html')
def fmain(request):
    return render(request,'fmain.html')

def imain(request):
    return render(request,'imain.html')
def fresult(request):
    df=pd.read_csv("c:/Users/USER/Desktop/Projects/Crop_yield_prediction/yield_df.csv")
    df.drop("Unnamed: 0", axis=1,inplace=True)
    c = df.Area.astype('category')
    df['Area'] = c.cat.codes
    c = df.Item.astype('category')
    df['Item'] = c.cat.codes
    X=df[['Area','average_rain_fall_mm_per_year','pesticides_tonnes','avg_temp']]
    y=df[['Item']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dtr=RandomForestRegressor(random_state=42)
    dtr.fit(X_train, y_train)
    var1=float(request.GET['a'])
    var2 = float(request.GET['ar'])
    var3 = float(request.GET['pt'])
    var4 = float(request.GET['at'])
    pred=dtr.predict(np.array([var1,var2,var3,var4]).reshape(1,-1))
    pred=round(pred[0])
    cp="crop recommendation for you is :" +str(pred)
    return render(request,"fmain.html",{"result":cp})
def iresult(request):
    df=pd.read_csv("c:/Users/USER/Desktop/Projects/Crop_yield_prediction/yield_df.csv")
    df.drop("Unnamed: 0", axis=1,inplace=True)
    c = df.Area.astype('category')
    df['Area'] = c.cat.codes
    c = df.Item.astype('category')
    df['Item'] = c.cat.codes
    X=df[['Area','Item','average_rain_fall_mm_per_year','pesticides_tonnes','avg_temp']]
    y=df[['hg/ha_yield']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dtr=RandomForestRegressor(random_state=42)
    dtr.fit(X_train, y_train)
    var1=float(request.GET['ae'])
    var2=float(request.GET['I'])
    var3 = float(request.GET['ar'])
    var4 = float(request.GET['pt'])
    var5 = float(request.GET['at'])
    pred=dtr.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    pred=round(pred[0])
    cp="Yield recommendation for you is :" +str(pred)
    return render(request,"imain.html",{"result":cp})