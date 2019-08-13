#coding:utf-8
import socket,time,threading
from SQLdb import  DbContext,Info

list=['756e62b971cf550d','ec3a7f52bf798572','ce61aebabd9dd82e','ed4047d57f27c107','5a832f67f4e73df2','4fb37695649167c1']

exec_count = 0
def heart_beat():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('94.191.97.65', 30670))
    s.send(b'756e62b971cf550d|01|01|02|00|F0|55')
    time.sleep(15)
    global exec_count
    exec_count += 1
    # 15秒后停止定时器
    if exec_count < 360:
        threading.Timer(10, heart_beat).start()





BUFSIZ=1024
def tcpclient():
    a = 0
    while True:
        time.sleep(10)
        a += 1
        s = socket.socket()
        s.connect(('94.191.97.65', 30670))
        info = Info.Machine_info
        db = DbContext.dbSession(info.db).query(info).filter(info.MachineCode != 'M31395').order_by(info.Created.desc()).limit(10)
        for sn in db:
            s.send(bytes( sn.MachineSerialer+ '|01|01|02|00|F0|55', encoding='utf-8'))
            data = s.recv(BUFSIZ)  # 接收回应消息，接收到的是字节数组
            if not data:  # 如果接收服务器信息失败，或没有消息回应
                break
            print(data.decode('utf-8'))
        keepclass = "我已连接" + str(a * 10) + "秒"
        print(keepclass)



def tcptest():
    a = 0
    while True:
        time.sleep(10)
        a += 1
        s = socket.socket()
        s.connect(('94.191.97.65', 30670))
        info = Info.Machine_info
        db = DbContext.dbSession(info.db).query(info).filter(info.MachineCode != 'M31395').order_by(info.Created.desc()).limit(10)
        for sn in db:
            s.send(bytes( sn.MachineSerialer+ '|01|01|02|00|F0|55', encoding='utf-8'))
            data = s.recv(BUFSIZ)  # 接收回应消息，接收到的是字节数组
            if not data:  # 如果接收服务器信息失败，或没有消息回应
                break
            print(data.decode('utf-8'))
        keepclass = "我已连接" + str(a * 10) + "秒"
        print(keepclass)


tcptest()


