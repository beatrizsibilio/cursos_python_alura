from lista1.veiculo import Veiculo


class Carro(Veiculo):
  def __init__(self, marca, modelo, portas) -> None:
    super().__init__(marca, modelo)
    self._portas = portas
  
  def __str__(self) -> str:
    status =  'ligado' if self._ligado else 'desligado'
    cabecalho = f'{"Marca".ljust(25)} | {"Modelo".ljust(25)} | {"Portas".ljust(25)} | Status'
    return f'{cabecalho}\n{self._marca.ljust(25)} | {self._modelo.ljust(25)} | {str(self._portas).ljust(25)} | {status}'