import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("客户端1")
win.geometry("400x400+200+20")

ck = None#用于储存客户端的信息

def getInfo():
    """接收服务器的消息并在GUI展示"""
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT, data.decode("utf-8"))

def sendMail():
    '''发送指定格式的消息(带发送者名称)'''
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr
    ck.send(sendStr.encode("utf-8"))

def connectServer():
    """客户端套接字服务"""
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    client.send(userStr.encode("utf-8"))
    ck = client #?

    t = threading.Thread(target=getInfo)  # 多线程因为收取多个其他客户端发送的消息
    t.start()

"""GUI"""
labelUse = tkinter.Label(win, text="userName").grid(row=0, column=0)

euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win, text="ip").grid(row=1, column=0)

eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)

eport = tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="启动", command=connectServer).grid(row=3, column=0)

text = tkinter.Text(win, height=5, width=30).grid(row=4, column=1)
labeltext= tkinter.Label(win, text="显示消息").grid(row=4, column=0)

labelesend = tkinter.Label(win, text="发送的消息").grid(row=5, column=0)
esend = tkinter.Variable()
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=1)

labelefriend= tkinter.Label(win, text="发给谁").grid(row=6, column=0)
efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win, text="发送", command=sendMail).grid(row=7, column=0)

win.mainloop()
