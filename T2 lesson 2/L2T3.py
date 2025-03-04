class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip

class Server:

    ip_counter = 1

    def __init__(self, router):
        self.Buffer = []
        self.ip = Server.ip_counter
        Server.ip_counter += 1
        self.router = router
        router.link(self)

    def send_data(self, data: Data):
        self.Buffer.append(data)
        self.router.adding_data(data)

    def get_data(self):
        adding_data = self.Buffer
        self.Buffer = []
        return adding_data

    def get_ip(self):
        return self.ip

class Router:

    def __init__(self):
        self.Buffer = []
        self.server = []
    
    def link(self, server: Server):
        self.server.append(server)

    def unlink(self, server: Server):
        self.server.remove(server)

    def adding_data(self, data: Data):
        self.Buffer.append(data)

    def send_data(self):
        for data in self.Buffer:
            for server in self.server:
                if server.get_ip == data.ip:
                    server.Buffer.append(data)
        self.Buffer.clear()