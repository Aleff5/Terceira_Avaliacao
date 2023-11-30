from datetime import datetime

import random


def gerarNumero(): # função que gera numero da conta
    return random.randint(100000, 999999)

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = str(nome)
        self.cpf = str(cpf)
        

    def grava(self):
        with open("DadosClientes.txt", "a") as arquivo:
            arquivo.write(f"Nome: {self.nome}, CPF: {self.cpf};\n")
            print('Gravado com sucesso ')

    def lerDados(self):
        try:
            with open("DadosClientes.txt", 'r') as arquivo:
                conteudo = arquivo.read()
                print("Arquivo lido com sucesso!")
                return conteudo
        except FileNotFoundError:
            return "ERROR: Arquivo não encontrado"

    def imprime(self):
        try:
            with open("DadosClientes.txt", 'r') as arquivo:
                conteudo = arquivo.read()
                if not conteudo:
                    print('Arquivo vazio')
                else:
                    print(conteudo)
        except FileNotFoundError:
            return "ERROR: Arquivo não encontrado"


class Historico:
    def __init__(self):
        
        self.transacoes = []

    def registrar_transacao(self, numeroConta, tipo, valor):
        datahora = datetime.now()
        transacao = f'Numero da conta : {numeroConta}.\nDescrição : {tipo}.\nHorário : {datahora}.\nValor : R${valor}\n'
        self.transacoes.append(transacao)

    def gravar_arquivo(self):
        with open('historicoContas.txt', 'w') as arquivo:
            arquivo.write("Histórico de Transações:\n")
            for transacao in self.transacoes:
                arquivo.write(transacao + '\n')

    def ler_arquivo(self):
        try:
            with open('HistoricoContas.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                print("Histórico lido com sucesso!")
                return conteudo
        except FileNotFoundError:
            print("ERROR: Arquivo de histórico não encontrado")
            return None

        
    def imprimir_arquivo(self):
        try:
            with open('historicoContas.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                if not conteudo:
                    print('Histórico vazio')
                else:
                    print(conteudo)
        except FileNotFoundError:
            print("ERROR: Arquivo de histórico não encontrado")


class Conta:
    def __init__(self, cliente, numero_da_conta, data_abertura):
        self.cliente = cliente
        self.numero = numero_da_conta
        self.data_abertura = data_abertura
        self.saldo_da_conta = 0
        self.historico = Historico()

    def gravaDados(self):
        with open('DadosConta.txt', 'a') as arquivo:
            arquivo.write(f'Conta número: {self.numero}.\nData de abertura: {self.data_abertura}.\nSaldo atual: {self.saldo_da_conta}.\n')

    def lerDados(self): #LER OS DADOS DO ARQUIVO
        try:
            with open('DadosConta.txt', 'r') as arquivo:
                print("Arquivo lido com sucesso!")
                return arquivo
        except FileNotFoundError:
            return "ERROR: Arquivo não encontrado"

    def imprime(self):
        with open('DadosConta.txt', 'r') as arquivo:
            conteudo = arquivo.read()

            if not conteudo: #caso n tenha nadaa no arquivo
                print("Arquivo vazio")
            else:
                print(conteudo)

    def depositar(self, valor):
        self.saldo_da_conta += valor
        self.historico.registrar_transacao(self.numero,'Deposito', valor)#envia a transaçao para o historico
        self.gravaDados()#grava os dados da conta

    def sacar(self, valor):
        if self.saldo_da_conta <= valor:
            return "Ação indisponível. Saldo insuficiente."
        else:
            self.saldo_da_conta -= valor
            self.historico.registrar_transacao(self.numero,'Saque', valor)#envia a transaçao para o historico
            self.gravaDados()#grava os dados da conta

    def movimentacao(self, outraConta, valor):
        if self.saldo_da_conta <= valor:
            print("Ação indisponível. Saldo insuficiente.")
        else:
            self.saldo_da_conta -= valor
            outraConta.depositar(valor)
            self.historico.registrar_transacao(self.numero,'Transferência',valor)#envia a transaçao para o historico
            print(f"Transferência de {valor} para a conta {outraConta.numero} foi realizada com sucesso.")
            self.gravaDados()#grava os dados da conta





# data atual
data_atual = datetime.now()

# teste da classe "cliente"
cliente = Cliente('nome1', 'cpf1')
cliente_2 = Cliente('nome2', 'cpf2')

cliente.grava()
cliente.lerDados()
cliente.imprime()
cliente_2.grava()
cliente_2.lerDados()
cliente_2.imprime()

# teste da classe Conta
conta = Conta(cliente, gerarNumero(), data_atual)
conta_2 = Conta(cliente_2, gerarNumero(), data_atual)

conta.gravaDados()
conta.lerDados()
conta.imprime()

print(20*'=')
# teste das ações
conta.depositar(10000)
conta.sacar(5000)
conta.imprime()

print(20*'=')

conta_2.gravaDados()
conta_2.lerDados()
conta_2.imprime()

print(20*'=')
# teste das ações
conta_2.depositar(10000)
conta_2.sacar(5000)
conta_2.imprime()

print(20*'=')

conta.movimentacao(conta_2, 2000) #transfere 2000 da conta 1 para a conta 2
conta.imprime()
conta_2.imprime()

print(20*'=')

# Teste Historico

conta.historico.gravar_arquivo()
conta.historico.ler_arquivo()
conta.historico.imprimir_arquivo()
