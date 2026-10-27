import math


class SaldoInsuficienteError(Exception):
    """Lançada quando o saque ou a transferência excede o saldo."""


class ContaBancaria:
    def __init__(self, numero: str, titular: str):
        # RF01
        if numero is None or not str(numero).strip():
            raise ValueError("Número da conta é obrigatório.")
        if titular is None or len(str(titular).strip()) < 3:
            raise ValueError("Titular deve ter no mínimo 3 caracteres.")
        self._numero = numero
        self._titular = titular
        self._saldo = 0.00

    # RF02
    def depositar(self, valor: float) -> None:
        self._validar_valor(valor)
        self._saldo += valor

    # RF03
    def sacar(self, valor: float) -> None:
        self._validar_valor(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        self._saldo -= valor

    # RF04: todas as validações ocorrem ANTES de qualquer alteração (RN03)
    def transferir(self, destino: "ContaBancaria", valor: float) -> None:
        if destino is None:
            raise ValueError("Conta de destino não pode ser nula.")
        if destino is self:
            raise ValueError("Não é possível transferir para a própria conta.")
        self._validar_valor(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para a transferência.")
        self.sacar(valor)
        destino.depositar(valor)

    # RF05
    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> str:
        return self._numero

    @property
    def titular(self) -> str:
        return self._titular

    # RN02: rejeita não numéricos, NaN, infinito, zero e negativos
    @staticmethod
    def _validar_valor(valor) -> None:
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
            or valor <= 0
        ):
            raise ValueError("O valor deve ser um número positivo.")