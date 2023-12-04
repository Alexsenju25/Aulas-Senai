class Tarefa:
    def __int__(self, nome, data_vencimento):
        self.nome = nome
        self.data_vencimento = data_vencimento
        self.status = "Pendente"

    def marcar_concluida(self):
        self.status = "Concluída"

    def verificar_vencimento(self):

        data_tarefa = input("Digite a data da tarefa")
        if self.status == "Pendente" and self.data_vencimento <
            return f"A tarefa '{self.nome}' está atrasada."
        
        return f"A tarefa '{self.nome}' está em dia. "

tarefa1 = Tarefa("Passear com cachorro", "2023-10-17")

print(tarefa.verificar)

