class ConsultaPet():
    def __init__(self, pet, motivo_consulta, peso_atual, medicamento_atual, medicamento_prescritos,
                 exames, data=""):
        self.__pet = pet
        self.__motivo_consulta = motivo_consulta
        self.__peso_atual = peso_atual
        self.__medicamento_atual = medicamento_atual
        self.__medicamento_prescritos = medicamento_prescritos
        self.__exames = exames
        self.__data = data

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, pet):
        self.__pet = pet

    @property
    def motivo_consulta(self):
        return self.__motivo_consulta

    @motivo_consulta.setter
    def motivo_consulta(self, motivo_consulta):
        self.__motivo_consulta = motivo_consulta

    @property
    def peso_atual(self):
        return self.__peso_atual

    @peso_atual.setter
    def peso_atual(self, peso_atual):
        self.__peso_atual = peso_atual

    @property
    def medicamento_atual(self):
        return self.__medicamento_atual

    @medicamento_atual.setter
    def medicamento_atual(self, medicamento_atual):
        self.__medicamento_atual = medicamento_atual

    @property
    def medicamento_prescritos(self):
        return self.__medicamento_prescritos  # Corrigir para usar o atributo privado

    @medicamento_prescritos.setter
    def medicamento_prescritos(self, medicamento_prescritos):
        self.__medicamento_prescritos = medicamento_prescritos  # Corrigir para usar o atributo privado

    @property
    def exames(self):
        return self.__exames

    @exames.setter
    def exames(self, exames):
        self.__exames = exames

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data