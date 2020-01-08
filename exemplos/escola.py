class Aluno:

    def __init__(self, nome, ano, matricula):
        self._nome = nome
        self._ano = ano
        self._matricula = matricula


    @property
    def nome(self):
        return self._nome


class Disciplina:

    _numero_de_disciplinas = 0

    def __init__(self, horario, alunos=[]):
        self._horario = horario
        self._alunos = alunos
        self._notas = {}
        Disciplina.adiciona_disciplina()
    
    @classmethod
    def adiciona_disciplina(cls): #TESTAR
        cls._numero_de_disciplinas += 1

    def adiciona_aluno(self, aluno):
        self._alunos.append(aluno)

    def adiciona_nota(self, aluno, nota):
        self._notas[aluno] = nota

    def imprime_notas(self):
        if not self._notas:
            print("Não há notas registradas!")
            return

        print("\nNOTAS")
        for aluno in self._notas.keys():
            print("{}: {}".format(aluno, self._notas[aluno]))

    @property
    def horario(self):
        return self._horario
    
if __name__ == "__main__":
    aluno1 = Aluno('ze', 2, 0)
    aluno2 = Aluno('zezinho', 3, 1)
    aluninhos = [aluno1, aluno2]
    aluno3 = Aluno('zezao', 1, 2)

    disciplina1 = Disciplina(14, aluninhos)
    print(disciplina1.horario)
    disciplina1.imprime_notas()

    disciplina1.adiciona_nota(aluno1._nome, 0.0)
    disciplina1.imprime_notas()    

    disciplina1.adiciona_aluno(aluno3)
    disciplina1.adiciona_nota(aluno2._nome, 10.0)
    disciplina1.adiciona_nota(aluno3._nome, 6.5)
    disciplina1.imprime_notas()

    disciplina1.adiciona_nota(aluno1._nome, 6.5)
    disciplina1.imprime_notas()


