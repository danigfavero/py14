import abc


class Tributavel(abc.ABC):
    """ Classe que contém operações de um objeto autenticável

    As subclasses concretas devem sobrescrever um método get_valor_imposto.
    """

    @abc.abstractmethod
    def get_valor_imposto(self, valor):
        """ aplica taxa de imposto sobre um determinado valor do objeto """
        pass
