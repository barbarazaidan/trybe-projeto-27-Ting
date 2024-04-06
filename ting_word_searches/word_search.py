# esta função que verifica a existência
# de uma palavra em todos os arquivos processados
def exists_word(word, instance):
    list = []
    word = word.lower()
    # vou percorrer a lista de dicionários
    for index in range(len(instance)):
        element = instance.search(index)
        line_register = []

        # vou percorrer a lista de linhas do arquivo atual do loop
        for line in element["linhas_do_arquivo"]:
            # procuro a posição da linha atual (line)
            # na lista de linhas do arquivo
            # o +1 é para não começar a contar a partir de 1
            index_line = element["linhas_do_arquivo"].index(line) + 1

            # verifico se a palavra está na linha e adiciono-a no registro
            if word in line.lower():
                line_register.append(
                    {
                        "linha": index_line,
                    }
                )
        if len(line_register) > 0:
            list.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": line_register,
                }
            )
    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
