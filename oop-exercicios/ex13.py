class Computador:
    departamento = 'Comum'
    def __init__(self, modelo, processador, memoria):
        self.modelo = modelo
        self.processador = processador
        self.memoria = memoria

class CompIA(Computador):
    departamento = 'IA'
    def __init__(self, modelo, processador, memoria, placa_de_video):
        super().__init__(modelo, processador, memoria)
        self.placa_de_video = placa_de_video

c1 = Computador('Dell Inspiron 15', 'I5-12250U', '8 GB')
c2 = CompIA('Dell G15', 'I9-12420', '32 GB', 'RTX 4060Ti')    

