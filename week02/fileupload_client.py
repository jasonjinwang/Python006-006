#!/usr/bin/env python
import socket
import os,json,sys

HOST = 'localhost'
PORT = 10000

def fileupload_client():

    ''' fileupload Server 的 Client 端: '''
    ''' Usage: python fileupload_client.py <name>'''
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    fd = {}

    while True:
        # add file upload
        # {name:name,size:99999}
        if sys.argv[1]:
            
            if len(sys.argv) == 2:
                print('arg1 ->' + sys.argv[1])
                print('arg0 ->' + sys.argv[0])
                name = sys.argv[1].split('\\')[-1]
                fd['name'] = name
                fd['size'] = os.path.getsize(sys.argv[1])
            jsonString = json.dumps(fd).encode('utf-8')
            # 发送文件描述到服务端
            s.send(jsonString) 

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            size = 0
            with open(sys.argv[1],'rb') as file:
                while size < fd['size']:
                    fileDate = file.read(1024)
                    s.send(fileDate)
                    size += 1024
    s.close()

if __name__ == '__main__':
    fileupload_client()
