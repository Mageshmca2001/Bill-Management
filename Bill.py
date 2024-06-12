from tkinter import *
from tkinter import messagebox
import os

      
def login():
     user=username.get()
     code=password.get()

     if user=="Magesh" and code=="1234":
         root=Toplevel(screen)
         root.title("Bill Managemrnt")
         root.geometry("1000x500+150+80")
         root.configure(bg="#d7dae2")
         root.resizable(False,False)

         #copy and paste your code here
        
         def Reset():
    
             entry_dosa.delete(0,END)
             entry_cookies.delete(0,END)
             entry_Tea.delete(0,END)
             entry_coffee.delete(0,END)
             entry_freshjuice.delete(0,END)
             entry_juice.delete(0,END)
             entry_pancakes.delete(0,END)
             entry_icecream.delete(0,END)

         def Total():
              try:a1=int(dosa.get())
              except: a1=0

              try:a2=int(cookies.get())
              except: a2=0

              try:a3=int(Tea.get())
              except: a3=0

              try:a4=int(coffee.get())
              except: a4=0

              try:a5=int(freshjuice.get())
              except: a5=0

              try:a6=int(juice.get())
              except: a6=0

              try:a7=int(pancakes.get())
              except: a7=0

              try:a8=int(icecream.get())
              except: a8=0

              #define cost of item per quantity
              c1=60*a1
              c2=30*a2
              c3=20*a3
              c4=40*a4
              c5=50*a5
              c6=25*a6
              c7=100*a7
              c8=200*a8


              lbl_Total=Label(f2,font=('Lucida calligraphy',20,'italic'),text="Total",width=16,fg="lightpink",bg="black")
              lbl_Total.place(x=0,y=50)


              entry_total=Entry(f2,font=('Lucida calligraphy',20,'bold'),textvariable=Total_bill,bd=8,width=10,bg="lightgreen")
              entry_total.place(x=40,y=100)

              Totalcost=c1+c2+c3+c4+c5+c6+c7+c8
              string_bill="Rs.",str('%.2f' %Totalcost)
              Total_bill.set(string_bill)
    


         Label(root,text="Bill Management",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()


         #MENU CARD
         f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
         f.place(x=10,y=118)

         Label(f,text="Menu",font=("gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

         Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="Cookies......Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="Tea......Rs.20/plate",fg="black",bg="lightgreen").place(x=10,y=140)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="Coffee......Rs.40/plate",fg="black",bg="lightgreen").place(x=10,y=170)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="FreshJuice......Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=200)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="Juice......Rs.25/plate",fg="black",bg="lightgreen").place(x=10,y=230)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="pancakes......Rs.100/plate",fg="black",bg="lightgreen").place(x=10,y=260)
         Label(f,font=("Lucida calligraphy",15,"bold"),text="Icecream......Rs.200/plate",fg="black",bg="lightgreen").place(x=10,y=290)



         #BILL
         f2=Frame(root,bg="lightpink",highlightbackground="black",highlightthickness=1,width=300,height=370)
         f2.place(x=690,y=118)

         Bill=Label(f2,text="Bill",font=('Lucida calligraphy',20),bg="lightpink")
         Bill.place(x=120,y=10)


         #ENTRY WORK
         f1=Frame(root,bd=6,height=370,width=300,relief=RAISED)
         f1.pack()

         dosa=StringVar()
         cookies=StringVar()
         Tea=StringVar()
         coffee=StringVar()
         freshJuice=StringVar()
         juice=StringVar()
         pancakes=StringVar()
         icecream=StringVar()
         Total_bill=StringVar()

         #Label
         lbl_dosa=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Dosa",width=12,fg="blue4")
         lbl_cookies=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Cookies",width=12,fg="blue4")
         lbl_tea=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Tea",width=12,fg="blue4")
         lbl_coffee=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Coffee",width=12,fg="blue4")
         lbl_freshJuice=Label(f1,font=("Lucida calligraphy",15,"italic"),text="FreshJuice",width=12,fg="blue4")
         lbl_juice=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Juice",width=12,fg="blue4")
         lbl_pancakes=Label(f1,font=("Lucida calligraphy",15,"italic"),text="pancakes",width=12,fg="blue4")
         lbl_icecream=Label(f1,font=("Lucida calligraphy",15,"italic"),text="Icecream",width=12,fg="blue4")
         lbl_dosa.grid(row=1,column=0)
         lbl_cookies.grid(row=2,column=0)
         lbl_tea.grid(row=3,column=0)
         lbl_coffee.grid(row=4,column=0)
         lbl_freshJuice.grid(row=5,column=0)
         lbl_juice.grid(row=6,column=0)
         lbl_pancakes.grid(row=7,column=0)
         lbl_icecream.grid(row=8,column=0)

         #Entry
         entry_dosa=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=dosa,bd=6,width=8,bg="lightblue")
         entry_cookies=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=cookies,bd=6,width=8,bg="lightblue")
         entry_Tea=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=Tea,bd=6,width=8,bg="lightblue")
         entry_coffee=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=coffee,bd=6,width=8,bg="lightblue")
         entry_freshjuice=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=freshJuice,bd=6,width=8,bg="lightblue")
         entry_juice=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=juice,bd=6,width=8,bg="lightblue")
         entry_pancakes=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=pancakes,bd=6,width=8,bg="lightblue")
         entry_icecream=Entry(f1,font=("Lucica calligraphy",15,"italic"),textvariable=icecream,bd=6,width=8,bg="lightblue")

         entry_dosa.grid(row=1,column=1)
         entry_cookies.grid(row=2,column=1)
         entry_Tea.grid(row=3,column=1)
         entry_coffee.grid(row=4,column=1)
         entry_freshjuice.grid(row=5,column=1)
         entry_juice.grid(row=6,column=1)
         entry_pancakes.grid(row=7,column=1)
         entry_icecream.grid(row=8,column=1)






         #buttons
         btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("Lucica calligraphy",14,"italic"),width=10,text="Reset",command=Reset)
         btn_reset.grid(row=9,column=0)


         btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("Lucica calligraphy",14,"italic"),width=10,text="Total",command=Total)
         btn_total.grid(row=9,column=1)









          #end of code
         

      #all alerts ,when someone try to enter wrong username and password

         

     elif user=="" and code=="":
          messagebox.showerror("Invalid","Please enter username and password")

     elif user=="":
          messagebox.showerror("Invalid","username is required")

     elif code=="":
          messagebox.showerror("Invalid","The password field is required")

     elif user!="kamal" and code!="1234":
          messagebox.showerror("Invalid","Invalid username and password")

     elif user!="kamal":
          messagebox.showerror("Invalid","please enter a valid username")

     elif code!="1234":
          messagebox.showerror("Invalid","please enter a valid password")
             

         

        
     
def main_screen():


     global screen
     global username
     global password
        
     screen=Tk()
     screen.geometry("1280x720+150+80")
     screen.configure(bg="#d7dae2")

     

          
     lblTitle=Label(text="Login System",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
     lblTitle.pack(pady=50)


     bordercolor=Frame(screen,bg="black",width=800,height=400)
     bordercolor.pack()


     mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
     mainframe.pack(padx=20,pady=20)


     Label(mainframe,text="username",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=50)
     Label(mainframe,text="password",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=150)
       


     username=StringVar()
     password=StringVar()

     entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("aril",30))
     entry_username.place(x=400,y=50)
     entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("aril",30),show="*")
     entry_password.place(x=400,y=150)

     def reset():
         entry_username.delete(0,END)
         entry_password.delete(0,END)

     Button(mainframe,text="Login",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=login).place(x=100,y=250)
     Button(mainframe,text="Reset",height="2",width=23,bg="#1089ff",fg="white",bd=0,command=reset).place(x=300,y=250)
     Button(mainframe,text="Exit",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)

                          
   

    



     screen.mainloop()
     

main_screen()
