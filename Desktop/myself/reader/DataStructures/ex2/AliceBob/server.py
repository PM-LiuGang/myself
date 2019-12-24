import tkinter
import socket, threading

win = tkinter.Tk()  
win.title('模拟服务器')
win.geometry("400x400+200+20")
users = {}

def run(ck, ca):
    """
    接收客户发过来的信息
    :param ck: 新的套接字对象
    :param ca: 连接的客户端地址
    :return:
    """
    userName = ck.recv(1024)  # 接收发送人的名称
    users[userName.decode("utf-8")] = ck  # 储存发送者的名称,对套接字引用
    
    printStr = "" + userName.decode("utf-8") + "连接\n"
    text.insert(tkinter.INSERT, printStr)

    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")  # b'' -> ''
        infolist = dataStr.split(":")  #friend:sendStr
        users[infolist[0]].send((userName.decode("utf-8") + "说" + infolist[1]).encode("utf"))

def start():
    '''启动服务端服务'''
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)
    printStr = "服务器启动成功\n"
    text.insert(tkinter.INSERT, printStr)
    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))
        t.start()

def startSever():
    '''启动(服务端)线程'''
    s = threading.Thread(target=start)
    s.start()
    # start() # 必须线程，否则报错，为什么？

labelIp = tkinter.Label(win, text='ip').grid(row=0, column=0)
labelPort = tkinter.Label(win, text='port').grid(row=1, column=0)

eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)

button = tkinter.Button(win, text="启动", command=startSever).grid(row=2, column=0)

text = tkinter.Text(win, height=5, width=30)
text.grid(row=3, column=1)  # 放在上面一行，不报错，但是text is None

labeltext = tkinter.Label(win, text='连接消息').grid(row=3, column=0)

win.mainloop()
