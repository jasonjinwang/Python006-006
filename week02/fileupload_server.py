#!/usr/bin/env python
import socket
import json
import os
import sys
import inspect
from pathlib import *

HOST = 'localhost'
PORT = 10000


def fileupload_server():
    ''' Echo Server 的 Server 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)
    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')

        # 接收文件属性数据,创建文件
        jsonObj = json.loads(conn.recv(1024).decode('utf-8'))
        print('接收到数据', jsonObj)
        if not jsonObj:
            os.mknod(jsonObj['name'])
        msg = json.dumps({'name': '消息', '信号': '创建成功'})
        # 回数据确认已经建立新文件
        conn.send(msg.encode('utf-8'))

        # 接收数据
        size = 0
        sizeValue = int(jsonObj['size'])
        print('开始接收数据')
        # 获得python脚本的绝对路径
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path = os.path.dirname(os.path.abspath(filename))
        p = Path(path)
        pyfile_path = p.resolve().parent
        # 建立新的目录receivedFiles
        html_path = pyfile_path.joinpath('receivedFiles')

        if not html_path.is_dir():
            Path.mkdir(html_path)
        page = html_path.joinpath(jsonObj['name'])

        try:
            size = 0
            with open(page, 'wb') as file:
                while size < sizeValue:
                    value = sizeValue - size
                    if value > 1024:
                        getdate = conn.recv(1024)
                    else:
                        getdate = conn.recv(value)
                    file.write(getdate)
                    size += 1024
        except FileNotFoundError as e:
            print(f'文件无法打开,{e}')
        except IOError as e:
            print(f'读写文件出错,{e}')
        except Exception as e:
            print(e)
        
        print('结束')

        conn.close()
    s.close()


if __name__ == '__main__':
    fileupload_server()
