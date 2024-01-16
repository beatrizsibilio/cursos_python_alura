class Veiculo:
  def __init__(self, marca, modelo) -> None:
    self._marca = marca
    self._modelo = modelo
    self._ligado = False
  
  def __str__(self) -> str:
    status =  'ligado' if self._ligado else 'desligado'
    cabecalho = f'{"Marca".ljust(25)} | {"Modelo".ljust(25)} | Status'
    return f'{cabecalho}\n{self._marca.ljust(25)} | {self._modelo.ljust(25)} | {status}'