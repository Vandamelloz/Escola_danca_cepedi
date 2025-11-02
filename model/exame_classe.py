class Exame: 
 def __init__(self, conducao_resposta:int, abraco:int, mecanica:int,
               ritmo:int, marcacao:int):
  self.conducao_resposta=conducao_resposta
  self.abraco=abraco
  self.mecanica=mecanica
  self.ritmo=ritmo
  self.marcacao=marcacao
 def __str(self):
   return (f"(Nota condução resposta: {self.conducao_resposta}, Nota abraco: {self.abraco}, )",
                f"Nota mecânica da dança: {self.mecanica}, Nota para ritmo da dança {self.ritmo}",
                f"Nota de marcação: {self.marcacao}")
  
  