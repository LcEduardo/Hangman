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
        self.palavra_erradas = []
        self.letras_escolhidas = []
        
        

    def tamanhoDaPalavra(self):
        tamanho = ['_' for i in self.palavra]
        return tamanho
    
    def status(self):
        print("----------------Bem-Vindo ao Jogo da Forca----------------\n")
        print(f"Palavra: {self.tamanhoDaPalavra()}\n")
        print(f"Palavras Erradas: {self.palavra_erradas}\n")

    def verificaLetra(self,letra):

        if letra in self.palavra:
           
           # Isto deve estar em outro método
           '''
            for i, caractere in enumerate(self.palavra):
                    if caractere == letra:
                        self.tamanhoDaPalavra()[i] = letra
            
           ''' 
                       
        else:
            self.palavra_erradas.append(letra)   

    def win(self):
        if '_' not in self.tamanho_palavra:
            return True
        return False
    

def main():

    clear_screen()
    
    game1 = Game(listaPalavras())
    game1.status()  

    letra = input("Digite uma letra: ")
    game1.verificaLetra(letra)


if __name__ == "__main__":
    main()