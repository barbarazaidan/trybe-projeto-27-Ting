# Esta função é capaz de importar notícias a partir de um arquivo TXT,
# utilizando "\n" como separador.
# O caractere de nova linha é \n .
# Ele é usado para indicar o final de uma linha de texto.

import sys


def txt_importer(path_file):
    try:
        with open(path_file) as file:
            if path_file.endswith(".txt"):
                return file.read().split("\n")
            else:
                sys.stderr.write("Formato inválido\n")
                return None
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None


# print(txt_importer("sd-030-a-project-ting/ting_file_management/exemplo.txa"))
