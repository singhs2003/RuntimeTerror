#Here we are dumping our model so we can call it anytime with a standard key word.
import joblib
joblib.dump(rf,'Patient_Monitoring')
model=joblib.load('Patient_Monitoring')
model

#Here we start our GUI using tkinter
from tkinter import *
import customtkinter
screen=Tk()
screen.geometry("650x600")
screen.title("Dummy Software")
img= PhotoImage(file='bg.png',master=screen)
img_label=Label(screen,image=img)

#define the position of the image
img_label.place(x=0, y=46)

def show_predict():
    p1=float(e1.get())
    p2=float(e2.get())
    p3=float(e3.get())
    p4=float(e4.get())
    p5=float(e5.get())
    p6=float(e6.get())
    p7=float(e7.get())
    p8=float(e8.get())
    p9=float(e9.get())
    
    
    model=joblib.load('Patient_Monitoring')
    result=model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9]])
    if(p==1):
        
        print("Patient requires immediate attention.Alert message forwared.")
        from twilio.rest import Client
        SID='ACffcfd99dd4f3ce5db5853025ea8f5417'
        Auth_Token='154f133a657fc16dd934fe0ce9c562a7'
        c1=Client(SID,Auth_Token)
        if(p5>80):
            c1.messages.create(body='Ward Boy immediately report at bed no. x. High Blood Pressure!!!',from_='+18058192317',to='+919911589022')
            c1.messages.create(body='Dr. Asthana plz see Patient no. x.High Blood Pressure!!! ',from_='+18058192317',to='+919818490813')
        if(p7<95):
            c1.messages.create(body='Ward Boy immediately report at bed no. x.Decreased Oxygen Saturation!!!',from_='+18058192317',to='+919911589022')
            c1.messages.create(body='Dr. Asthana plz see Patient no. x..Decreased Oxygen Saturation!!! ',from_='+18058192317',to='+919818490813')   
        if(p8<7.35 or p8>7.45):
            c1.messages.create(body='Ward Boy immediately report at bed no. x. PH change. Rush To ICU!!',from_='+18058192317',to='+919911589022')
            c1.messages.create(body='Dr. Asthana plz see Patient no. x.PH change. Rush To ICU!! ',from_='+18058192317',to='+919818490813')
        
        else:
            print("Patient sounds fine.") 

    ans=Label(text="Status Is : ",bg="light blue",fg="black").place(x=230,y=400)
    asn2=Label(text=result,bg="black",fg="white").place(x=230,y=430)
    


heading=Label(text="HeAlgo , A Buddy Next To Your Bed..",bg="sky blue",fg="black",height="2",width="500",font=('Cooper Black',18))
heading.pack()


hr=Label(text="Heart Rate",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
hr.place(x=10,y=80)
pulse=Label(text="Pulse",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
pulse.place(x=10,y=130)
temp=Label(text="Temperature",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
temp.place(x=10,y=180)
sbp=Label(text="Systolic Blood Pressure",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
sbp.place(x=10,y=230)
dbp=Label(text="Diastolic Blood pressure",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
dbp.place(x=10,y=280)
rpr=Label(text="Respiratory Rate",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
rpr.place(x=10,y=330)
Oxy=Label(text="SP O2",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
Oxy.place(x=10,y=380)
ph=Label(text="PH",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
ph.place(x=10,y=430)
pco2=Label(text="PCO2",font=('Times New Roman',15),bg='white',borderwidth=1,relief='solid')
pco2.place(x=10,y=480)


e1=Entry(screen,borderwidth=3,relief='solid')
e1.place(x=235,y=80)
e2=Entry(screen,borderwidth=3,relief='solid')
e2.place(x=235,y=130)
e3=Entry(screen,borderwidth=3,relief='solid')
e3.place(x=235,y=180)
e4=Entry(screen,borderwidth=3,relief='solid')
e4.place(x=235,y=230)
e5=Entry(screen,borderwidth=3,relief='solid')
e5.place(x=235,y=280)
e6=Entry(screen,borderwidth=3,relief='solid')
e6.place(x=235,y=330)
e7=Entry(screen,borderwidth=3,relief='solid')
e7.place(x=235,y=380)
e8=Entry(screen,borderwidth=3,relief='solid')
e8.place(x=235,y=430)
e9=Entry(screen,borderwidth=3,relief='solid')
e9.place(x=235,y=480)


x=Button(screen,text="Predict Now..",command=show_predict,font=('Cooper Black',15),bg='white',fg='black',cursor='hand2',borderwidth=3,relief='solid').place(x=150,y=540)

screen.mainloop()

