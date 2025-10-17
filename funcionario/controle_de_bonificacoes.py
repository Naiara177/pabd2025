from funcionario.funcionario import Funcionario
class ControleDeBonificacoes:

    __slots__ = ['_total']
    def __init__(self, total = 0):
        self._total = total

    # registrar - incrementa as bonificações dos funcionarios 
    def registrar(self, obj):
        # verifica se o objeto é uma instância da classe Funcionario
        if isinstance(obj, Funcionario):
            self._total += obj.get_bonificacao()
        else:
            print(f"Instância de {obj.__class__.__name__} não implementa o método get_bonificacao()")

        @property
        def total(self):
            return self._total
    
    if __name__ == "__main__":
        controle = ControleDeBonificacoes()
        # Exemplo de uso: crie instâncias de Funcionario compatíveis com sua implementação.
        # Por exemplo (ajuste conforme o construtor da sua classe Funcionario):
        # f = Funcionario("Alice", 3000.0)
        # g = Funcionario("Bob", 2500.0)
        try:
            controle.registrar(f)
        except NameError:
            # f não está definido no contexto de importação; pule o registro
            pass
        try:
            controle.registrar(g)
        except NameError:
            # g não está definido no contexto de importação; pule o registro
            pass
        print(f"Total = R$ {controle.total:.2f}")