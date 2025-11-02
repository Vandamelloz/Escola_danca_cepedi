class Exame: 
 def __init__(self, conducao_resposta:int, abraco:int, mecanica:int,
               ritmo:int, marcacao:int, data_exame: str="dd-mm-aaaa"):
  self.conducao_resposta=conducao_resposta
  self.abraco=abraco
  self.mecanica=mecanica
  self.ritmo=ritmo
  self.marcacao=marcacao
  self.data_exame=data_exame
 def __str(self):
   return (f"(Nota condução resposta: {self.conducao_resposta}, Nota abraco: {self.abraco}, )",
                f"Nota mecânica da dança: {self.mecanica}, Nota para ritmo da dança {self.ritmo}",
                f"Nota de marcação: {self.marcacao}, Data de realização do exame:{self.data_exame}")
  
  