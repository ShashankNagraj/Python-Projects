from tkinter import *
import sqlite3


#CREATE A GUI WINDOW
window=Tk()
window.title("YOUR CHOICE")
window.geometry("320x340")
window.resizable(0, 0)
file_name="File.db" #Its your choice

#CREATE A DATABASE AND CONNECTION TO IT
conn=sqlite3.connect(file_name)
cursor=conn.cursor()


FullName=StringVar()
gender=StringVar()
branch=StringVar() 

                      
def query():
    #FUNCTION WHICH PERFORMS CREATING TABLE,INSERTING VALUES
    #INTO IT AND SELECT AND UPDATE THE CONTENTS OF THE TABLE
    conn=sqlite3.connect(file_name)
    with conn:
        c=conn.cursor()
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS DETAILS(USN VARCHAR type,sl_no INTEGER  PRIMARY KEY AUTOINCREMENT,FullName TEXT type NOT NULL ,gender TEXT NOT NULL,branch TEXT NOT NULL)')
        cursor.execute('INSERT INTO DETAILS(FULLNAME,GENDER,BRANCH) VALUES (?,?,?)',(e1.get().upper(),gender.get(),branch.get()))
        conn.commit()
        
        c.execute("DELETE FROM DETAILS WHERE FullName=''")
        c.execute("DELETE FROM DETAILS WHERE GENDER=''")
        c.execute("DELETE FROM DETAILS WHERE BRANCH=''")
        
        #CSE USN GENERATION
        c.execute("SELECT FullName FROM DETAILS where branch='CSE' ORDER BY FullName ASC   ")
        result=c.fetchall()
        c.execute("SELECT sl_no FROM DETAILS where branch='CSE' ORDER BY FullName ASC")
        sl_list=c.fetchall()
        list_usn=gen_usn(result,"CSE")
        
        for i in range(0,len(list_usn)):
            c.execute("UPDATE  DETAILS SET (USN)=(?) WHERE (branch='CSE' AND Fullname=(?) AND sl_no=(?))",(list_usn[i],result[i][0],sl_list[i][0]))
             
        #ECE USN GENERATION     
        c.execute("SELECT FullName FROM DETAILS where branch='ECE' ORDER BY FullName ASC   ")
        result=c.fetchall()
        c.execute("SELECT sl_no FROM DETAILS where branch='ECE' ORDER BY FullName ASC")
        sl_list=c.fetchall()
        list_usn=gen_usn(result,"ECE")
        for i in range(0,len(list_usn)):
            c.execute("UPDATE  DETAILS SET (USN)=(?) WHERE (branch='ECE' AND Fullname=(?) AND sl_no=(?))",(list_usn[i],result[i][0],sl_list[i][0]))
        
        #ME USN GENERATION
        c.execute("SELECT FullName FROM DETAILS where branch='ME' ORDER BY FullName ASC   ")
        result=c.fetchall()
        c.execute("SELECT sl_no FROM DETAILS where branch='ME' ORDER BY FullName ASC")
        sl_list=c.fetchall()
        if(len(result)!=0):
            list_usn=gen_usn(result,"ME")
            for i in range(0,len(list_usn)):
                c.execute("UPDATE  DETAILS SET (USN)=(?) WHERE (branch='ME' AND Fullname=(?) AND sl_no=(?))",(list_usn[i],result[i][0],sl_list[i][0]))
        
        conn.commit()
        
          
def all_list():
    #FUNCTION TO FETCH ALL THE RECORDS IN THE TABLE
    with conn:
        c=conn.cursor()
        top=Toplevel()
        top.title("FULL LIST")
        top.geometry("320x340")
        top.mainloop(2) 
        a=Listbox(top,width=300,height=320)
        c.execute("Select USN,FULLNAME from DETAILS ORDER BY USN ASC")
        records_in=c.fetchall()
       
        row_format="{:15} {:30}"
        
        for i in range(0,len(records_in)):
            a.insert(END,row_format.format(records_in[i][0],records_in[i][1]))
            a.grid(column=6)
        a.pack()
        conn.commit()

        
def gen_usn(list_name,br):
    #FUNCTION TO GENERATE USN FOR ALL BRANCH
    i=1
    usn_list=[]
    if(br=="CSE"):
        #GENERATES USN FOR A STUDENT OF CSE
        for values in range(0,len(list_name)):
            if(i<10):
                usn="CS00"+str(i)
            elif(i<100):
                usn="CS0"+str(i)
            elif(i>99):
                usn="CS"
            i+=1
            usn_list.append(usn)
            
        return usn_list
    elif(br=="ECE"):
        #GENERATES USN FOR A STUDENT OF ECE
        for values in range(0,len(list_name)):
            if(i<10):
                usn="EC00"+str(i)
            elif(i<100):
                usn="EC0"+str(i)
            elif(i>99):
                usn="EC"
            i+=1
            usn_list.append(usn)
            
        return usn_list
    elif(br=="ME"):
        #GENERATES USN FOR A STUDENT OF ME
        for values in range(0,len(list_name)):
            if(i<10):
                usn="ME00"+str(i)
            elif(i<100):
                usn="ME0"+str(i)
            elif(i>99):
                usn="ME"
            i+=1
            usn_list.append(usn)
            
        return usn_list
        
       
def cse_list():
    #FUNCTION TO FETCH RECORDS OF CSE BRANCH
    conn=sqlite3.connect(file_name)
    with conn:
        c=conn.cursor()
        top=Toplevel()
        top.title("CSE LIST")
        top.geometry("320x340")
        top.mainloop(2) 
        a=Listbox(top,width=300,height=320)    
        c.execute("Select USN,FULLNAME from DETAILS WHERE BRANCH='CSE' ORDER BY USN ASC ")
        records_in=c.fetchall()
        
        row_format="{:15} {:30}"
        
        for i in range(0,len(records_in)):
            a.insert(END,row_format.format(records_in[i][0],records_in[i][1]))
            a.grid(column=6)
        a.pack()
        conn.commit()
        
def ece_list():
    #FUNCTION TO FETCH RECORDS OF ECE BRANCH
    conn=sqlite3.connect(file_name)
    with conn:
        c=conn.cursor()
        top=Toplevel()
        top.title("ECE LIST")
        top.geometry("320x340")
        top.mainloop(2) 
        a=Listbox(top,width=300,height=320)    
        c.execute("Select USN,FULLNAME from DETAILS WHERE BRANCH='ECE' ORDER BY USN ASC ")
        records_in=c.fetchall()
        
        row_format="{:15} {:30}"
        
        for i in range(0,len(records_in)):
            a.insert(END,row_format.format(records_in[i][0],records_in[i][1]))
            a.grid(column=6)
        a.pack()
        conn.commit()
        
def me_list():
    #FUNCTION TO FETCH RECORDS OF ME BRANCH
    conn=sqlite3.connect(file_name)
    with conn:
        c=conn.cursor()
        top=Toplevel()
        top.title("ME LIST")
        top.geometry("320x340")
        top.mainloop(3) 
        a=Listbox(top,width=300,height=320)    
        c.execute("Select USN,FULLNAME from DETAILS WHERE BRANCH='ME' ORDER BY USN ASC ")
        records_in=c.fetchall()
        row_format="{:15} {:30}"
        
        for i in range(0,len(records_in)):
            a.insert(END,row_format.format(records_in[i][0],records_in[i][1]))
            a.grid(column=6)
        a.pack()
        conn.commit()
        
#WIDGET TO ENTER THE NAME
Your_name=Label(window,text='Your Name',width=20)
Your_name.grid(row=0)

e1=Entry(window,bg="yellow",cursor="hand2",width=25)
e1.place(x=120,y=0)

#WIDGET TO ENTER THE GENDER
gender_label=Label(window,text="Gender",width=20)
gender_label.grid(row=1)

c1=Radiobutton(window,text="MALE",value="MALE",variable=gender)
c1.place(x=120,y=20)

c2=Radiobutton(window,text="FEMALE",variable=gender,value="FEMALE")
c2.place(x=120,y=40)

#WIDGET TO ENTER THE BRANCH
Label(window,text="Branch",width=20).place(x=0,y=60)
    
cse=Radiobutton(window,text="CSE",variable=branch,value="CSE")
cse.place(x=120,y=60)

ece=Radiobutton(window,text="ECE",variable=branch,value="ECE")
ece.place(x=120,y=80)

me=Radiobutton(window,text="ME",variable=branch,value="ME")
me.place(x=120,y=100)
   
#CREATE  BUTTONS    
b1=Button(window,text="Submit",width=25,command=query)
b1.place(x=100,y=130)

query_btn=Button(window,text="ALL STUDENT LIST",width=25,command=all_list)
query_btn.place(x=100,y=210)

csn_btn=Button(window,text="CSE LIST",width=10,command=cse_list)
csn_btn.place(x=10,y=250)

ece_btn=Button(window,text="ECE LIST",width=10,command=ece_list)
ece_btn.place(x=110,y=250)

me_btn=Button(window,text="ME LIST",width=10,command=me_list)
me_btn.place(x=210,y=250)

conn.commit()

window.mainloop()