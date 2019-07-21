from tkinter import*
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
from mutagen.mp3 import MP3
import os
import time
from time import sleep
import threading

class music:
    def __init__(self,master):
        mixer.init()                #initializition of mixer
        self.total_length=0
        self.c=0
        self.g=0
        self.t=0
        self.new=100
        self.master = master
        self.master.title("Moon Music")
        self.master.configure(background="skyblue")  

        self.master.iconbitmap(r'F:\python\hello\new\Allinone\png\ty.ico')
        self.master.geometry("600x450")
        self.master.resizable(width=False, height=False)
        self.p1=PhotoImage(file=r"F:\python\hello\new\Allinone\png\play-button.png")
        self.p2=PhotoImage(file=r"F:\python\hello\new\Allinone\png\list.png")        
        self.p3=PhotoImage(file=r"F:\python\hello\new\Allinone\png\pre.png")
        self.p4=PhotoImage(file=r"F:\python\hello\new\Allinone\png\next.png")
        self.p5=PhotoImage(file=r"F:\python\hello\new\Allinone\png\pause.png")
        self.p6=PhotoImage(file=r"F:\python\hello\new\Allinone\png\mute.png")
        self.p7=PhotoImage(file=r"F:\python\hello\new\Allinone\png\unmute.png")
        self.p8=PhotoImage(file=r"F:\python\hello\new\Allinone\png\rewind.png")
        self.p9=PhotoImage(file=r"F:\python\hello\new\Allinone\png\play.png")
        self.p10=PhotoImage(file=r"F:\python\hello\new\Allinone\png\minus.png")
        self.p11=PhotoImage(file=r"F:\python\hello\new\Allinone\png\plus.png")
        self.p12=PhotoImage(file=r"F:\python\hello\new\Allinone\png\stop.png")








        self.l2=Label(self.master, text="MOON MUSIC", font = "Helvetica 30 bold italic", bg="skyblue").place(x=160,y=0)
        
        self.b1=Button(self.master, image =self.p1, command = self.pauseresume, bg="skyblue" ,border="0", activebackground="skyblue")
        self.b1.place(x=40,y=50)

        self.b2=Button(self.master, bg="skyblue",image=self.p2, border="0", activebackground="skyblue",command=self.open)
        self.b2.place(x=10,y=380)

        self.b3=Button(self.master, bg="skyblue",image=self.p3, border="0", activebackground="skyblue", command=self.pre)
        self.b3.place(x=80,y=380)

        self.b4=Button(self.master, bg="skyblue",image=self.p4, border="0", activebackground="skyblue", command=self.next)
        self.b4.place(x=150,y=380)

        self.b5=Button(self.master, bg="skyblue", border="0",image=self.p8, activebackground="skyblue",command=self.rewind)
        self.b5.place(x=220,y=380)

        self.b6=Button(self.master, bg="skyblue", border="0",image=self.p7, activebackground="skyblue",command=self.mute)
        self.b6.place(x=360,y=380)

        
        self.b7=Button(self.master, bg="skyblue", border="0",image=self.p11, activebackground="skyblue",command=self.open)
        self.b7.place(x=340,y=240)

        self.b8=Button(self.master, bg="skyblue", border="0",image=self.p10, activebackground="skyblue",command=self.delsong)
        self.b8.place(x=480,y=240)

        self.b9=Button(self.master, bg="skyblue", border="0",image=self.p9, activebackground="skyblue",command=self.play)
        self.b9.place(x=410,y=240)

        self.b10=Button(self.master, bg="skyblue", border="0",image=self.p12, activebackground="skyblue",command=self.stop_music)
        self.b10.place(x=290,y=380)


        self.ll1=IntVar()
        self.l1=Label(self.master,textvariable=self.ll1,bg="skyblue").place(x=340,y=40,width=210)
        self.ll1.set('playing music')

        self.ll2=IntVar()
        self.l2=Label(self.master, textvariable=self.ll2).place(x=550,y=290,width=50)
        self.ll2.set('00:00')

        self.ll3=IntVar()
        self.l3=Label(self.master,textvariable=self.ll3, text='Current Time').place(x=0,y=290,width=50)
        self.ll3.set('00:00')


        
        self.s2=Scale(self.master, from_=0,to=self.new, resolution=1, orient=HORIZONTAL, bg="skyblue")
        self.s2.place(x=0,y=310,width=600,height=65)
        self.s2.set(self.t)

        self.s1=Scale(self.master, from_=0,to=100, resolution=10, orient=HORIZONTAL,command=self.vol, bg="skyblue")
        self.s1.place(x=430,y=380,width=160,height=65)
        self.s1.set(20)
        self.vol(20)

        self.playlistbox = Listbox(self.master,bg="skyblue",border=0)
        self.playlistbox.place(x=340,y=60,width=210,height=170)




        self.master.protocol("WM_DELETE_WINDOW", lambda arg=self.master: self.onclosing(arg))

      

        self.mute=0
        self.playlist =[]

        
        

    def mute(self):
        if (self.mute==0):
            self.u=self.s1.get()
            mixer.music.set_volume(0)
            self.s1.set(0)
            self.mute=1
            self.b6.config(image=self.p6)

            

            
        else:
            self.s1.set(self.u)
            self.vol(self.u)
            self.mute=0
            self.b6.config(image=self.p7)


    def vol(self,con):
        self.con=int(con)/100
        mixer.music.set_volume(self.con)

    def open(self):
        global f
        f = filedialog.askopenfilename()

        self.add_to_playlist(f)

    
    def add_to_playlist(self,f5):
        global f
        self.f5=f5
        self.f5 = os.path.basename(self.f5)
        self.index = 0
        self.playlistbox.insert(self.index, self.f5)
        self.playlist.insert(self.index, f)
        self.index += 1
        

    def rewind(self):
        self.play()

    def stop_music(self):
        mixer.music.stop()


    def pauseresume(self):
        if(self.g==0):
            self.g=1
            mixer.music.pause()
            self.b1.config(image=self.p1)

        elif(self.g==1):
            self.g=0
            mixer.music.unpause()
            self.b1.config(image=self.p5)

    def play(self):
        try:
            self.stop_music()
            time.sleep(1)   
            selected_song1 = self.playlistbox.curselection()
            self.selected_song = int(selected_song1[0])
            self.play_it = self.playlist[self.selected_song]
            f=self.play_it
            mixer.music.load(f)
            mixer.music.play() 
            self.b1.config(image=self.p5)
            self.showtime(f)

        except:
            tkinter.messagebox.showinfo("ABOUT MOON MUSIC","PLEASE CLICK THE SONG FROM LIST")

    def showtime(self,f9):
        t="playing"+"-"+os.path.basename(f9)
        self.ll1.set(t)
        file = os.path.splitext(f9)

        if (file[1]=='.mp3'):
            audio=MP3(f9)
            self.total_length= audio.info.length

        else:
            a=mixer.Sound(f9)
            self.total_length=a.get_length()

        self.new=self.total_length
        self.s2.config(to=self.new)
        mins, secs=divmod(self.total_length,60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.ll2.set(timeformat)
  



        self.t1 = threading.Thread(target=self.loop)
        self.t1.start()

        
        
    def loop(self):
        self.t=0

        while (self.t<=self.total_length and mixer.music.get_busy()):
            if (self.g == 1):
                continue
            else:
                mins, secs=divmod(self.t,60)
                mins = round(mins)
                secs = round(secs)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                self.ll3.set(timeformat)
                time.sleep(1)
                self.t=self.t+1
                self.s2.set(self.t)



    def onclosing(self,new):
        self.stop_music()
        new.destroy()

    def delsong(self):
        selected_song = self.playlistbox.curselection()
        selected_song = int(selected_song[0])
        self.playlistbox.delete(selected_song)
        self.playlist.pop(selected_song)
        
    def next(self):
        self.stop_music()
        time.sleep(1) 
        self.selected_song=self.selected_song +1
        self.play_it = self.playlist[self.selected_song]
        f=self.play_it
        mixer.music.load(f)
        mixer.music.play() 
        self.b1.config(image=self.p5)
        self.showtime(f)


    def pre(self):
        self.stop_music()
        time.sleep(1) 
        self.selected_song=self.selected_song -1
        self.play_it = self.playlist[self.selected_song]
        f=self.play_it
        mixer.music.load(f)
        mixer.music.play() 
        self.b1.config(image=self.p5)
        self.showtime(f)

        

root=Tk()
s=music(root)
mainloop()
