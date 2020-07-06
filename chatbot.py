from tkinter import *
import speech_recognition as sr 
import wikipedia
import pyttsx3 
scr=Tk()
scr.title("Chatbot")
scr.resizable(0,0)
scr.configure(bg="black")
scr.geometry('1072x655')
l=Label(scr,text="   Welcome to Saturn     ",bg="black",fg="blue",font=('time','70','bold'))
l.place(x=1,y=1)
l=Label(scr,text="Clear screen before every search",bg="black",fg="blue",font=('time','22','bold'))
l.place(x=300,y=600)
text=Text(scr,width=70,height=15,wrap=WORD,font=('Time','20'),selectbackground="grey",bg="gray10",fg="white", insertbackground='white')
text.place(x=1,y=116)
b=Button(scr,text="Enter",bg="limegreen",fg="black",font=('Time','20','bold'),command=lambda:Text())
b.place(x=977,y=600)
b1=Button(scr,text="Voice",bg="Tomato",fg="black",font=('Time','20','bold'),command=lambda:Voice())
b1.place(x=97,y=600)
b2=Button(scr,text="Clear",bg="firebrick2",fg="black",font=('Time','20','bold'),command=lambda:clear())
b2.place(x=882,y=600)
b3=Button(scr,text=" Help ",bg="DeepSkyBlue",fg="black",font=('Time','20','bold'),command=lambda:Help())
b3.place(x=1,y=600)
vscroll = Scrollbar(scr, orient=VERTICAL, command=text.yview,activebackground="red")
text['yscroll'] = vscroll.set
vscroll.place(in_=text, relx=1.0, relheight=1.0, bordermode="outside")
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("Hey ! Welcome to Saturn. ")

engine.runAndWait()
cmatch={"hello":"hey","hey":"hello","hi":"hola","your name":"call me Saturn","your father":"I consider Master Yash Dixit my only family.",
"your age":"I launched in 2020, I'm still a newbie","your birthday":
"Master Yash Dixit celebrates his birthday on April 3rd, I think it's a good day to celebrate.","namaste":"irasshaimase","you are intelligent":"Arigato",
"who are you":"I am Saturn your Smart Assistant. Ask me anything you like.","you single":"I'm still waiting for the right electronic device to steal my heart",
"you married":"No, I'm still waiting for the right electronic device to steal my heart","your favourite movie":"Civil War",
"your favourite series":"Breading Bad","your favourite anime":"One piece","yash dixit":
"Master Yash Dixit is a software engineer and the mastermind behind me."}
def clear():
    text.delete(1.0,END)

def Voice():
    engine.say("Speak now")
    engine.runAndWait()
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            query = r.recognize_google(audio2)
            query = query.lower()
            search(query)
    except sr.RequestError as e:
         text.delete(0.0,END)
         text.insert(0.0,"Error: API call failed. Key valid? Internet connection?")          
    except sr.UnknownValueError: 
         text.delete(0.0,END)
         text.insert(0.0,"Error: Unable to understand audio.")   

def Text():
    query=text.get(0.0,END)
    query=query.lower()
    search(query)
        
def search(query):
    if(len(query)>40):
        result="Error: Request too long to be processed. Try using keywords or short sentences.\nYou may also see this error if you forget to clear screen before search."
        text.delete(0.0,END)
        text.insert(0.0,result)
    else:
        
        flag=0
        for i in cmatch:
            if(re.search(i,query)):
                result=cmatch.get(i)
                flag=1
        if(flag==0):
            try:
                result=wikipedia.summary(query)
            except wikipedia.PageError:
                result="Your search does not match any pages. Try to be more specific in your request."
        engine.say(result[:300])
        engine.runAndWait()
        result="You: "+query+"\nMe: "+result
        text.delete(0.0,END)
        text.insert(0.0,result)

def Help():
    scr1=Tk()
    scr1.title("Help")
    scr1.geometry('630x160')
    scr1.resizable(0,0)
    lb = Listbox(scr1,width = 90,bg="black",fg="white",font=('Time','10','bold'))
    lb.insert(1, " Saturn is a Smart Assistant designed to interact users in both text and audio form.")
    lb.insert(2, " In order to use Saturn follow the following steps:")
    lb.insert(3, " Type text in the textarea and hit Enter button.")
    lb.insert(4, " To use audio service hit Voice button and speak.")
    lb.insert(5, " Try to use keywords or short sentences.")
    lb.insert(6, " Clear screen after every search.")
    lb.insert(7, " Common system errors will be notified, try to avoid it from next time.")
    lb.insert(8, " If some unknown error occurs kindly check your internet connection or restart the application.")
    lb.place(x=1,y=1)
