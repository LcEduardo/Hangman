import random
import os 
from os import name, system

def clear_screen():
    
    if name == 'nt':
        _ = system('cls')

def listaPalavras():
    try:
        with open("palavras.txt", "r") as arquivo:
            conteudo = arquivo.read()

        texto_sem_espaco = conteudo.replace(" ", "")
        tamanho_da_palavra = texto_sem_espaco.split(",")

        indice = random.randint(0, len(tamanho_da_palavra) -1)
        palavra = tamanho_da_palavra[indice]       

        return palavra
    
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    return []
    

class Game:

    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = ['_' for i in self.palavra]
    
    def status(self):
        print("----------------Bem-Vindo ao Jogo da Forca----------------\n")
        print(f"Palavra: {' '.join(self.letras_escolhidas)}\n")
        print(f"Palavras Erradas: {self.letras_erradas}\n")


    def verificaLetra(self,letra):

        if letra in self.palavra:
            for idx, char in enumerate(self.palavra):
                if char == letra:
                    self.letras_escolhidas[idx] = letra
        else:
            self.letras_erradas.append(letra)  

    def hangman_over(self):
        return self.win() or (len(self.letras_erradas) == 6)

    def win(self):
        if '_' not in self.letras_escolhidas:
            return True
        return False
    
    def getPalavra(self):
        return self.palavra

def main():

    clear_screen()
    
    game1 = Game(listaPalavras())

    while not game1.hangman_over():
        game1.status()  

        letra = input("Digite uma letra: ")
        game1.verificaLetra(letra)


    if game1.win():
        print("Parabens você venceu!!\n")
        print(f"A Palavra era: {game1.getPalavra().upper()}")
    else:
        print("Você perdeu!!")
        print(f"A Palavra era: {game1.getPalavra().upper()}")

if __name__ == "__main__":
    main()