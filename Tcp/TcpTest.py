#coding:utf-8
import socket,time,threading
from SQLdb import  DbContext,Info
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from multiprocessing import Process,Pool

lock = threading.Lock()
BUFSIZ=1024
def tcpclient():
    a = 0
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    info = Info.Machine_Info
    db = DbContext.dbSession(info.db).query(info).filter(info.MachineType==1).order_by(info.Created.desc()).limit(10)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        a += 1
        for sn in db:
            s.connect(('94.191.97.65', 30670))
            s.send(bytes('(' + sn.MachineSerialer + '|01|01|02|00|F0|55)', encoding='utf-8'))
            data = s.recv(BUFSIZ)  # 接收回应消息，接收到的是字节数组
            if not data:  # 如果接收服务器信息失败，或没有消息回应
                break
            print(data.decode('utf-8'))
        keepclass = "我已连接" + str(a * 10) + "秒"
        print(keepclass)
        time.sleep(10)

#249服务器TCP连接配置：   tcp.hk.zjgx188.com:30670
#测试环境TCP连接配置： 94.191.97.65:30670
def tcptest(sn):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('94.191.97.65', 30670))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            while True:
                try:
                    s.send(bytes('('+sn + '|01|01|02|00|F0|55)', encoding='utf-8'))
                    print('发送消息:' + '('+sn + '|01|01|02|00|F0|55)')
                    time.sleep(30)
                except:
                    print(exec())
                    time.sleep(1)




def tcp_thread(sn_number,machinetype):
    info = Info.Machine_Info
    db = DbContext.dbSession(info.db).query(info).filter(
        info.MachineType == machinetype and info.MachineCode != 'M30944').order_by(info.Created.desc()).limit(sn_number)
    for i in db:
        lock.acquire()
        try:
            th=threading.Thread(target=tcptest, args=(i.MachineSerialer,))
            th.start()
        finally:
            lock.release()






#
# if __name__=='__main__':
#     p = Pool()
#     info = Info.Machine_Info
#     db = DbContext.dbSession(info.db).query(info).filter(info.MachineType == 1 and info.MachineCode!='M30944').order_by(info.Created.desc()).limit(30)
#     for i in db:
#         p.apply_async(tcptest, args=(i.MachineSerialer,))
#     time.sleep(300)
#     # p.close()
#     # p.join()


#tcptest('d55321a189218531')


