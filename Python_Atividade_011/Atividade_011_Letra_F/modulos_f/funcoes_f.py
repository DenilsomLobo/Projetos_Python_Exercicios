# Função:


def formador_Dict(lista1, lista2):
    """[Função que converte listas em dicionario]

    Args:
        lista1 ([List]): [Lista que vai ser a chave]
        lista2 ([List]): [Lista que vai ser o valor]

    Returns:
      newList  [Dict]: [Novo dicionario com chave e valores das listas inseridas]
    """
    newList = dict(zip(lista1, lista2))
    return newList

