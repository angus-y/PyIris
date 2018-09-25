import socket
import PIL
import uuid
import pickle


def main(sock):
    sock.settimeout(None)
    data = sock.recv(999999)
    sock.settimeout(2)
    while True:
        try:
            tmp_data = sock.recv(999999)
            if not tmp_data:
                raise socket.error
            data += tmp_data
        except (socket.error, socket.timeout):
            if data.startswith('png:'):
                data = data[4:]
                img = pickle.loads(data)
                id = str(uuid.uuid4())
                img.save(id+'.png', 'PNG')
                return 'Your data was an image!'
            else:
                return data
