import json
with open('pokepoke.json') as arquivo: 
    inspermons = json.load(arquivo)
import time
##  PEGA OS INSPERMONS EM DICIONÁRIOS E TRANSFORMA OS NOMES, VIDA, DEFESA E PODER EM LISTAS##
pokenomes=[]
pokevidas=[]
pokedefesas=[]
pokepoderes=[]
for i in range(len(inspermons)):
    nomes = inspermons[i]["nome"]
    pokenomes.append(nomes)
    
    vidas = inspermons[i]["vida"]
    pokevidas.append(vidas)

    defesas = inspermons[i]["defesa"]
    pokedefesas.append(defesas)
    
    poderes = inspermons[i]["poder"]
    pokepoderes.append(poderes)

## MENU INICIAL##
def menu ():
    esc=[input("O que gostaria de fazer, {}?(dormir/ caminhar/ pokedex)\n ".format(name))]
    if esc[0]=='dormir':
        print("Boa noite!!  \n")
        time.sleep(0.9)
        print("Zzzzzzzzz")
        time.sleep(0.9)
        print("Zzzzzzzzz")
        time.sleep(0.9)
        print("Zzzzzzzzz")
        time.sleep(0.9)
        print("Zzzzzzzzz \n")
        time.sleep(0.9)
        print("Bom dia!!")
        menu() 
    if esc[0]=='caminhar':
        print("Você estava andando até que..." "\n")
        ale = range(len(inspermons))
        poke2 = random.choice(ale)
        print("UM {} SELVAGEM APARECEU!!" "\n".format(inspermons[poke2]["nome"]).upper())
        var=input("Você deseja batalhar? (sim/nao)\n")
        if var=='sim':
            print("Aqui estão seus inspermons: \n") 
            for i in dex:
                print(i,"\n")
            
            poke=input("Escolha o inspermon que deseja usar para a batalha:\n  ")
            
            
            while poke not in dex :
                print("Inspermon inválido" "\n")

                poke=input("Escolha um inspermon válido que deseja usar:\n  ")
                
            poke1 = pokenomes.index(poke) 
        if var=='nao':
                    print("Que pena...")
                    menu() 
        else:
            while var!= 'nao' and var!='sim':
                print("digite uma resposta válida")
                var=input("Você deseja batalhar? (sim/nao)\n")
                if var=='sim':
                    print("Aqui estão seus inspermons: \n") 
                    for i in dex:
                        print(i,"\n")
                    poke=input("Escolha o inspermon que deseja usar para a batalha:\n ")
                    
                    while poke not in dex :
                        print("Inspermon inválido" "\n")
                        poke=input("Escolha um inspermon válido que deseja usar: \n ")
                        for a in dex:
                            print(a)
                    poke1 = pokenomes.index(poke) 
                
                if var=='nao':
                    print("Que pena...\n")
                    menu() 
                
        batalha(poke1,poke2)
    if esc[0]=='pokedex':
        print("Aqui estão seus inspermons: \n") 
        for i in dex:
            print(i,"\n")
        atr=input("Deseja ver os atributos de algum deles? (sim/nao)\n")
        if atr=='sim':
            pe=input("Digite o nome dele: \n")
            while pe not in dex :
                print("Inspermon inválido" "\n")
                pe=input("Escolha um inspermon válido que deseja usar {}:\n  ".format(dex))
            mostra_ipmon(pe)
            menu()
        if atr=='nao':
            print("Então ok :D\n ")
           
        else:
            while atr!= 'nao' and atr!='sim':
                print("Digite uma resposta válida\n")
                atr=input("Deseja ver os atributos de algum deles? (sim/nao)\n")
                if atr=='sim':
                    pe=input("Digite o nome dele: \n")
                    while pe not in dex :
                        print("Inspermon inválido" "\n")
                        pe=input("Escolha um inspermon válido que deseja usar {}:\n  ".format(dex))
                    mostra_ipmon(pe)
                    
                if atr=='nao':
                    print("Então ok :D\n ")
                     
                
                
    else:
        while esc[0]!='pokedex' and esc[0]!='caminhar'and esc[0]!='dormir':
            print("Resposta errada, tente de novo: \n")
            esc=[input("O que gostaria de fazer, {}?(dormir/ caminhar/ pokedex)\n ".format(name))]




def mostra_ipmon(nome): 
    i = pokenomes.index(nome)
    print("Você escolheu o {0}, estes são seus atributos:".format(pokenomes[i]))
    print("poder = {0}".format(pokepoderes[i])) 
    print("vida = {0}".format(pokevidas[i]))
    print("defesa = {0}\n".format(pokedefesas[i]))
    
    
   
##   MODO BATALHA##

import random
def batalha (poke1, poke2):
    v1 = inspermons[poke1]["vida"]
    v2 = inspermons[poke2]["vida"]
    a1 = inspermons[poke1]["poder"]
    a2 = inspermons[poke2]["poder"]
    d1 = inspermons[poke1]["defesa"]
    d2 = inspermons[poke2]["defesa"]
    fator = [1 ,1 ,1 ,1 ,1 ,1 ,2 ,2, 2]
    print("{} VS {} \n ".format(inspermons[poke1]["nome"].upper(), inspermons[poke2]["nome"].upper()))
    while v1>0 and v2>0:
        sa1 = random.choice(fator)
        sa2 = random.choice(fator)
        if sa1==2:
            print("Que sorte, Seu ataque dobrou!\n")
        if sa2==2:
            print("Que azar, o ataque do seu oponente dobrou\n")
        del1 = a1*sa1 - d2
        del2 = a2*sa2 - d1
        if del1 > 0:
            v2 = v2 - del1
        else:
            v1=v1
        if del2 > 0:
            v1 = v1 - del2
        else:
            v2=v2

        if v1<=0 or v2<=0:
            
            if v1>v2:
                print("PARABÉNS, SEU {} GANHOU A BATALHA!".format(inspermons[poke1]["nome"]).upper())
                salva_insperdex(poke2)
        
            else:
                print("O SEU {} FOI DERROTADO!".format(inspermons[poke1]["nome"]).upper())
            break
    
        lisa=input("Essa é sua vida {0}, e essa é do seu adversário {1}. Deseja continuar lutando? (sim/nao)\n".format(v1,v2))
        if lisa=='sim':
            print("Próximo round!\n")
        if lisa=='nao':
            print("Então empatou!")
            break
            
        else:
            while lisa!= 'sim' and lisa!= 'nao':
                print("Resposta inválida \n")
                lisa=input("Essa é sua vida {0}, e essa é do seu adversário {1}. Deseja continuar lutando? (sim/nao)\n".format(v1,v2))
                if lisa=='sim':
                    print("Próximo round!\n")
                if lisa=='nao':
                    print("Então empatou!")
                    break
    menu()
    

    
## FATOR DE SORTE##



# SALVA INSPERDEX##
insperdex = []

def salva_insperdex(joj):
    p = inspermons[joj]["nome"]
    if p not in dex:
        print("Voce capturou um novo pokemon")
        dex.append(p)
    else:
        print("Você já tem esse inspermon né? \n")
# MOSTRA INSPERDEX##
    
#  INICIO DO JOGO#
print("Bem vindo caro treinador! \n")
dex=[]
name = input("Para começarmos diga seu nome:  \n")
first = input("Olá, {0}.Escolha seu inspermon inicial: (picaxu/cocomon)  \n".format(name))
while first not in pokenomes:
    first = input("Esse inspermon nao existe. \nEscolha seu inspermon inicial: (picaxu/cocomon)  \n")
mostra_ipmon(first)
dex.append(first)

## LOOP DO JOGO:##

while len(dex)<len(pokenomes):
    menu()
print("Parabéns você zerou o jogo!!!")

