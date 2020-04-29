from tkinter import *


window=Tk()
window.title("CALCULATOR")
window.geometry("320x340")
window.resizable(0, 0)


def btn_click(item):
    global expression 
    expression+=str(item)
    input_text.set(expression)

def btn_clear():
    global expression 
    expression=""
    input_text.set("")

def btn_equal():
    global expression 
    result=str(eval(expression))
    input_text.set(result)
    expression=""

expression=""
input_text=StringVar()
input_frame=Frame(window,width=400,height=50,bd=3,highlightbackground="green",highlightcolor="red")
input_frame.pack(side=TOP)

input_field=Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg='#FFA07A',bd=3)
input_field.grid(row=0,columnspan=4)
input_field.pack(ipady=10)
input_field.focus_set()



btns_frame=Frame(window,width=400,height=272.5,bg="#8B0000")


btns_frame.columnconfigure(0,pad=3)
btns_frame.columnconfigure(1,pad=3)
btns_frame.columnconfigure(2,pad=3)
btns_frame.columnconfigure(3,pad=3)

btns_frame.rowconfigure(0,pad=3)
btns_frame.rowconfigure(1,pad=3)
btns_frame.rowconfigure(2,pad=3)
btns_frame.rowconfigure(3,pad=3)
btns_frame.rowconfigure(4,pad=3)
btns_frame.rowconfigure(5,pad=3)


clear=Button(btns_frame,text="Clear",fg="#191970",width=32,height=3,bd=0,bg="#FFD700",cursor="hand2",command=btn_clear).grid(row=1,column=0,columnspan=3,ipadx=2)
divide=Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("/")).grid(row=1,column=3)



seven=Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("7")).grid(row=2,column=0)
eight=Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("8")).grid(row=2,column=1)
nine=Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("9")).grid(row=2,column=2)
multiply=Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("*")).grid(row=2,column=3)

four=Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("4")).grid(row=3,column=0)
five=Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("5")).grid(row=3,column=1)
six=Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("6")).grid(row=3,column=2)
minus=Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("-")).grid(row=3,column=3)

three=Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("3")).grid(row=4,column=0)
two=Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("2")).grid(row=4,column=1)
one=Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("1")).grid(row=4,column=2)
plus=Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("+")).grid(row=4,column=3)

dot=Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click(".")).grid(row=5,column=2)
enter=Button(btns_frame,text="Enter",fg="black",width=10,height=3,bd=0,bg="#FFD700",cursor="hand2",command=btn_equal).grid(row=5,column=3)
zero=Button(btns_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#FFD700",cursor="hand2",command=lambda:btn_click("0")).grid(row=5,columnspan=2,ipadx=1)

btns_frame.pack()
window.mainloop()














