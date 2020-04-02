import asyncio
import os
import websockets
import time
import base64
#from uuid import uuid4
#import logging

user_list=["lisomn","ghost","yellow"]

ues_bs=":&*"
#连接用户列表
chatRegister={}
chatname={}
log_path=os.getcwd()+"\\log"
if not os.path.exists(log_path):
    os.mkdir(log_path)
glb_time=str(int(time.time()))

#uuid_list={}
def de_log(mess):
    flog=open(log_path+"\\"+glb_time+"_py.log","a")
    flog.write(mess)
    flog.close
    
def make_message(name,text,say_type):
    response_time = str(int(time.time()))
    response_name = name
    response_id = str(base64.b64encode(response_name.encode("utf-8")))
    response_text = text
    response_data_id = str(base64.b64encode(response_text.encode("utf-8")))
    response_type = say_type
    return response_time+ues_bs+response_id+ues_bs+response_name+ues_bs+response_data_id+ues_bs+response_text+ues_bs+response_type

async def check_permit(websocket):
    while True:
        recv_str = await websocket.recv()
        if recv_str != "":
            response_str = "congratulation, you have connect with server\r\nnow, you can do something else"
            await websocket.send(response_str)
            remote_info=str(websocket.remote_address[0])+str(websocket.remote_address[1])
            chatRegister[remote_info]=websocket
            chatname[remote_info]=recv_str
            de_log(str(time.time())+"|"+remote_info+"|"+"连接\n")
            for i in chatRegister.keys():
               send_socket=chatRegister[i]
               await send_socket.send(make_message(recv_str,"123","join"))
            print(remote_info+"连接\n")
            return True
        else:
            response_str = "sorry, the username or password is wrong, please submit again"
            print("error 用户名:"+recv_str+"\n")
            await websocket.send(response_str)

# 接收客户端消息并处理,message
async def recv_msg(websocket):
    remote_info=str(websocket.remote_address[0])+str(websocket.remote_address[1])
    try:
        while True:
            recv_text = await websocket.recv()
            get_message=recv_text.split(":")
            
            user=get_message[0]
            user_message=get_message[1]
            
            de_log(str(time.time())+"|"+remote_info+"|"+recv_text+"|"+"消息\n")
            for i in chatRegister.keys():
               send_socket=chatRegister[i]
               await send_socket.send(make_message(user,user_message,"message"))
    except:
        print(remote_info+"连接断开\n")
        del chatRegister[remote_info]
        de_log(str(time.time())+"|"+remote_info+"|"+"断开\n")
        for i in chatRegister.keys():
            send_socket=chatRegister[i]
            await send_socket.send(make_message(chatname[remote_info],"123","exit"))
        del chatname[remote_info]
        


# 服务器端主逻辑
async def main_logic(websocket, path):
    await check_permit(websocket)

    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '', 24258)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
