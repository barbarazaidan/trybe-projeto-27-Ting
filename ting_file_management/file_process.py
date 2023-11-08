# Essa função é capaz de transformar o conteúdo da lista
# gerada pela função txt_importer
# em um dicionário que será armazenado dentro da fila.

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list_content = txt_importer(path_file)

    # faço uma iteração sobre os elementos da fila
    for index in range(instance.__len__()):
        # acesso o elemento da fila através do método search
        element = instance.search(index)
        # verifico se o nome do arquivo já está na fila
        if element["nome_do_arquivo"] == path_file:
            return None

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_content),
        "linhas_do_arquivo": list_content,
    }

    instance.enqueue(new_dict)
    print(new_dict)


# Essa função é capaz de remover o primeiro arquivo processado
def remove(instance):
    """Aqui irá sua implementação"""


# Essa função é capaz de apresentar as informações
# superficiais de um arquivo processado.
def file_metadata(instance, position):
    """Aqui irá sua implementação"""
