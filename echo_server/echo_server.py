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

        text = recv_bytes.decode('utf-8')
        print(f'Message received: {text}')

        # Получаем метод  --> GET
        req_method = text.split('\n')[0].split(' ')[0]

        # Получаем статус  --> / или /?status=404
        status = text.split('\n')[0].split(' ')[1]

        # Получаем список всех заголовков (берем все кроме первой)  -->
        # ['Host: 192.168.1.3:5000\r', 'Connection: keep-alive\r', ...]
        headers_list = text.split('\n')[1:]

        # Убираем символ \r перевода каретки из конца каждого элемента списка -->
        # ['Host: 192.168.1.3:5000', 'Connection: keep-alive', ...]
        cleaned_list = [item.replace('\r', '') for item in headers_list]

        # При помощи лямбда-функции формируем список строк-заголовков и джойним их в одну строку
        heads_to_body = '\n'.join((lambda x: [f'<p>Header-name: {i}</p>' for i in x if ':' in i])(cleaned_list))
        print(heads_to_body)

        # Создаем объект httpStatus с кодом из параметра запроса /?status=404  --> 404
        try:
            status_code = HTTPStatus(int(status.split('=')[1]))
        # В случае если статус ошибочный (ValueError) или endpoint без параметра статуса (IndexError) - присваиваем 200
        except (ValueError, IndexError):
            status_code = HTTPStatus(200)

        body = '<h1>Hello from OTUS!</h1>' \
               f'<p>Request Method: {req_method}</p>' \
               f'<p>Response Status: {status_code.value, status_code.name}</p>' \
               f'<p>Request Source: {addr}</p>' \
               f'{heads_to_body}'

        status_line = 'HTTP/1.1 200 OK'
        headers = '\r\n'.join([status_line, 'Content-Type: text/html', f'Content-Lenght: {len(body)}'])
        resp = '\r\n\r\n'.join([headers, body])
        sent_bytes = conn.send(resp.encode('utf-8'))

        # Закрываем соединение
        print('Closing connection...')
        conn.close()
