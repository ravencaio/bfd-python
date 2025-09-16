class Computador:
    departamento = 'Comum'
    modelo = 'Dell Inspiron 15'
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria

class CompIA(Computador):
    departamento = 'IA'
    modelo = 'Dell G15'
    def __init__(self, processador, memoria, placa_de_video):
        super().__init__(processador, memoria)
        self.placa_de_video = placa_de_video

c1 = Computador('I5-12250U', '8 GB')
c2 = CompIA('I9-12420', '32 GB', 'RTX 4060Ti')    

