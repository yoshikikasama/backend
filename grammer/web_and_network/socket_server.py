"""
ウェルノウンポート番号 (0-1023)
登録済みポート番号 (1024-49151)
動的・プライベートポート番号(49152-65535)
"""
import socket

# TCP通信
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     # 1接続
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         # 接続が終わったら閉じるためのwith文
#         with conn:
#             while True:
#                 # ネットワークのバッファサイズが1024のため
#                 data = conn.recv(1024)
#                 if not data:
#                    break
#                 print(f'data: {data}, addr: {addr}')
#                 # clinetにmessageを返す
#                 conn.sendall(b'Received: ' + data)

# UDP通信
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print(f'data: {data}, addr: {addr}')