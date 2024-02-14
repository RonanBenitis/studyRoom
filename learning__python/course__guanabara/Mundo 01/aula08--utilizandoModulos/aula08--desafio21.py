# Faça um programa em Pythom que abra e reproduza o audio de um arquivos MP3.

# Use módulos

from playsound import playsound
import time

piada = input('Gostaria de uma piada? S/N: ')

if piada == 's':
    print("Qual time de futebol tem um bar onde os frequentadores ficam na chuva?")
    time.sleep(2)
    print("Bar sem-lona.")
    playsound("C:\\Users\\ronan\\Desktop\\#RESOURCES\\risada-chaves.mp3")

# == Resolução Guanabara ==
# Guanabara resolveu o desafio utilizando o módulo pygame com a instrução pygame.mixer.music.load e outras instruções.