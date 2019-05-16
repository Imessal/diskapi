import base64
import hashlib
import socket
import ssl

PORT = 443
ADDRESS = 'webdav.yandex.ru'
LOGIN = ''
PASSWD = ''


def send_command(sock, command, buffer=1024):
    sock.send(command + b'\n')
    return sock.recv(buffer).decode()


def read_file(name):
    has_md5 = hashlib.sha256()
    file = b''
    with open(name, 'rb') as f:
        return f.read()


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock = ssl.wrap_socket(sock)
        sock.settimeout(3)
        sock.connect((ADDRESS, PORT))
        # print(sock.recv(1024).decode())
        log_pass = LOGIN+':'+PASSWD
        auth = base64.b64encode(log_pass.encode())
        rqst=('GET /ha.txt HTTP/1.1\n'
              'Host: webdav.yandex.ru\n'
              'Accept: */*\n'
              f'Authorization: Basic {auth.decode()}\n\n').encode()
        print(rqst)
        print(send_command(sock, rqst))

        put_rqst='Host: webdav.yandex.ru'
                 'Accept: */*'
                 f'Authorization: OAuth Basic {auth.decode()}'
                 f'Etag: {Etag}'
                 'Sha256: {Sha256}'
                 'Expect: 100 - continue'
                 'Content - Type: application / binary'
                 f'Content - Length: {size}'