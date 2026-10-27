import math


class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, numero, titular):
        if numero is None or not str(numero).strip():
            raise ValueError("Número da conta é obrigatório.")
        if titular is None or len(str(titular).strip()) < 3:
            raise ValueError("Titular deve ter no mínimo 3 caracteres.")
        self._numero = numero
        self._titular = titular
        self._saldo = 0.00

    def _validar_valor(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O valor deve ser um número.")
        if not math.isfinite(valor) or valor <= 0:
            raise ValueError("O valor deve ser positivo.")

    def depositar(self, valor):
        self._validar_valor(valor)
        self._saldo += valor

    def sacar(self, valor):
        self._validar_valor(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self._saldo -= valor

    def transferir(self, destino, valor):
        if destino is None:
            raise ValueError("Destino não pode ser nulo.")
        if destino is self:
            raise ValueError("Não pode transferir para a própria conta.")
        self._validar_valor(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular