import socket
import threading
import zm_homepage
import zm_chatroom
host=''
port=80
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(128)

def read_from_client(s):
    try:
        return s.recv(1024).decode('utf-8')
    except:
        s.close
        
def server_target(s):
    try:
        while True:
            recv_data=read_from_client(s)
            if recv_data:
                arry_data=recv_data.split()
                page_recv_data = recv_data.split()[1]
                if page_recv_data == "/favicon.ico":
                    s.close()
                    raise "favicon"
                print('请求的资源路径为：', page_recv_data)
                real_recv_page = page_recv_data
                if arry_data[0] == "POST" and page_recv_data == "/chat":
                    if "name=" in arry_data[-1] and "login=ENTER" in arry_data[-1]:
                        print(f"{arry_data[-1]}\n")
                        chat_info=arry_data[-1].split("&")[0].split("=")[1]
                        print(f"登录用户{chat_info}\n")
                if real_recv_page in ["/app.css","/cont.js"]:
                    data = f'web{real_recv_page}'
                    print("data:"+data)
                    with open(data, 'rb') as file:
                        page_data = file.read()
                    http_line = 'HTTP/1.1 / 200 ok\r\n'
                    http_header = 'Server: PWS/1.0\r\n'
                    send_data = (http_line + http_header + '\r\n').encode() + page_data
                    s.send(send_data)
                if real_recv_page == "/chat":
                    if arry_data[0] == "GET":
                        page_data=zm_homepage.get_homepage().encode()
                    elif arry_data[0] == "POST":
                        page_data=zm_chatroom.get_chatpage(chat_info).encode()
                    http_line = 'HTTP/1.1 / 200 ok\r\n'
                    http_header = 'Server: PWS/1.0\r\n'
                    send_data = (http_line + http_header + '\r\n').encode() + page_data
                    s.send(send_data)
                s.close()
    except IOError as e:
        print(e.strerror)
        


if __name__ == '__main__':
    while True:
        client_socket, ip_port = server_socket.accept()
        threading.Thread(target=server_target,args=(client_socket,)).start()