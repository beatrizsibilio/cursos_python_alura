from lista1.veiculo import Veiculo


class Moto(Veiculo):
  def __init__(self, marca, modelo, tipo) -> None:
    super().__init__(marca, modelo)
    self._tipo = tipo
  
  def __str__(self) -> str:
    status =  'ligado' if self._ligado else 'desligado'
    cabecalho = f'{"Marca".ljust(25)} | {"Modelo".ljust(25)} | {"Tipo".ljust(25)} | Status'
    return f'{cabecalho}\n{self._marca.ljust(25)} | {self._modelo.ljust(25)} | {self._tipo.ljust(25)} | {status}'