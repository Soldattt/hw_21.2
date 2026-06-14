
from http.server import BaseHTTPRequestHandler, HTTPServer




hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('paje_4.html', 'r', encoding='UTF-8') as f:
            html_contacts = f.read()
        self.wfile.write(bytes(html_contacts, "utf-8")) # Тело ответа

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C

        pass


    webServer.server_close()
    print("Server stopped.")
