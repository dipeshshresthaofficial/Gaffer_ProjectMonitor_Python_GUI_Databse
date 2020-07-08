from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import speech_recognition as speech
import os
import sqlite3
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

db=sqlite3.connect("latestgafferfinal.db")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS 'TEAM'(T_CODE INTEGER PRIMARY KEY, T_NAME VARCHAR(10), CAP_NAME VARCHAR(20) NOT NULL, USERNAME CHAR(10) NOT NULL UNIQUE,PWD VARCHAR(20) NOT NULL,TINBOX VARCHAR(100))")
cur.execute("CREATE TABLE IF NOT EXISTS 'CLIENT'(C_ID INTEGER PRIMARY KEY, C_NAME VARCHAR(20) NOT NULL, STREET VARCHAR(15), CITY VARCHAR(20) NOT NULL, COUNTRY VARCHAR(20), EMAIL VARCHAR(30) UNIQUE)")
cur.execute("CREATE TABLE IF NOT EXISTS 'ROLE'(R_ID INTEGER PRIMARY KEY, R_NAME CHAR(15) NOT NULL, SALARY INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS 'CLIENT_MOBILE'(MOBILE_ID INTEGER PRIMARY KEY AUTOINCREMENT, MOBILE BIGINT,CUSTOMER_ID INTEGER, CONSTRAINT FK1 FOREIGN KEY (CUSTOMER_ID) REFERENCES CLIENT (C_ID) ON DELETE CASCADE  ON UPDATE CASCADE)")
cur.execute("CREATE TABLE IF NOT EXISTS 'PROJECT'(P_CODE INTEGER PRIMARY KEY,P_NAME VARCHAR(15) NOT NULL, BUDGET INTEGER, STATUS VARCHAR(8), START_DATE DATE NOT NULL, DUE_DATE DATE NOT NULL, CUST_ID INTEGER, CONSTRAINT FK2 FOREIGN KEY (CUST_ID) REFERENCES CLIENT (C_ID) ON DELETE CASCADE ON UPDATE CASCADE)")
cur.execute("CREATE TABLE IF NOT EXISTS 'MEMBERS'(M_ID CHAR(10) PRIMARY KEY,AGE INTEGER,M_NAME VARCHAR(20) NOT NULL,CELL CHAR(10) UNIQUE, COUNTRY VARCHAR(15),START_DATE DATE, TEAM_CODE INTEGER,ROLE_ID INTEGER,MINBOX VARCHAR(100), CONSTRAINT FK3 FOREIGN KEY (TEAM_CODE) REFERENCES TEAM (T_CODE) ON DELETE CASCADE ON UPDATE CASCADE,CONSTRAINT FK4 FOREIGN KEY(ROLE_ID) REFERENCES ROLE(R_ID) ON DELETE CASCADE ON UPDATE CASCADE)")
cur.execute("CREATE TABLE IF NOT EXISTS 'WORKON' (PROGRESSBAR INTEGER,MEM_ID CHAR(10), PROJ_CODE INTEGER,CONSTRAINT FK5 FOREIGN KEY (MEM_ID) REFERENCES MEMBERS (M_ID) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT FK6 FOREIGN KEY (PROJ_CODE) REFERENCES PROJECT (P_CODE) ON DELETE CASCADE ON UPDATE CASCADE)")

db.commit()

def Database():
    db=sqlite3.connect('latestgafferfinal.db')
    cur=db.cursor()

root=Tk()

root.geometry('400x500')
#root.config(bg='purple')
root.title('Gaffer- The Project Monitor')


def functionOne(frame):
    frame.tkraise()
    
"""Frame initialization"""

loginPage=Frame(root)
captainDashboard=Frame(root)
allProjectWin=Frame(root)
projectDetailWin=Frame(root)
allMemberWin=Frame(root)
memberDetailWin=Frame(root)
allClientWin=Frame(root)
clientDetailWin=Frame(root)

memberDashboard=Frame(root)
memberHome=Frame(root)
memberProjectProgress=Frame(root)



for frame in (loginPage,captainDashboard,memberDashboard,allProjectWin,projectDetailWin,allMemberWin,memberDetailWin,allClientWin,clientDetailWin,memberProjectProgress):
    frame.grid(row=0,column=0,sticky='news')





    

"""def insertTeam():
    print("team inserted")
    #global TEAM_CODE,TEAM_NAME,CAPTAIN_NAME,CAPTAIN_USERNAME,CAPTAIN_PWD
    #cur.execute("INSERT INTO 'TEAM'(T_CODE,T_NAME,CAP_NAME,USERNAME,PWD) VALUES(?,?,?,?,?)",(int(TEAM_CODE.get()),str(TEAM_NAME.get()),str(CAPTAIN_NAME.get()),str(CAPTAIN_USERNAME.get()),str(CAPTAIN_PWD.get())))
    #db.commit()
    """



"""""""""""""""""""""""""""""""""""""""WINDOW FOR INSERTING team and captain details in TEAM table"""""""""""""""""""""""""""""""""""""""""""""

abc=Frame(loginPage,bg='powder blue',bd=10,width=250,height=100,padx=250,pady=50,relief=RIDGE)

def signUp():

    root8=Toplevel()
    root8.geometry('500x500')
    root8.title('Gaffer- The Project Monitor')
    db.commit()
    
    #Initializing variables---
    
    TEAM_CODE=IntVar()
    TEAM_NAME=StringVar()
    CAPTAIN_NAME=StringVar()
    CAPTAIN_USERNAME=StringVar()
    
    CAPTAIN_PWD=StringVar()
    
    """root9.title('Sign UP')

    root8=Frame(root9)
    root8.grid(row=2,column=2,sticky=E,padx=80,pady=80)"""
    
    """Adding Captain details"""
    new_captain_label=ttk.Label(root8,text="Fill The Details Below",font=("Calibri",20))
    new_team_code_label=ttk.Label(root8,text="Team Code",font=("Calibri",12))
    new_team_name_label=ttk.Label(root8,text="Team Name",font=("Calibri",12))
    new_captain_name_label=ttk.Label(root8,text="Captain Name",font=("Calibri",12))
    new_captain_username_label=ttk.Label(root8,text="Username",font=("Calibri",12))
    new_captain_password_label=ttk.Label(root8,text="Password",font=("Calibri",12))
    
    new_team_code_entry=ttk.Entry(root8,textvariable=TEAM_CODE,font=("Calibri",12))
    new_team_name_entry=ttk.Entry(root8,textvariable=TEAM_NAME,font=("Calibri",12))
    new_captain_name_entry=ttk.Entry(root8,textvariable=CAPTAIN_NAME,font=("Calibri",12))
    new_captain_username_entry=ttk.Entry(root8,textvariable=CAPTAIN_USERNAME,font=("Calibri",12))
    new_captain_password_entry=ttk.Entry(root8,textvariable=CAPTAIN_PWD,show="*",font=("Calibri",12))

    

    new_captain_label.grid(row=1,column=2,columnspan=3,pady=20,padx=90)
    
    new_team_code_label.grid(row=3,column=3,sticky=W,pady=5,padx=5)
    new_team_name_label.grid(row=5,column=3,sticky=W,pady=5,padx=5)
    new_captain_name_label.grid(row=7,column=3,sticky=W,pady=5,padx=5)
    new_captain_username_label.grid(row=9,column=3,sticky=W,pady=5,padx=5)
    new_captain_password_label.grid(row=11,column=3,sticky=W,pady=5,padx=5)
   
    new_team_code_entry.grid(row=3,column=4,pady=5,sticky=E)
    new_team_name_entry.grid(row=5,column=4,pady=5,sticky=E)
    new_captain_name_entry.grid(row=7,column=4,pady=5,sticky=E)
    new_captain_username_entry.grid(row=9,column=4,pady=5,sticky=E)
    new_captain_password_entry.grid(row=11,column=4,pady=5,sticky=E)

   
    def insertTeam():
    
        TEMP1=TEAM_CODE.get()
        TEMP2=TEAM_NAME.get()
        TEMP3=CAPTAIN_NAME.get()
        TEMP4=CAPTAIN_USERNAME.get()
        TEMP5=CAPTAIN_PWD.get()
        
        #print(int(textin.get()))
        #print(str(textinn.get()))
        db=sqlite3.connect('latestgafferfinal.db')
        cur=db.cursor()
        
        cur.execute("INSERT INTO 'TEAM' (T_CODE,T_NAME,CAP_NAME,USERNAME,PWD) VALUES('%d','%s','%s','%s','%s')"%(TEMP1,TEMP2,TEMP3,TEMP4,TEMP5))

        db.commit()
        cur.close()
    
    cap_submit_btn=ttk.Button(root8,text='SUBMIIT',command=insertTeam)
    cap_submit_btn.grid(row=13,column=4,sticky=W,pady=20)
    
    cap_done_btn=ttk.Button(root8,text='DONE',command=root8.destroy)
    cap_done_btn.grid(row=13,column=3,sticky=W,pady=20)


    
"""""""""""""""""""""""""""""""""""""""WINDOW FOR INSERTING client into CLIENT table"""""""""""""""""""""""""""""""""""""""""""""          
abc=Frame(loginPage,bg='powder blue',bd=10,width=250,height=100,padx=250,pady=50,relief=RIDGE)

def addClientWin():
    root6=Toplevel()
    root6.geometry('500x500')
    root6.title('Gaffer- The Project Monitor')
    db.commit()

    """root6=Frame(root7)
    root6.grid(row=2,column=2,sticky=E,padx=80,pady=80)"""

     #Variables Assignment---

    CLIENT_ID=IntVar()
    CLIENT_NAME=StringVar()
    CLIENT_STREET=StringVar()
    CLIENT_CITY=StringVar()
    CLIENT_COUNTRY=StringVar()
    CLIENT_EMAIL=StringVar()
    CLIENT_1MOBILE=StringVar()
    CLIENT_2MOBILE=StringVar()
    
    
    #Adding Client details---
    
    new_client_label= ttk.Label(root6,text="Fill The Client Details Below",font=("Calibri",20))
    new_client_id_label= ttk.Label(root6,text="Client Id",font=("Calibri",12))
    new_client_name_label= ttk.Label(root6,text="Client Name",font=("Calibri",12))
    new_client_1mobile_label= ttk.Label(root6,text="Mobile No",font=("Calibri",12))
    new_client_2mobile_label= ttk.Label(root6,text="Alternate Mobile No",font=("Calibri",12))
    new_client_email_label= ttk.Label(root6,text="Email",font=("Calibri",12))
    new_client_street_label= ttk.Label(root6,text="Street",font=("Calibri",12))
    new_client_city_label= ttk.Label(root6,text="City",font=("Calibri",12))
    new_client_country_label= ttk.Label(root6,text="Country",font=("Calibri",12))
    
    new_client_id_entry= ttk.Entry(root6,textvariable=CLIENT_ID,font=("Calibri",12))
    new_client_name_entry= ttk.Entry(root6,textvariable=CLIENT_NAME,font=("Calibri",12))
    new_client_1mobile_entry= ttk.Entry(root6,textvariable=CLIENT_1MOBILE,font=("Calibri",12))
    new_client_2mobile_entry= ttk.Entry(root6,textvariable=CLIENT_2MOBILE,font=("Calibri",12))
    new_client_email_entry= ttk.Entry(root6,textvariable=CLIENT_EMAIL,font=("Calibri",12))
    new_client_street_entry= ttk.Entry(root6,textvariable=CLIENT_STREET,font=("Calibri",12))
    new_client_city_entry= ttk.Entry(root6,textvariable=CLIENT_CITY,font=("Calibri",12))
    new_client_country_entry= ttk.Entry(root6,textvariable=CLIENT_COUNTRY,font=("Calibri",12))

    
    new_client_label.grid(row=1,column=2,columnspan=3,pady=20,padx=90)

    new_client_id_label.grid(row=3,column=3,sticky=W,pady=5,padx=5)
    new_client_name_label.grid(row=5,column=3,sticky=W,pady=5,padx=5)
    new_client_1mobile_label.grid(row=7,column=3,sticky=W,pady=5,padx=5)
    new_client_2mobile_label.grid(row=9,column=3,sticky=W,pady=5,padx=5)
    new_client_email_label.grid(row=11,column=3,sticky=W,pady=5,padx=5)
    new_client_street_label.grid(row=13,column=3,sticky=W,pady=5,padx=5)
    new_client_city_label.grid(row=15,column=3,sticky=W,pady=5,padx=5)
    new_client_country_label.grid(row=17,column=3,sticky=W,pady=5,padx=5)

    new_client_id_entry.grid(row=3,column=4,pady=5,sticky=E)
    new_client_name_entry.grid(row=5,column=4,pady=5,sticky=E)
    new_client_1mobile_entry.grid(row=7,column=4,pady=5,sticky=E)
    new_client_2mobile_entry.grid(row=9,column=4,pady=5,sticky=E)
    new_client_email_entry.grid(row=11,column=4,pady=5,sticky=E)
    new_client_street_entry.grid(row=13,column=4,pady=5,sticky=E)
    new_client_city_entry.grid(row=15,column=4,pady=5,sticky=E)
    new_client_country_entry.grid(row=17,column=4,pady=5,sticky=E)

        
    #inserting into table TEAM---
    def insertClient():
        TEMP1=CLIENT_ID.get()
        TEMP2=CLIENT_NAME.get()
        TEMP3=CLIENT_STREET.get()
        TEMP4=CLIENT_CITY.get()
        TEMP5=CLIENT_COUNTRY.get()
        TEMP6=CLIENT_EMAIL.get()
        TEMP7=CLIENT_1MOBILE.get()
        TEMP8=CLIENT_2MOBILE.get()
        
        #print(int(textin.get()))
        #print(str(textinn.get()))
        db=sqlite3.connect('latestgafferfinal.db')
        cur=db.cursor()
        
        cur.execute("INSERT INTO 'CLIENT' (C_ID,C_NAME,STREET,CITY,COUNTRY,EMAIL) VALUES('%d','%s','%s','%s','%s','%s')"%(TEMP1,TEMP2,TEMP3,TEMP4,TEMP5,TEMP6))
        
        db.commit()
        if(TEMP7!=0):
        
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP7,TEMP1))
        if(int(TEMP8)!=0):
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP8,TEMP1))
            
        db.commit()
        cur.close()
        
    client_submit_btn=ttk.Button(root6,text='SUBMIIT',command=insertClient)
    client_submit_btn.grid(row=19,column=4,sticky=W)
    
    client_done_btn=ttk.Button(root6,text='DONE',command=root6.destroy)
    client_done_btn.grid(row=19,column=3,sticky=W,pady=20)


"""""""""""""""""""""""""""""""""""""""WINDOW FOR INSERTING member into MEMBER table"""""""""""""""""""""""""""""""""""""""""""""
abc=Frame(loginPage,bg='powder blue',bd=10,width=250,height=100,padx=250,pady=50,relief=RIDGE)

def addMemberWin():
    root4=Toplevel()
    root4.geometry('500x500')
    root4.title('Gaffer- The Project Monitor')
    """root4=Frame(root5)
    root4.grid(row=2,column=2,sticky=E,padx=100,pady=80)"""
    db.commit()
    
    #Variables Assignment---
    MEMBER_ID= StringVar()
    MEMBER_NAME= StringVar()
    MEMBER_COUNTRY= StringVar()
    MEMBER_MOBILE= StringVar()
    MEMBER_SDATE= StringVar()
    MEMBER_TCODE= IntVar()
    MEMBER_RID= IntVar()
    
    """Adding Member details"""
    new_mem_label=ttk.Label(root4,text="Fill The Member Details Below",font=("Calibri",20))
    new_mem_id_label=ttk.Label(root4,text="Member Id",font=("Calibri",12))
    new_mem_name_label=ttk.Label(root4,text="Member Name",font=("Calibri",12))
    new_mem_mobile_label=ttk.Label(root4,text="Cell No",font=("Calibri",12))
    new_mem_country_label=ttk.Label(root4,text="Country",font=("Calibri",12))
    new_mem_sdate_label=ttk.Label(root4,text="Starting Date",font=("Calibri",12))
    new_mem_tcode_label=ttk.Label(root4,text="Team Code",font=("Calibri",12))
    new_mem_rid_label=ttk.Label(root4,text="Role Id",font=("Calibri",12))
    
    new_mem_id_entry=ttk.Entry(root4,textvariable=MEMBER_ID,font=("Calibri",12))
    new_mem_name_entry=ttk.Entry(root4,textvariable=MEMBER_NAME,font=("Calibri",12))
    new_mem_mobile_entry=ttk.Entry(root4,textvariable=MEMBER_MOBILE,font=("Calibri",12))
    new_mem_country_entry=ttk.Entry(root4,textvariable=MEMBER_COUNTRY,font=("Calibri",12))
    new_mem_sdate_entry=ttk.Entry(root4,textvariable=MEMBER_SDATE,font=("Calibri",12))
    new_mem_tcode_entry=ttk.Entry(root4,textvariable=MEMBER_TCODE,font=("Calibri",12))
    new_mem_rid_entry=ttk.Entry(root4,textvariable=MEMBER_RID,font=("Calibri",12))
    

    new_mem_label.grid(row=1,column=2,columnspan=3,pady=20,padx=50)

    new_mem_id_label.grid(row=3,column=3,sticky=W,pady=5,padx=5)
    new_mem_name_label.grid(row=5,column=3,sticky=W,pady=5,padx=5)
    new_mem_mobile_label.grid(row=7,column=3,sticky=W,pady=5,padx=5)
    new_mem_country_label.grid(row=9,column=3,sticky=W,pady=5,padx=5)
    new_mem_sdate_label.grid(row=11,column=3,sticky=W,pady=5,padx=5)
    new_mem_tcode_label.grid(row=13,column=3,sticky=W,pady=5,padx=5)
    new_mem_rid_label.grid(row=15,column=3,sticky=W,pady=5,padx=5)
    
    new_mem_id_entry.grid(row=3,column=4,pady=5,sticky=E)
    new_mem_name_entry.grid(row=5,column=4,pady=5,sticky=E)
    new_mem_mobile_entry.grid(row=7,column=4,pady=5,sticky=E)
    new_mem_country_entry.grid(row=9,column=4,pady=5,sticky=E)
    new_mem_sdate_entry.grid(row=11,column=4,pady=5,sticky=E)
    new_mem_tcode_entry.grid(row=13,column=4,sticky=E,pady=5)
    new_mem_rid_entry.grid(row=15,column=4,sticky=E,pady=5)
    
    #inserting into table TEAM---
    def insertMember():
        TEMP1=MEMBER_ID.get()
        TEMP2=MEMBER_NAME.get()
        TEMP3=MEMBER_COUNTRY.get()
        TEMP4=MEMBER_MOBILE.get()
        TEMP5=MEMBER_SDATE.get()
        TEMP6=MEMBER_TCODE.get()
        TEMP7=MEMBER_RID.get()    
    
        #print(int(textin.get()))
        #print(str(textinn.get()))
        db=sqlite3.connect('latestgafferfinal.db')
        cur=db.cursor()
        
        cur.execute("INSERT INTO 'MEMBERS' (M_ID,M_NAME,CELL,COUNTRY,START_DATE,TEAM_CODE,ROLE_ID) VALUES('%s','%s','%s','%s','%s','%d','%d')"%(TEMP1,TEMP2,TEMP4,TEMP3,TEMP5,TEMP6,TEMP7))
        
        db.commit()
        """if(TEMP7!=0):
        
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP7,TEMP1))
        if(int(TEMP8)!=0):
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP8,TEMP1))
            """
        cur.close()
        
    member_submit_btn=ttk.Button(root4,text='SUBMIIT',command=insertMember)
    member_submit_btn.grid(row=17,column=4,sticky=E,pady=20)
    
    member_done_btn=ttk.Button(root4,text='DONE',command=root4.destroy)
    member_done_btn.grid(row=17,column=3,sticky=W,pady=20)
    

"""""""""""""""""""""""""""""""""""""""WINDOW FOR INSERTING Project into PROJECT table"""""""""""""""""""""""""""""""""""""""""""""    
abc=Frame(loginPage,bg='powder blue',bd=10,width=250,height=100,padx=250,pady=50,relief=RIDGE)

def addProjectWin():
    root2=Toplevel()
    root2.geometry('500x500')
    root2.title('Gaffer- The Project Monitor')
    
    db.commit()
    """root2=Frame(root3)
    root2.grid(row=2,column=2,sticky=E,padx=100,pady=80)"""
    
    #Variables Assignment---
    PROJECT_CODE= IntVar()
    PROJECT_NAME= StringVar()
    PROJECT_BUDGET= IntVar()
    PROJECT_STATUS= StringVar()
    PROJECT_SDATE= StringVar()
    PROJECT_DDATE= StringVar()
    PROJECT_CLIENTID= IntVar()
    PROJECT_MEMID= StringVar()
    
    """Adding Project details"""
    new_prj_label=ttk.Label(root2,text="Fill The Project Details Below",font=("Calibri",20))
    new_prj_code_label=ttk.Label(root2,text="Project Code",font=("Calibri",12))
    new_prj_name_label=ttk.Label(root2,text="Project Name",font=("Calibri",12))
    new_prj_budget_label=ttk.Label(root2,text="Project Budget",font=("Calibri",12))
    new_prj_status_label=ttk.Label(root2,text="Project Status",font=("Calibri",12))
    new_prj_sdate_label=ttk.Label(root2,text="Starting Date",font=("Calibri",12))
    new_prj_ddate_label=ttk.Label(root2,text="Due Date",font=("Calibri",12))
    new_prj_client_id_label=ttk.Label(root2,text="Client Id",font=("Calibri",12))
    new_prj_assigned_member_id_label=ttk.Label(root2,text="Member Id",font=("Calibri",12))
    
    new_prj_code_entry=ttk.Entry(root2,textvariable=PROJECT_CODE,font=("Calibri",12))
    new_prj_name_entry=ttk.Entry(root2,textvariable=PROJECT_NAME,font=("Calibri",12))
    new_prj_budget_entry=ttk.Entry(root2,textvariable=PROJECT_BUDGET,font=("Calibri",12))
    new_prj_status_entry=ttk.Entry(root2,textvariable=PROJECT_STATUS,font=("Calibri",12))
    new_prj_sdate_entry=ttk.Entry(root2,textvariable=PROJECT_SDATE,font=("Calibri",12))
    new_prj_ddate_entry=ttk.Entry(root2,textvariable=PROJECT_DDATE,font=("Calibri",12))
    new_prj_client_id_entry=ttk.Entry(root2,textvariable=PROJECT_CLIENTID,font=("Calibri",12))
    new_prj_assigned_member_id_entry=ttk.Entry(root2,textvariable=PROJECT_MEMID,font=("Calibri",12))
    
    new_prj_label.grid(row=1,column=2,columnspan=3,pady=20,padx=50)

    new_prj_code_label.grid(row=3,column=2,sticky=W,pady=5,padx=5)
    new_prj_name_label.grid(row=5,column=2,sticky=W,pady=5,padx=5)
    new_prj_budget_label.grid(row=7,column=2,sticky=W,pady=5,padx=5)
    new_prj_status_label.grid(row=9,column=2,sticky=W,pady=5,padx=5)
    new_prj_sdate_label.grid(row=11,column=2,sticky=W,pady=5,padx=5)
    new_prj_ddate_label.grid(row=13,column=2,sticky=W,pady=5,padx=5)
    new_prj_client_id_label.grid(row=15,column=2,sticky=W,pady=5,padx=5)
    new_prj_assigned_member_id_label.grid(row=17,column=2,sticky=W,pady=5,padx=5)
    
    new_prj_code_entry.grid(row=3,column=3,pady=5,sticky=E)
    new_prj_name_entry.grid(row=5,column=3,pady=5,sticky=E)
    new_prj_budget_entry.grid(row=7,column=3,pady=5,sticky=E)
    new_prj_status_entry.grid(row=9,column=3,pady=5,sticky=E)
    new_prj_sdate_entry.grid(row=11,column=3,pady=5,sticky=E)
    new_prj_ddate_entry.grid(row=13,column=3,pady=5,sticky=E)
    new_prj_client_id_entry.grid(row=15,column=3,pady=5,sticky=E)
    new_prj_assigned_member_id_entry.grid(row=17,column=3,pady=5,sticky=E)
    
    def insertPrj():
        
        TEMP1=PROJECT_CODE.get()
        TEMP2=PROJECT_NAME.get()
        TEMP3=PROJECT_BUDGET.get()
        TEMP4=PROJECT_STATUS.get()
        TEMP5=PROJECT_SDATE.get()
        TEMP6=PROJECT_DDATE.get()
        TEMP7=PROJECT_CLIENTID.get()    
        TEMP8=PROJECT_MEMID.get()
        
        #print(int(textin.get()))
        #print(str(textinn.get()))
        db=sqlite3.connect('latestgafferfinal.db')
        cur=db.cursor()

        #updating PROJECT TABLE
        cur.execute("INSERT INTO 'PROJECT' (P_CODE,P_NAME,BUDGET,STATUS,START_DATE,DUE_DATE,CUST_ID) VALUES('%d','%s','%d','%s','%s','%s','%d')"%(TEMP1,TEMP2,TEMP3,TEMP4,TEMP5,TEMP6,TEMP7))
        
        db.commit()
        #updating WORKON TABLE
        cur.execute("INSERT INTO 'WORKON'(MEM_ID,PROJ_CODE)VALUES('%s','%d')"%(TEMP8,TEMP1)) #Think about logic to assign the project automatically
        db.commit()
        """if(TEMP7!=0):
        
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP7,TEMP1))
        if(int(TEMP8)!=0):
            cur.execute("INSERT INTO 'CLIENT_MOBILE' (MOBILE,CUSTOMER_ID) VALUES('%s','%s')"%(TEMP8,TEMP1))
            """
        cur.close()
    
    prj_submit_btn=ttk.Button(root2,text='SUBMIIT',command=insertPrj)
    prj_submit_btn.grid(row=19,column=2)
    
    prj_done_btn=ttk.Button(root2,text='DONE',command=root2.destroy)
    prj_done_btn.grid(row=19,column=3,sticky=W,pady=20)

    
"""this function uses GOOGLE API to recognize the spoken words and stores it in a variable"""
def captainIdSpeech():
    recognizing=speech.Recognizer()
    
    with speech.Microphone() as source:
        audio=recognizing.listen(source)
    
    try:
        variable1=recognizing.recognize_google(audio)
        captainIdSpeechSet(variable1) 
    except Exception:
        messagebox.showerror("Error","Couldn't reach you, Please try again")
        
    
"""CaptainIdSpeechSet() function shows the spoken words in ENTRY field of Captain ID"""
def captainIdSpeechSet(text):
    captain_id_entry.delete(0,END) #removes the previously entered value completely(END)
    captain_id_entry.insert(0,text) #setting the value of text(i.e variable1) in the entry field
    return
    
    
"""Creating captain login window"""
#I'm prefixing widgets with "ttk." as it gives better looks

#defining variables
CAP_USERNAME=StringVar()
CAP_PWD=StringVar()

captain_label=ttk.Label(loginPage,text="CAPTAIN WINDOW")
captain_username_label=ttk.Label(loginPage,text="Captain Username: ")
captain_pwd_label=ttk.Label(loginPage,text="Password: ")

captain_username_entry=ttk.Entry(loginPage,textvariable=CAP_USERNAME)
captain_pwd_entry=ttk.Entry(loginPage,show="*",textvariable=CAP_PWD)  #show attribute hides the password content, here with '*'
captain_id_speech_button=ttk.Button(loginPage,text="speak",command=captainIdSpeech)

captain_id_speech_button.grid(row=1,column=2)

captain_label.grid(row=0,column=0,columnspan=2,pady=10)
captain_username_label.grid(row=1,column=0,sticky=W,padx=2)
captain_pwd_label.grid(row=2,column=0,sticky=W,padx=2)
captain_username_entry.grid(row=1,column=1,sticky=W,pady=3)
captain_pwd_entry.grid(row=2,column=1,sticky=W,pady=3)
captain_checkbutton=ttk.Checkbutton(loginPage,text="Keep me logged in")



#to verify
def verifyCapLogin():

    TEMP1=CAP_USERNAME.get()
    TEMP2=CAP_PWD.get()
    list1=[] #This list is to store all the rows fetched from database
    list2=[] #This list is to extract each row separately from list1
    Database()
    cur.execute("SELECT USERNAME,PWD FROM TEAM") #select query to retrives all rows from TEAM table
    row=cur.fetchall() #retrives all rows from TEAM table into row variable
    
    for data in row: 
        list1.append(data)#each row is stored to each index of list1

    for erow in list1: #each row iteration
        list2=erow #EG: 1st index (i.e. 1st row (USERNAME and PWD) of TEAM table) of list1 is stored in list2
        if(TEMP1==list2[0] and TEMP2==list2[1]): #checking if username and password matches or not
            print("Login Successful")
            functionOne(captainDashboard) #calling frame (i.e captain Dashboard) if username and password matches
            break
        
    else:
        messagebox.showerror("ERROR","Please enter correct username or password or Sign Up!")
        print("Login Unsuccessful")

# .place() function is very easy to use and is very very very effective than .grid() function"""
captain_checkbutton.grid(row=3,column=0,sticky=E)
captain_login_button=ttk.Button(loginPage,text="Log in",command=lambda: verifyCapLogin())
captain_login_button.grid(row=4,column=0,pady=10)

captain_signup_button=ttk.Button(loginPage,text="Sign up?",command=signUp)
captain_signup_button.grid(row=4,column=1,pady=10)











#defining variables
MEMBER_MOBILE=StringVar()
MEMBER_ID=StringVar()

    
"""Creating member login window"""
#I'm prefixing widgets with "ttk." as it gives better looks

member_label=ttk.Label(loginPage,text="MEMBER WINDOW")
member_mobile_label=ttk.Label(loginPage,text="Mobile no: ")
member_mobile_entry=ttk.Entry(loginPage,textvariable=MEMBER_MOBILE)
member_id_label=ttk.Label(loginPage,text="Member Id: ")
member_id_entry=ttk.Entry(loginPage,show="*",textvariable=MEMBER_ID)
      #show attribute hides the password content, here with '*'

member_label.grid(row=6,column=0,columnspan=2,pady=10)
member_mobile_label.grid(row=8,column=0,sticky=W,padx=2)
member_mobile_entry.grid(row=8,column=1,sticky=W,pady=3)
member_id_label.grid(row=7,column=0,sticky=W,padx=2)
member_id_entry.grid(row=7,column=1,sticky=W,pady=3)


member_checkbutton=ttk.Checkbutton(loginPage,text="Keep me logged in")
# .place() function is very easy to use and is very very very effective than .grid() function"""


#Adding list box
member_home_listbox=Listbox(memberDashboard,height=10,width=20,selectmode=BROWSE,bg="black",fg="red",font=("Calibri",12))
member_home_listbox.grid(row=5,column=5,padx=70)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Should work on this
def decreaseProgressbar(data):
    Database()
    decrease=int(data)-20
    cur.execute("UPDATE 'WORKON' SET PROGRESSBAR=? WHERE MEM_ID=? AND PROJ_CODE=?",(decrease,MEMBER_ID.get(),temp[0],))
    db.commit()
    
def increaseProgressbar(data):
    Database()
    increase=int(data)+20
    cur.execute("UPDATE 'WORKON' SET PROGRESSBAR=? WHERE MEM_ID=? AND PROJ_CODE=?",(increase,MEMBER_ID.get(),temp[0],))
    db.commit()

def memProgressbar(value):
        
    root13=Tk()
    root13.geometry('300x250')
    root13.title('Gaffer- The Project Monitor')
    
    bar=Progressbar(root13,length=100)
    bar['value']=value
    bar.grid(column=1,row=0,sticky=N+S+E+W)
    
    
    done_btn=ttk.Button(root13,text='Done',command=root13.destroy)
    done_btn.grid(row=1,column=2)
    decrease_btn=ttk.Button(root13,text='Reduce',command=decreaseProgressbar(value)) 
    
    increase_btn=ttk.Button(root13,text='Increase',command=increaseProgressbar(value)) 
    decrease_btn.grid(row=1,column=1)
    increase_btn.grid(row=1,column=3)
    
    root13.mainloop()

MESSAGE_FROM_CAP=StringVar()

def openInbox():

    inboxWin= Toplevel()
    inboxWin.geometry('360x300')
    inboxWin.title('Gaffer- The Project Monitor')

    inbox_msg_from_label=ttk.Label(inboxWin,text="Message From:",font=("Calibri",12))
    inbox_msg_from_label.grid(row=3,column=1,pady=10)

    Database()
    cur.execute("SELECT CAP_NAME FROM TEAM,MEMBERS WHERE T_CODE=TEAM_CODE AND M_ID=?",(MEMBER_ID.get(),))
    rows=cur.fetchall()
    for datas in rows:
        print(datas[0])

    inbox_msg_from_label_entry=ttk.Label(inboxWin,text=datas[0],font=("Calibri",12))
    inbox_msg_from_label_entry.grid(row=3,column=2,pady=10,sticky=W)
    
    Database()
    cur.execute("SELECT MINBOX FROM MEMBERS WHERE M_ID=?",(MEMBER_ID.get(),))
    row=cur.fetchall()
    for data in row:
        print(data[0])

    T = Text(inboxWin, height=14, width=40)
    T.grid(row=5,column=1,columnspan=2,pady=10,padx=20)
    T.insert(END,data[0])


    
def verifiedMember():
    functionOne(memberDashboard)

    Database()
    cur.execute("SELECT M_NAME FROM MEMBERS WHERE M_ID=?",(MEMBER_ID.get(),))
    row=cur.fetchall()
    for data in row:
        print(data[0])
    """Second Page -- Member Dashboard"""
    member_home_label=ttk.Label(memberDashboard,text='Welcome ' + data[0],font=("Calibri",15))
    member_home_back_button=ttk.Button(memberDashboard,text='Back',command=lambda:functionOne(loginPage))
    member_home_inbox_button=ttk.Button(memberDashboard,text='Inbox**',command=openInbox)
    member_home_piechart_button=ttk.Button(memberDashboard,text='Bar Chart',command=lambda:functionOne(memberDashboard)) #not done: first complete all then PIE-CHART

    Database()
    cur.execute("SELECT PROJ_CODE FROM WORKON WHERE MEM_ID=?",(MEMBER_ID.get(),))
    row=cur.fetchall()

    p=1
    
    member_home_listbox.delete(0,'end')#when i click PROJECTS once (if listbox shows 2 items) & when go back and again click PROJECTS then listbox shows 4 items & soon so THIS LINE CLEARS THOSE PREVIOUS ONES
    
    for data in row:
        
        member_home_listbox.insert(p,data)
        p=p+1
    
    
    #.place() and .grid() is works together
    member_home_label.place(x=100,y=10)
    member_home_back_button.grid(row=3,column=0,pady=50)
    member_home_inbox_button.grid(row=5,column=0,pady=20)
    member_home_piechart_button.grid(row=7,column=0,pady=20)


    #memProgressbar shows the progress of each project of a member
    
            
    def updateProgress():
        global temp
        clicked_item= member_home_listbox.curselection()
        
        for item in clicked_item:
            temp=member_home_listbox.get(item)
            print(temp[0])
       
        Database()
        cur.execute("SELECT PROGRESSBAR FROM WORKON WHERE MEM_ID=? AND PROJ_CODE=?",(MEMBER_ID.get(),temp[0],)) #select query to retrives all rows from TEAM table
        row1=cur.fetchall() #retrives all rows from TEAM table into row variable

        
        for data in row1:
            print(data[0])
            memProgressbar(data[0])
            break
            
    member_home_update_progress_button=ttk.Button(memberDashboard,text='Update Progress',command=updateProgress)#not done: first learn to display in proper way,what is TREE?? 

    member_home_update_progress_button.grid(row=7,column=5,padx=100)
    
 

def memLogin():
    global TEMP1,TEMP2
    
    TEMP1=MEMBER_MOBILE.get()
    TEMP2=MEMBER_ID.get()
    list1=[] #This list is to store all the rows fetched from database
    list2=[] #This list is to extract each row separately from list1
    Database()
    cur.execute("SELECT CELL,M_ID FROM MEMBERS") #select query to retrives all rows from TEAM table
    row=cur.fetchall() #retrives all rows from TEAM table into row variable
    
    for data in row: 
        list1.append(data)#each row is stored to each index of list1

    for erow in list1: #each row iteration
        list2=erow #EG: 1st index (i.e. 1st row (USERNAME and PWD) of TEAM table) of list1 is stored in list2
        if(TEMP1==list2[0] and TEMP2==list2[1]): #checking if username and password matches or not
            print("Login Successful")
            verifiedMember() #if username and password matches
            break
        
    else:
        messagebox.showerror("ERROR","Please enter correct username or password or Sign Up!")
        print("Login Unsuccessful")

member_checkbutton.grid(row=9,column=0,sticky=E)
member_login_button=ttk.Button(loginPage,text="Log in",command=memLogin)
member_login_button.grid(row=10,column=0,pady=10)


#list box for displaying all projects

cap_project_listbox=Listbox(allProjectWin,height=10,width=20,selectmode=SINGLE,bg="black",fg="red",font=("Calibri",12))
cap_project_listbox.grid(row=5,column=5,padx=70)

"""while entering into allProjectWin accessing the values of all projects which this TEAM has taken"""
def prjFun():

    functionOne(allProjectWin)
    
    

    #Adding list box
    Database()
    cur.execute("SELECT DISTINCT(PROJ_CODE) FROM WORKON,MEMBERS,TEAM WHERE MEM_ID=M_ID AND TEAM_CODE=T_CODE AND USERNAME=?",(CAP_USERNAME.get(),))
    row=cur.fetchall()

    p=1
    
    cap_project_listbox.delete(0,'end')#when i click PROJECTS once (if listbox shows 2 items) & when go back and again click PROJECTS then listbox shows 4 items & soon so THIS LINE CLEARS THOSE PREVIOUS ONES
    
    for data in row:
        
        cap_project_listbox.insert(p,data)
        p=p+1
        
    
    """Getting the value of the selected item from the list box"""

    def prjDetail():
        clicked_item= cap_project_listbox.curselection()
        #print(clicked_item)
        #print(cap_project_listbox.get(clicked_item))
        for item in clicked_item:
            temp=cap_project_listbox.get(item)
            print(temp[0])
        #cs=cap_project_listbox.curselection()[0]
        #temp=cap_project_listbox.get(cs)#temp holds the selected value from listbox
        #print(temp)#Project details from DB using value of temp
        Database()
        cur.execute("SELECT * FROM PROJECT,CLIENT WHERE CUST_ID=C_ID AND P_CODE=?",(temp[0],)) #select query to retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        for data in row:

            root12=Toplevel()
            root12.geometry('500x400')

            root12.title('Gaffer- The Project Monitor')
            
            show_prj_label=ttk.Label(root12,text="Project Details",font=("Calibri",20))

            show_prj_code_label=ttk.Label(root12,text="Project Code",font=("Calibri",12))
            show_prj_name_label=ttk.Label(root12,text="Project Name",font=("Calibri",12))
            show_prj_budget_label=ttk.Label(root12,text="Project Budget",font=("Calibri",12))
            show_prj_status_label=ttk.Label(root12,text="Project Status",font=("Calibri",12))
            show_prj_sdate_label=ttk.Label(root12,text="Starting Date",font=("Calibri",12))
            show_prj_ddate_label=ttk.Label(root12,text="Due Date",font=("Calibri",12))
            show_prj_client_id_label=ttk.Label(root12,text="Client Id",font=("Calibri",12))
            show_prj_client_name_label=ttk.Label(root12,text="Client Name",font=("Calibri",12))

            show_prj_code_label_result=ttk.Label(root12,text=data[0],font=("Calibri",12))
            show_prj_name_label_result=ttk.Label(root12,text=data[1],font=("Calibri",12))
            show_prj_budget_label_result=ttk.Label(root12,text=data[2],font=("Calibri",12))
            show_prj_status_label_result=ttk.Label(root12,text=data[3],font=("Calibri",12))
            show_prj_sdate_label_result=ttk.Label(root12,text=data[4],font=("Calibri",12))
            show_prj_ddate_label_result=ttk.Label(root12,text=data[5],font=("Calibri",12))
            show_prj_client_id_label_result=ttk.Label(root12,text=data[6],font=("Calibri",12))
            show_prj_client_name_label_result=ttk.Label(root12,text=data[8],font=("Calibri",12))

            show_prj_label.grid(row=1,column=2,columnspan=3,pady=20,padx=80)

            show_prj_code_label.grid(row=3,column=2,sticky=W,pady=5,padx=80)
            show_prj_name_label.grid(row=5,column=2,sticky=W,pady=5,padx=80)
            show_prj_budget_label.grid(row=7,column=2,sticky=W,pady=5,padx=80)
            show_prj_status_label.grid(row=9,column=2,sticky=W,pady=5,padx=80)
            show_prj_sdate_label.grid(row=11,column=2,sticky=W,pady=5,padx=80)
            show_prj_ddate_label.grid(row=13,column=2,sticky=W,pady=5,padx=80)
            show_prj_client_id_label.grid(row=15,column=2,sticky=W,pady=5,padx=80)
            show_prj_client_name_label.grid(row=17,column=2,sticky=W,pady=5,padx=80)

            show_prj_code_label_result.grid(row=3,column=3,sticky=W,pady=5,padx=5)
            show_prj_name_label_result.grid(row=5,column=3,sticky=W,pady=5,padx=5)
            show_prj_budget_label_result.grid(row=7,column=3,sticky=W,pady=5,padx=5)
            show_prj_status_label_result.grid(row=9,column=3,sticky=W,pady=5,padx=5)
            show_prj_sdate_label_result.grid(row=11,column=3,sticky=W,pady=5,padx=5)
            show_prj_ddate_label_result.grid(row=13,column=3,sticky=W,pady=5,padx=5)
            show_prj_client_id_label_result.grid(row=15,column=3,sticky=W,pady=5,padx=5)
            show_prj_client_name_label_result.grid(row=17,column=3,sticky=W,pady=5,padx=5)

            show_prj_done_btn=ttk.Button(root12,text='DONE',command=root12.destroy)
            show_prj_done_btn.grid(row=19,column=2,sticky=W,pady=20,padx=80)


    def updatePrjDDate():
        NEW_DDATE=StringVar()
        
        clicked_item= cap_project_listbox.curselection()
        #print(clicked_item)
        #print(cap_project_listbox.get(clicked_item))
        for item in clicked_item:
            temp=cap_project_listbox.get(item)
            print(temp[0])
        #cs=cap_project_listbox.curselection()[0]
        #temp=cap_project_listbox.get(cs)#temp holds the selected value from listbox
        #print(temp)#Project details from DB using value of temp
        Database()
        cur.execute("SELECT DUE_DATE FROM PROJECT WHERE P_CODE=?",(temp[0],)) #select query to retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        for data in row:

            root12=Toplevel()
            root12.geometry('600x400')
            root12.title('Gaffer- The Project Monitor')
            
            update_prj_ddate_label=ttk.Label(root12,text="Updating Due Date",font=("Calibri",20))
            
            old_ddate_label=ttk.Label(root12,text="Old Due Date",font=("Calibri",12))
            new_ddate_label=ttk.Label(root12,text="New Due Date",font=("Calibri",12))
            old_ddate_label_result=ttk.Label(root12,text=data[0],font=("Calibri",12))
            new_ddate_entry=ttk.Entry(root12,textvariable=NEW_DDATE,font=("Calibri",12))

            update_prj_ddate_label.grid(row=1,column=2,columnspan=3,pady=20,padx=80)
            old_ddate_label.grid(row=3,column=2,sticky=W,pady=5,padx=80)
            new_ddate_label.grid(row=5,column=2,sticky=W,pady=5,padx=80)
            old_ddate_label_result.grid(row=3,column=3,sticky=W,pady=5,padx=80)
            new_ddate_entry.grid(row=5,column=3,sticky=W,pady=5,padx=80)
            print(NEW_DDATE.get())
            print(temp[0])

            
            def updatedPrjDDate():
                Database()
                cur.execute("UPDATE PROJECT SET DUE_DATE=? WHERE P_CODE=?",(NEW_DDATE.get(),temp[0]))
                db.commit()
                

            
            update_prj_ddate_done_btn=ttk.Button(root12,text='DONE',command=root12.destroy)
            update_prj_ddate_done_btn.grid(row=7,column=2,sticky=W,pady=20,padx=80)
            
            update_prj_ddate_update_btn=ttk.Button(root12,text='UPDATE',command=updatedPrjDDate)
            update_prj_ddate_update_btn.grid(row=7,column=3,sticky=W,pady=20,padx=80)


    def prjBudget():

        global temp
        
        """progressChartWin=Toplevel()
        progressChartWin.geometry('300x300')
        progressChartWin.title('Progress Chart')"""
        
        
        budget_list=[]
        pname_list=[]
        left=[]
        clicked_item= cap_project_listbox.curselection()
        
        for item in clicked_item:
            temp=cap_project_listbox.get(item)
            print(temp[0])
        
        Database()
        cur.execute("SELECT Budget,P_NAME FROM PROJECT WHERE P_CODE=?",(temp[0],)) #retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        for data in row:
            budget_list.append(data[0]) #inserting all the progress of the members in each project to progress_list
            pname_list.append(data[1])  #inserting all the project name into pname_list

        
        
        #plt.plot(pname_list,progress_list) #this is for SIMPLE PLOTTING
        #plt.show()

        for i in range(len(pname_list)): #how many projects did member do- getting length according to that we have to assign X-VALUES of BAR
            left.append(i) # X-VALUES - to be on LEFT side of the BAR #different members may be assigned to different no. of projects so to get specific X-VALUES
        height= budget_list   #passing HEIGHTS of BARS
        print(height)
        tick_label = pname_list  #passing LABELS for BARS
        print(tick_label)
        
        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label, width=0.2, color = ['green', 'pink'])

        # naming the x-axis
        plt.xlabel('Project')

        # naming the y-axis
        plt.ylabel('Budget') 

        # plot title
        plt.title("Budget Analysis") #assigning the bar title with the specific member name

        # function to show the plot
        plt.show()

    """Second Page -- Captain window : All Project Window"""
    cap_project_window_label=ttk.Label(allProjectWin,text='Project Window',font=("Calibri",20))
    cap_project_back_button=ttk.Button(allProjectWin,text='Back',command=lambda:functionOne(captainDashboard))
    cap_project_add_button=ttk.Button(allProjectWin,text='Add Project',command=addProjectWin)
    cap_project_piechart_button=ttk.Button(allProjectWin,text='Bar Chart',command=prjBudget) #not done: first complete all then PIE-CHART
    

    #.place() and .grid() is works together
    cap_project_window_label.place(x=100,y=10)
    cap_project_back_button.grid(row=3,column=0,pady=50)
    cap_project_add_button.grid(row=5,column=0,pady=20)
    cap_project_piechart_button.grid(row=7,column=0,pady=20)

            
    #cap_project_listbox.bind("<<ListboxSelect>>",lambda x: go())
    cap_project_show_button=ttk.Button(allProjectWin,text='Show',command=prjDetail)#not done: first learn to display in proper way,what is TREE??

    cap_project_show_button.grid(row=7,column=5,padx=100)

    cap_project_update_ddate_button=ttk.Button(allProjectWin,text='Update Due Date',command=updatePrjDDate)#not done: first learn to display in proper way,what is TREE??

    cap_project_update_ddate_button.grid(row=9,column=5,padx=100)


#list box for members displaying
cap_member_listbox=Listbox(allMemberWin,height=10,width=20,selectmode=BROWSE,bg="black",fg="red",font=("Calibri",12))
cap_member_listbox.grid(row=5,column=5,padx=70)

def memFun():

    functionOne(allMemberWin)

    


    #Adding list box
    Database()
    cur.execute("SELECT M_ID FROM MEMBERS,TEAM WHERE TEAM_CODE=T_CODE AND USERNAME=?",(CAP_USERNAME.get(),))
    row=cur.fetchall()

    p=1
    
    cap_member_listbox.delete(0,'end')#when i click PROJECTS once (if listbox shows 2 items) & when go back and again click PROJECTS then listbox shows 4 items & soon so THIS LINE CLEARS THOSE PREVIOUS ONES
    
    for data in row:
        
        cap_member_listbox.insert(p,data)
        p=p+1
        

    

    
    
    """Getting the value of the selected item from the list box"""

    def memDetail():
        global temp
        clicked_item= cap_member_listbox.curselection()
        #print(clicked_item)
        #print(cap_project_listbox.get(clicked_item))
        for item in clicked_item:
            temp=cap_member_listbox.get(item)
            print(temp[0])
        #cs=cap_project_listbox.curselection()[0]
        #temp=cap_project_listbox.get(cs)#temp holds the selected value from listbox
        #print(temp)#Project details from DB using value of temp
        Database()
        cur.execute("SELECT M_ID,M_NAME,CELL,START_DATE,COUNTRY,T_NAME,R_NAME FROM MEMBERS,ROLE,TEAM WHERE ROLE_ID=R_ID AND TEAM_CODE=T_CODE AND M_ID=?",(temp[0],)) #select query to retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        """Database()
            row1=cur.execute("SELECT * FROM WORKON WHERE MEM_ID=?",(temp[0],))
            print(row1)""" #for displaying the projects in which member is working on
        print(row)
        for data in row:

            root12=Toplevel()
            root12.geometry('500x400')
            root12.title('Gaffer- The Project Monitor')


            show_mem_label=ttk.Label(root12,text="Member Details",font=("Calibri",20))

            show_mem_code_label=ttk.Label(root12,text="Member Id",font=("Calibri",12))
            show_mem_name_label=ttk.Label(root12,text="Member Name",font=("Calibri",12))
            #show_mem_age_label=ttk.Label(root12,text="Age",font=("Calibri",12))
            show_mem_mobile_label=ttk.Label(root12,text="Mobile No",font=("Calibri",12))
            show_mem_sdate_label=ttk.Label(root12,text="Joining Date",font=("Calibri",12))
            show_mem_country_label=ttk.Label(root12,text="Country",font=("Calibri",12))
            show_mem_team_name_label=ttk.Label(root12,text="Team",font=("Calibri",12))
            show_mem_role_name_label=ttk.Label(root12,text="Designation",font=("Calibri",12))

            show_mem_code_label_result=ttk.Label(root12,text=data[0],font=("Calibri",12))
            show_mem_name_label_result=ttk.Label(root12,text=data[1],font=("Calibri",12))
            #show_mem_age_label_result=ttk.Label(root12,text=data[2],font=("Calibri",12))
            show_mem_mobile_label_result=ttk.Label(root12,text=data[2],font=("Calibri",12))
            show_mem_sdate_label_result=ttk.Label(root12,text=data[3],font=("Calibri",12))
            show_mem_country_label_result=ttk.Label(root12,text=data[4],font=("Calibri",12))
            show_mem_team_name_label_result=ttk.Label(root12,text=data[5],font=("Calibri",12))
            show_mem_role_name_label_result=ttk.Label(root12,text=data[6],font=("Calibri",12))

            show_mem_label.grid(row=1,column=2,columnspan=3,pady=20,padx=80)

            show_mem_code_label.grid(row=3,column=2,sticky=W,pady=5,padx=80)
            show_mem_name_label.grid(row=5,column=2,sticky=W,pady=5,padx=80)
            #show_mem_age_label.grid(row=7,column=2,sticky=W,pady=5,padx=80)
            show_mem_mobile_label.grid(row=9,column=2,sticky=W,pady=5,padx=80)
            show_mem_sdate_label.grid(row=11,column=2,sticky=W,pady=5,padx=80)
            show_mem_country_label.grid(row=13,column=2,sticky=W,pady=5,padx=80)
            show_mem_team_name_label.grid(row=15,column=2,sticky=W,pady=5,padx=80)
            show_mem_role_name_label.grid(row=17,column=2,sticky=W,pady=5,padx=80)

            show_mem_code_label_result.grid(row=3,column=3,sticky=W,pady=5,padx=5)
            show_mem_name_label_result.grid(row=5,column=3,sticky=W,pady=5,padx=5)
            #show_mem_age_label_result.grid(row=7,column=3,sticky=W,pady=5,padx=5)
            show_mem_mobile_label_result.grid(row=9,column=3,sticky=W,pady=5,padx=5)
            show_mem_sdate_label_result.grid(row=11,column=3,sticky=W,pady=5,padx=5)
            show_mem_country_label_result.grid(row=13,column=3,sticky=W,pady=5,padx=5)
            show_mem_team_name_label_result.grid(row=15,column=3,sticky=W,pady=5,padx=5)
            show_mem_role_name_label_result.grid(row=17,column=3,sticky=W,pady=5,padx=5)

            show_mem_done_btn=ttk.Button(root12,text='DONE',command=root12.destroy)
            show_mem_done_btn.grid(row=19,column=2,sticky=W,pady=20,padx=80)

    """when you clicked send message on ALL MEMBER WINDOW then this function is called"""
    #this function selects the particular member from the listbox to which captain wants to send the message

    def sentMsgToMem():
        inputValue=SEND_MSG.get("1.0",END) #accessing the values of textarea created in sendMsgToMem() function
        print(inputValue)
        Database()
        cur.execute("UPDATE MEMBERS SET MINBOX=? WHERE M_ID=?",(inputValue,temp[0])) #UPDATING the message to members table
        db.commit()

        """send_msg_label=ttk.Label(root12,text="Messanger",font=("Calibri",20))
        send_msg_label.grid(row=1,column=2,columnspan=3,pady=20,padx=80)
            
        """


    def sendMsgToMem():
        global SEND_MSG,temp  #making it global so that it can be visible and can be used in other functions(called functions i.e sentMsgToMem())
        
        clicked_item= cap_member_listbox.curselection()
      
        for item in clicked_item:
            temp=cap_member_listbox.get(item)
            
            print(temp[0])
    
        Database()
        #cur.execute("SELECT M_ID,M_NAME,CELL,START_DATE,COUNTRY,T_NAME,R_NAME FROM MEMBERS,ROLE,TEAM WHERE ROLE_ID=R_ID AND TEAM_CODE=T_CODE AND M_ID=?",(temp[0],)) #select query to retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        root13=Toplevel()
        root13.geometry('350x300')
        root13.title('Gaffer- The Project Monitor')

        SEND_MSG=scrolledtext.ScrolledText(root13,height=15,width=35)
        SEND_MSG.grid(row=2,column=1,columnspan=2)

        btn_send_tomem=ttk.Button(root13,text="SEND",command=sentMsgToMem)
        btn_send_tomem.grid(row=4,column=1,sticky=N+S+E+W)
        
        send_msg_btn=ttk.Button(root13,text='DONE',command=root13.destroy)
        send_msg_btn.grid(row=5,column=1,sticky=N+S+E+W)


    def memProgressBarChart():
        
        global temp
        
        """progressChartWin=Toplevel()
        progressChartWin.geometry('300x300')
        progressChartWin.title('Progress Chart')"""
        
        
        progress_list=[]
        pname_list=[]
        left=[]
        clicked_item= cap_member_listbox.curselection()
        
        for item in clicked_item:
            temp=cap_member_listbox.get(item)
            print(temp[0])
        
        Database()
        cur.execute("SELECT PROGRESSBAR,P_NAME FROM WORKON,MEMBERS,PROJECT WHERE MEM_ID=M_ID AND PROJ_CODE=P_CODE AND M_ID=?",(temp[0],)) #retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        for data in row:
            progress_list.append(data[0]) #inserting all the progress of the members in each project to progress_list
            pname_list.append(data[1])  #inserting all the project name into pname_list

        
        
        #plt.plot(pname_list,progress_list) #this is for SIMPLE PLOTTING
        #plt.show()

        for i in range(len(pname_list)): #how many projects did member do- getting length according to that we have to assign X-VALUES of BAR
            left.append(i) # X-VALUES - to be on LEFT side of the BAR #different members may be assigned to different no. of projects so to get specific X-VALUES
        height= progress_list   #passing HEIGHTS of BARS
        print(height)
        tick_label = pname_list  #passing LABELS for BARS
        print(tick_label)
        
        # plotting a bar chart
        plt.bar(left, progress_list, tick_label = tick_label, width=0.2, color = ['green', 'pink'])

        # naming the x-axis
        plt.xlabel('project')

        # naming the y-axis
        plt.ylabel('progress')

        Database()
        cur.execute("SELECT M_NAME FROM MEMBERS WHERE M_ID=?",(temp[0],)) #retriving the specific member name for title
        row=cur.fetchall()
        for data in row:
            print(data[0]) 

        # plot title
        plt.title("Progress Chart of " + data[0]) #assigning the bar title with the specific member name

        # function to show the plot
        plt.show()

    def deletingMem():

        clicked_item= cap_member_listbox.curselection()
        
        for item in clicked_item:
            temp=cap_member_listbox.get(item)
            print("deleting M_ID= " + temp[0])
        
        Database()
        cur.execute("DELETE FROM 'MEMBERS' WHERE M_ID=?",(temp[0],))
        db.commit()

        cur.execute("SELECT * FROM 'MEMBERS' WHERE M_ID=?",(temp[0],))
        row=cur.fetchall()

        for data in row:
            print(data[0])
    """"Third page -- Captain Window: All Member Window"""

    cap_member_window_label=ttk.Label(allMemberWin,text='Member Window',font=("Calibri",20))
    cap_member_back_button=ttk.Button(allMemberWin,text='Back',command=lambda:functionOne(captainDashboard))
    cap_member_add_button=ttk.Button(allMemberWin,text='Add Member',command=addMemberWin)
    cap_member_piechart_button=ttk.Button(allMemberWin,text='Bar Chart',command=memProgressBarChart)#not done: first complete all then PIE-CHART
        
    #.place() and .grid() is works together
    cap_member_window_label.place(x=100,y=10)
    cap_member_back_button.grid(row=3,column=0,pady=50)
    cap_member_add_button.grid(row=5,column=0,pady=20)
    cap_member_piechart_button.grid(row=7,column=0,pady=20)

    #cap_project_listbox.bind("<<ListboxSelect>>",lambda x: go())
    cap_member_show_button=ttk.Button(allMemberWin,text='Show',command=memDetail)#not done: first learn to display in proper way,what is TREE??
    cap_member_delete_button=ttk.Button(allMemberWin,text='Delete**',command=deletingMem) #not done: learn to delete from maam gave sql
    cap_member_send_msg_button=ttk.Button(allMemberWin,text='Send Message',command=sendMsgToMem)

    cap_member_send_msg_button.grid(row=13,column=5,padx=100)
    cap_member_show_button.grid(row=9,column=5,padx=100)
    cap_member_delete_button.grid(row=11,column=5,padx=100)








cap_client_listbox=Listbox(allClientWin,height=10,width=20,selectmode=BROWSE,bg="black",fg="red",font=("Calibri",12))
cap_client_listbox.grid(row=5,column=5,padx=70)
    
#for displaying the list of clients
    
def clientFun():

    functionOne(allClientWin)

    """"Fourth page -- Captain Window: All Clients Window"""

    cap_client_window_label=ttk.Label(allClientWin,text='Client Window',font=("Calibri",20))
    cap_client_back_button=ttk.Button(allClientWin,text='Back',command=lambda:functionOne(captainDashboard))
    cap_client_add_button=ttk.Button(allClientWin,text='Add Client',command=addClientWin)
    cap_client_piechart_button=ttk.Button(allClientWin,text='Bar Chart',command=lambda:functionOne(captainDashboard))#not done: first complete all then PIE-CHART


    #Adding list box
    Database()
    cur.execute("SELECT DISTINCT(C_ID) FROM PROJECT,CLIENT,WORKON,MEMBERS,TEAM WHERE CUST_ID= C_ID AND P_CODE=PROJ_CODE AND MEM_ID=M_ID AND TEAM_CODE=T_CODE AND USERNAME=?;",(CAP_USERNAME.get(),))
    row=cur.fetchall()

    p=1
    
    cap_client_listbox.delete(0,'end')#when i click PROJECTS once (if listbox shows 2 items) & when go back and again click PROJECTS then listbox shows 4 items & soon so THIS LINE CLEARS THOSE PREVIOUS ONES
    print(row)
        
    for data in row:
        
        cap_client_listbox.insert(p,data)
        p=p+1
        

    

    #.place() and .grid() is works together
    cap_client_window_label.place(x=100,y=10)
    cap_client_back_button.grid(row=3,column=0,pady=50)
    cap_client_add_button.grid(row=5,column=0,pady=20)
    cap_client_piechart_button.grid(row=7,column=0,pady=20)

    
    """Getting the value from database of the selected clients from the list box"""

    def clientDetail():
        clicked_item= cap_client_listbox.curselection()
        #print(clicked_item)
        #print(cap_project_listbox.get(clicked_item))
        for item in clicked_item:
            temp=cap_client_listbox.get(item)
            print(temp[0])
        #cs=cap_project_listbox.curselection()[0]
        #temp=cap_project_listbox.get(cs)#temp holds the selected value from listbox
        #print(temp)#Project details from DB using value of temp
        Database()
        cur.execute("SELECT C_ID,C_NAME,STREET,CITY,COUNTRY,EMAIL,P_NAME FROM CLIENT,PROJECT WHERE CUST_ID=C_ID AND C_ID=?",(temp[0],)) #select query to retrives all rows from TEAM table
        row=cur.fetchall() #retrives all rows from TEAM table into row variable

        print(row)
        """Database()
            row1=cur.execute("SELECT * FROM WORKON WHERE MEM_ID=?",(temp[0],))
            print(row1)""" #for displaying the projects in which member is working on
        
        for data in row:

            root12=Toplevel()
            root12.geometry('500x400')
            root12.title('Gaffer- The Project Monitor')

            show_client_label=ttk.Label(root12,text="Client Details",font=("Calibri",20))

            show_client_id_label=ttk.Label(root12,text="Client Id",font=("Calibri",12))
            show_client_name_label=ttk.Label(root12,text="Client Name",font=("Calibri",12))
            show_client_street_label=ttk.Label(root12,text="Street",font=("Calibri",12))
            show_client_city_label=ttk.Label(root12,text="City",font=("Calibri",12))
            show_client_email_label=ttk.Label(root12,text="Email",font=("Calibri",12))
            show_client_country_label=ttk.Label(root12,text="Country",font=("Calibri",12))
            
            #show_client_team_name_label=ttk.Label(root12,text="Team",font=("Calibri",12))
            #show_client_role_name_label=ttk.Label(root12,text="Designation",font=("Calibri",12))

            show_client_id_label_result=ttk.Label(root12,text=data[0],font=("Calibri",12))
            show_client_name_label_result=ttk.Label(root12,text=data[1],font=("Calibri",12))
            show_client_street_label_result=ttk.Label(root12,text=data[2],font=("Calibri",12))
            show_client_city_label_result=ttk.Label(root12,text=data[3],font=("Calibri",12))
            show_client_email_label_result=ttk.Label(root12,text=data[4],font=("Calibri",12))
            show_client_country_label_result=ttk.Label(root12,text=data[5],font=("Calibri",12))
            #show_client_team_name_label_result=ttk.Label(root12,text=data[6],font=("Calibri",12))
            #show_client_role_name_label_result=ttk.Label(root12,text=data[7],font=("Calibri",12))

            show_client_label.grid(row=1,column=2,columnspan=3,pady=20,padx=80)

            show_client_id_label.grid(row=3,column=2,sticky=W,pady=5,padx=80)
            show_client_name_label.grid(row=5,column=2,sticky=W,pady=5,padx=80)
            show_client_street_label.grid(row=7,column=2,sticky=W,pady=5,padx=80)
            show_client_city_label.grid(row=9,column=2,sticky=W,pady=5,padx=80)
            show_client_email_label.grid(row=11,column=2,sticky=W,pady=5,padx=80)
            show_client_country_label.grid(row=13,column=2,sticky=W,pady=5,padx=80)
            #show_client_team_name_label.grid(row=15,column=2,sticky=W,pady=5,padx=80)
            #show_client_role_name_label.grid(row=17,column=2,sticky=W,pady=5,padx=80)

            show_client_id_label_result.grid(row=3,column=3,sticky=W,pady=5,padx=5)
            show_client_name_label_result.grid(row=5,column=3,sticky=W,pady=5,padx=5)
            show_client_street_label_result.grid(row=7,column=3,sticky=W,pady=5,padx=5)
            show_client_city_label_result.grid(row=9,column=3,sticky=W,pady=5,padx=5)
            show_client_email_label_result.grid(row=11,column=3,sticky=W,pady=5,padx=5)
            show_client_country_label_result.grid(row=13,column=3,sticky=W,pady=5,padx=5)
            #show_client_team_name_label_result.grid(row=15,column=3,sticky=W,pady=5,padx=5)
            #show_client_role_name_label_result.grid(row=17,column=3,sticky=W,pady=5,padx=5)

            show_client_done_btn=ttk.Button(root12,text='DONE',command=root12.destroy)
            show_client_done_btn.grid(row=19,column=2,sticky=W,pady=20,padx=80)

            break #if there is multiple rows as output then that many windows will be created due to this for loop

    #cap_project_listbox.bind("<<ListboxSelect>>",lambda x: go())
    cap_client_show_button=ttk.Button(allClientWin,text='Show',command=clientDetail)#not done: first learn to display in proper way,what is TREE??
    cap_client_delete_button=ttk.Button(allClientWin,text='Delete',command=lambda:functionOne(captainDashboard)) #not done: learn to delete from maam gave sql

    cap_client_show_button.grid(row=7,column=5,padx=100)
    cap_client_delete_button.grid(row=9,column=5,padx=100)
    

    
"""Second Page -- Captain Dashboard"""
captain_dashboard_welcome_label=ttk.Label(captainDashboard,text='Welcome To Dashboard')
captain_dashboard_logout_button=ttk.Button(captainDashboard,text='Logout',command=lambda:functionOne(loginPage))
captain_dashboard_project_button=ttk.Button(captainDashboard,text='Projects',command=prjFun)
captain_dashboard_member_button=ttk.Button(captainDashboard,text='Members',command=memFun)
captain_dashboard_client_button=ttk.Button(captainDashboard,text='Clients',command=clientFun)
captain_dashboard_message_button=ttk.Button(captainDashboard,text='Send Message',command=memFun)
captain_dashboard_date_button=ttk.Button(captainDashboard,text='Update Due Date',command=prjFun)


captain_dashboard_welcome_label.grid(row=0,column=3,columnspan=2,sticky=N+S+E+W)
captain_dashboard_logout_button.grid(row=1,column=0,pady=20)
captain_dashboard_project_button.grid(row=3,column=3)
captain_dashboard_member_button.grid(row=5,column=3)
captain_dashboard_client_button.grid(row=7,column=3)
captain_dashboard_message_button.grid(row=9,column=3)
captain_dashboard_date_button.grid(row=11,column=3)



"""Adding pictures in the dashboard of Captain"""

project_img=PhotoImage(file="C:\\Users\\Dipesh Shrestha\\Gaffer in JUPYTER NOTEBOOK\\project1.png")
project_img_label=ttk.Label(captainDashboard,image=project_img)

member_img=PhotoImage(file="C:\\Users\\Dipesh Shrestha\\Gaffer in JUPYTER NOTEBOOK\\member.png")
member_img_label=ttk.Label(captainDashboard,image=member_img)

client_img=PhotoImage(file="C:\\Users\\Dipesh Shrestha\\Gaffer in JUPYTER NOTEBOOK\\client.png")
client_img_label=ttk.Label(captainDashboard,image=client_img)

message_img=PhotoImage(file="C:\\Users\\Dipesh Shrestha\\Gaffer in JUPYTER NOTEBOOK\\message.png")
message_img_label=ttk.Label(captainDashboard,image=message_img)

duedate_img=PhotoImage(file="C:\\Users\\Dipesh Shrestha\\Gaffer in JUPYTER NOTEBOOK\\due date.png")
duedate_img_label=ttk.Label(captainDashboard,image=duedate_img)


project_img_label.grid(row=3,column=1)
member_img_label.grid(row=5,column=1)
client_img_label.grid(row=7,column=1)
message_img_label.grid(row=9,column=1)
duedate_img_label.grid(row=11,column=1)




"""Ending of the Application"""
functionOne(loginPage)

loginPage.mainloop()
