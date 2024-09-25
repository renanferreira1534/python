import os

arquivo_original = input("digite o nome do arquivo que sera renomeado")
novo_arquivo = input("digite o novo nome do arquivo")


mudarNome(arquivo_original, novo_arquivo)

# para criar uma função em python iremos utilizar o comando
# def(definição)
def mudarNome(ar_or,nv_ar):
    """
    a função mudarNome, altera o nome de um arquivo.
    O usuario deve passar o nome o nome original do arquivo e 
    o novo nome.
    Args:
        ar_os(str): O nome original do arquivo
        nv_ar (str): O novo nome do arquivo
    returns:
        retorna uma msg de confirmaçao
    """
    os.rename(ar_or,nv_ar)
    msg = " o nome do arquivo foi alterado"
    return msg

arquivo_original = input("digite o nome do arquivo que sera renomeado")
novo_arquivo = input("digite o novo nome do arquivo")
rs = mudarNome(arquivo_original, novo_arquivo)
print(rs)



