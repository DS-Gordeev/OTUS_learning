import socket
from http import HTTPStatus

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    srv_addr = ('172.20.160.1', 5000)
    s.bind(srv_addr)
    s.listen(1)

    while True:
        print('Waiting for a connection...')

        conn, addr = s.accept()
        recv_bytes = conn.recv(1024)
        print(conn, addr)

        if not recv_bytes:
            print('Closing connection...')
            conn.close()

        text = recv_bytes.decode('utf-8')
        print(f'Message received: {text}')

        status_line = 'HTTP/1.1 200 OK'
        req_method = text.split('\n')[0].split(' ')[0]
        status = text.split('\n')[0].split(' ')[1]
        headers_list = text.split('\n')[1:]
        print(type(headers_list[-1]))
        heads = '\n'.join((lambda x: [f'<p>Header-name: {i}</p>' for i in x if i != ''])(headers_list))

        try:
            status_code = HTTPStatus(int(status.split('=')[1]))
        except (ValueError, IndexError):
            status_code = HTTPStatus(200)

        body = '<h1>Hello from OTUS!</h1>' \
        f'<p>Request Method: {req_method}</p>' \
        f'<p>Response Status: {status_code.value, status_code.name}</p>' \
        f'<p>Request Source: {addr}</p>' \
        f'{heads}'

        headers = '\r\n'.join([status_line, 'Content-Type: text/html', f'Content-Lenght: {len(body)}'])
        resp = '\r\n\r\n'.join([headers, body])
        sent_bytes = conn.send(resp.encode('utf-8'))
