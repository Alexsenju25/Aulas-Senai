class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato is not None:
            self.contatos.remove(contato)
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

# Função principal para interagir com a agenda de contatos
def main():
    minha_agenda = Agenda()

    while True:
        print("\nOpções:")
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            novo_contato = Contato(nome, telefone, email)
            minha_agenda.adicionar_contato(novo_contato)
            print("Contato adicionado com sucesso.")

        elif opcao == '2':
            print("Lista de Contatos:")
            minha_agenda.listar_contatos()

        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja buscar: ")
            contato = minha_agenda.buscar_contato(nome)
            if contato:
                print("Contato encontrado:")
                print(contato)
            else:
                print(f"Contato {nome} não encontrado na agenda.")

        elif opcao == '4':
            nome = input("Digite o nome do contato que deseja remover: ")
            minha_agenda.remover_contato(nome)

        elif opcao == '5':
            print("Encerrando a aplicação.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
