# _*_ coding: utf-8 _*_
import xml.dom.minidom
from SQLdb import  DbContext,Info


def readfile(filename, lines):
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip(' \n')
            if line.startswith('//') or len(line) == 0:
                continue
            lines.append(line)



def test_info():
    list = []
    minfo = Info.Machine_Info
    managerList = DbContext.dbSession(Info.Machine_Info.db).query(minfo.MachineSerialer).filter().limit(100)
    for i in managerList:
        list+=i
    return list



def createxml(managerList):

    # 在内存中创建一个空的文档
    doc = xml.dom.minidom.Document()
    # 创建一个根节点Managers对象
    root = doc.createElement('Root')
    # 将根节点添加到文档对象中
    doc.appendChild(root)

    #添加到根节点下
    Type=doc.createElement('Type')
    Type.appendChild(doc.createTextNode("Ascii"))
    root.appendChild(Type)

    Datas=doc.createElement('Datas')
    root.appendChild(Datas)



    for i in managerList:
        nodeData = doc.createElement('Data')
        nodeName = doc.createElement('Name')
        # 给叶子节点name设置一个文本节点，用于显示文本内容
        nodeName.appendChild(doc.createTextNode(i))

        nodeText = doc.createElement("Text")
        nodeText.appendChild(doc.createTextNode(i+"|01|01|02|00|F0|55"))



        # 将各叶子节点添加到父节点Manager中，
        # 最后将Manager添加到根节点Managers中
        nodeData.appendChild(nodeName)
        nodeData.appendChild(nodeText)
        Datas.appendChild(nodeData)
    # 开始写xml文档
    fp = open('D:\\sector.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


if __name__ == '__main__':
    SN=test_info()
    createxml(SN)