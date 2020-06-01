class DatabaseModel:
    def setId(self, id: int):
        self.id = id

    def setIdPriMed(self, idPriMed: int):
        self.idPriMed = idPriMed

    def setIdSegMed(self, idSegMed: int):
        self.idSegMed = idSegMed

    def setNomePriMed(self, nomePriMed: str):
        self.nomePriMed = nomePriMed

    def setNomeSegMed(self, nomeSegMed: str):
        self.nomeSegMed = nomeSegMed

    def setGravidade(self, gravidade: str):
        self.gravidade = gravidade

    def setInicio(self, inicio: str):
        self.inicio = inicio

    def setProb(self, probabilidade: str):
        self.probabilidade = probabilidade

    def setEfeito(self, efeito: str):
        self.efeito = efeito

    def setMecanismo(self, mecanismo: str):
        self.mecanismo = mecanismo

    def setSujestao(self, sujestao: str):
        self.sujestao = sujestao

    @property
    def getId(self):
        return self.id

    @property
    def getIdPriMed(self):
        return self.idPriMed

    @property
    def getIdSegMed(self):
        return self.idSegMed

    @property
    def getNomePriMed(self):
        return self.nomePriMed

    @property
    def getNomeSegMed(self):
        return self.nomeSegMed

    @property
    def getGravidade(self):
        return self.gravidade

    @property
    def getInicio(self):
        return self.inicio

    @property
    def getProb(self):
        return self.probabilidade

    @property
    def getEfeito(self):
        return self.efeito

    @property
    def getMecanismo(self):
        return self.mecanismo

    @property
    def getSujestao(self):
        return self.sujestao