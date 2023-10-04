class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "quit":
                print("Ate mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido! Tente novamente.")


class MotoristaCRUD(SimpleCLI):
    def __init__(self, driver_model):
        super().__init__()
        self.driver_model = driver_model
        self.add_command("create", self.create_driver)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_driver)
        self.add_command("delete", self.delete_driver)

    def create_driver(self):
        nota = int(input("Entre com a nota:"))
        corrida = input("Entre com a corrida:")
        self.driver_model.create_driver(nota, corrida)

    def read_driver(self):
        id = input("Enter the id: ")
        driver = self.driver_model.read_driver_by_id(id)
        if driver:
            print(f"Titulo: {driver['titulo']}")
            print(f"Autor: {driver['autor']}")
            print(f"Ano: {driver['ano']}")
            print(f"Preco: {driver['preco']}")

    def update_driver(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o novo titulo: ")
        autor = input("Entre com o novo autor: ")
        ano = int(input("Entre com o novo ano: "))
        preco = float(input("Entre com novo o preco: "))
        self.driver_model.update_driver(id, titulo, autor, ano, preco)

    def delete_driver(self):
        id = input("Entre com o id: ")
        self.driver_model.delete_driver(id)
        
    def run(self):
        print("Bem vindo ao driverCRUD!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()
        