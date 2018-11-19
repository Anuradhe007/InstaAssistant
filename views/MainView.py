from tkinter import *
import time
import sys

def handleStartBtn():
    pwd1 = ents[0][1].get().strip()
    uname1 = ents[1][1].get().strip()
    uname2 = ents[2][1].get().strip()
    uname3 = ents[3][1].get().strip()
    uname4 = ents[4][1].get().strip()
    uname5 = ents[5][1].get().strip()
    uname6 = ents[6][1].get().strip()
    uname7 = ents[7][1].get().strip()
    uname8 = ents[8][1].get().strip()
    uname9 = ents[9][1].get().strip()
    uname10 = ents[10][1].get().strip()
    uname11 = ents[11][1].get().strip()

    time1 = ents[12][1]
    proxy = ents[13][1]
    file = ents[14][1]

    credentials = dict()

    for key in ents:
        print(key)


def startBtnClick():
    handleStartBtn()

def handleStopBtn():
    sys.exit()

def makeform(root):
    entries = []
    for field in range(1, 18):
        row = Frame(root)
        row.pack(side=TOP, padx=5, pady=2)
        if field == 1:
            userNameLab = Label(row, text="Username", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            passwordLab = Label(row, text="Password", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            userNameLab.pack(side=LEFT)

            passworsEnt = Entry(row, width=40, show="*")
            entries.append(('password' + str(field), passworsEnt))
            userNameEnt = Entry(row, width=40)
            entries.append(('username' + str(field), userNameEnt))
            passworsEnt.pack(side=RIGHT, fill=X)
            passwordLab.pack(side=RIGHT)
            userNameEnt.pack(side=LEFT, fill=X)

        if (1 < field) and (field < 12):
            userName = "Username "+str(field-1)
            userNameLab = Label(row, text=userName, fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            userNameLab.pack(side=LEFT)

            userNameEnt = Entry(row, width=40)
            entries.append(('username' + str(field), userNameEnt))
            userNameEnt.pack(side=LEFT, fill=X)

        if field == 13:
            timeLab = Label(row, text="Time", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            timeLab.pack(side=LEFT)
            timeEnt = Entry(row, width=60)
            timeEnt.pack(side=RIGHT, fill=X)
            entries.append(('time' + str(field), timeEnt))

        if field == 14:
            proxyLab = Label(row, text="Proxy", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            proxyLab.pack(side=LEFT)
            proxyEnt = Entry(row, width=60)
            proxyEnt.pack(side=RIGHT, fill=X)
            entries.append(('proxy' + str(field), proxyEnt))

        if field == 15:
            filesLab = Label(row, text="Files", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
            filesLab.pack(side=LEFT)
            filesEnt = Entry(row, width=60)
            filesEnt.pack(side=RIGHT, fill=X)
            entries.append(('files' + str(field), filesEnt))

        if field == 16:
            b1 = Button(window, text='Start', command=startBtnClick)
            b1.pack(side=RIGHT, padx=5, pady=2)
            # b2 = Button(window, text='Stop', command=handleStopBtn)
            # b2.pack(side=RIGHT, padx=5, pady=2)

    return entries

window = Tk()
window.configure(background="#a1dbcd")
window.title("InstaAssistant")
photo = PhotoImage(file="insta-client-logo.gif")
logo = Label(window, image=photo)
logo.pack(side=TOP)

ents = makeform(window)

window.mainloop()