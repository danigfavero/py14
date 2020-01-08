class Aluno:

    def __init__(self, nome, ano, matricula):
        self._nome = nome
        self._ano = ano
        self._matricula = matricula


class Disciplina:

    def __init__(self, horario, alunos=[]):
        self._horario = horario
        self._alunos = alunos

    def adiciona_aluno(self, aluno):
        self._alunos.append(aluno)

    def 