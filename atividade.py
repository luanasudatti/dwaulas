from conta_bancaria import ContaBancaria, SaldoInsuficienteError

# Criando as três contas (saldo inicial vem de um depósito, pois toda conta começa com 0,00)
conta1 = ContaBancaria ('123', 'Ana Lima')
conta2 = ContaBancaria ('456', 'Carlos Souza')
conta3 = ContaBancaria ('789', 'Maria Silva')

conta1.depositar(500)
conta2.depositar(300)
conta3.depositar(100)


def mostrar_saldos(titulo):
    print(f"\n--- {titulo} ---")
    for conta in (conta1, conta2, conta3):
        print(f"{conta.titular} (conta {conta.numero}): R$ {conta.saldo:.2f}")


mostrar_saldos("Saldos iniciais")

# 1) Ana transfere R$ 200,00 para Carlos
conta1.transferir(conta2, 200)
print("\nAna transferiu R$ 200,00 para Carlos.")

# 2) Carlos transfere R$ 150,00 para Maria
conta2.transferir(conta3, 150)
print("Carlos transferiu R$ 150,00 para Maria.")

# 3) Maria tenta transferir R$ 500,00 para Ana (saldo insuficiente)
try:
    conta3.transferir(conta1, 500)
    print("Maria transferiu R$ 500,00 para Ana.")
except SaldoInsuficienteError as erro:
    print(f"Erro na transferência de Maria para Ana: {erro}")

mostrar_saldos("Saldos finais")

# 4) Transferência para a própria conta
try:
    conta1.transferir(conta1, 50)
except ValueError as erro:
    print(f"\nErro na transferência de Ana para ela mesma: {erro}")