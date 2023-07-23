from subprocess import run
import pyperclip

linha_parada = input('linha de parada: ')
linhas = []

while True:
    linha = input('texto: ')
    if linha == linha_parada:
        texto = '\n'.join(linhas)
        break
    linhas.append(linha)
n_caracteres = len(texto)
print(f'o texto tem {n_caracteres} caracteres')
divicao_caracteres = int(input('numeros de caracteres: '))
texto_dividido = list()
tem_o_tamanho = True

while True:
    if n_caracteres > divicao_caracteres:
        texto_dividido.append(texto[:divicao_caracteres])
        texto = texto.replace(texto_dividido[-1], '')
        n_caracteres_anterior = n_caracteres
        n_caracteres = n_caracteres - divicao_caracteres
        tem_o_tamanho = False
    else:
        if n_caracteres != - n_caracteres_anterior:
            texto_dividido.append(texto[:divicao_caracteres])
        break
            

def copy(indice:int) -> None:
    pyperclip.copy(texto_dividido[indice])
