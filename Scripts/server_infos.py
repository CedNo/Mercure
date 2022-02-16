from simple_websocket_server import WebSocketServer, WebSocket

class GestionIOT(WebSocket):
    def handle(self):
        donnees = self.data
        print(donnees)
        if donnees == "PowerOn":
           print("POWER ON")

        if donnees == "PowerOff":
           print("POWER OFF")

        if donnees == "TEST":
            print(clients)
            for client in clients:
                if client != self:
                    client.send_message('TEST')

    def connected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handle_close(self):
        print(self.address, 'closed')
        clients.remove(self)

clients = []

server = WebSocketServer('', 65000, GestionIOT)
print('En attente de connexion')
server.serve_forever()
    
