import os
import random
import time
from openpyxl.workbook import Workbook
import pandas as pd

inicio = time.time()
nJogadas = 0
vez = 1
vitoria = False
vencedor = ""
velha = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
jogar = "s"
nVitorias1=0 
nVitorias2=0   
jogar=0
nEmpates=0
df="" #data frame


def tabuleiro(velha):
    #os.system('cls')     
    print("  "+velha[0] + " | "+ velha[1]+ " | "+ velha[2])
    print(" -----------")
    print("  "+velha[3] + " | "+ velha[4]+ " | "+ velha[5])
    print(" -----------")
    print("  "+velha[6] + " | "+ velha[7]+ " | "+ velha[8])
    print(f"Numeros de jogadas: {nJogadas}")
    print("#"*30)    

def jogadorBrabo(jog, v):
    
    global nJogadas
    global vez
    global vitoria
    global vencedor
    global velha
    
    jog1="X" if jog=="O" else "O" 
        
    if vez==v and vitoria==False and nJogadas<9:
        #Se Primeira jogada
        if nJogadas==0:
            velha[0]=jog
            
        #Se Segunda jogada
        elif nJogadas==1:
            
            #Se oponente iniciou pelo meio
            if velha[4]!=" ":
                posicao = random.randrange(0,9)
                                 
                while (posicao==1) or (posicao==3) or (posicao==5) or (posicao==7)  or (posicao==4):                             
                    posicao = random.randrange(0,9)
                    
                velha[posicao] = jog
                
            #Se oponente iniciou pelas pontas centrais
            elif velha[4]==" ":
                velha[4]=jog
                
            
            
                             
        #Se Terceira jodada    
        elif nJogadas==2:
            if velha[1]!=" " or velha[2]!=" " or velha[5]!=" " or velha[7]!=" " or velha[8]!=" ":
                velha[6] = jog
            elif velha[3]!=" " or velha[6]!=" ":
                velha[2]=jog
            else:
                velha[8]=jog                                         
                                         
        #**Ataque**
        #posicao
        elif velha[0]==jog and velha[1]==jog and velha[2]==" ":
            velha[2]=jog
        elif velha[0]==jog and velha[1]==" " and velha[2]==jog:
            velha[1]=jog 
        elif velha[0]==" " and velha[1]==jog and velha[2]==jog:
            velha[0]=jog
            
        elif velha[3]==jog and velha[4]==jog and velha[5]==" ":
            velha[5]=jog
        elif velha[3]==jog and velha[4]==" " and velha[5]==jog:
            velha[4]=jog 
        elif velha[3]==" " and velha[4]==jog and velha[5]==jog:
            velha[3]=jog 
            
        elif velha[6]==jog and velha[7]==jog and velha[8]==" ":
            velha[8]=jog
        elif velha[6]==jog and velha[7]==" " and velha[8]==jog:
            velha[7]=jog 
        elif velha[6]==" " and velha[7]==jog and velha[8]==jog:
            velha[6]=jog
            
        #Coluna
        elif velha[0]==jog and velha[3]==jog and velha[6]==" ":
            velha[6]=jog
        elif velha[0]==jog and velha[3]==" " and velha[6]==jog:
            velha[3]=jog 
        elif velha[0]==" " and velha[3]==jog and velha[6]==jog:
            velha[0]=jog
            
        elif velha[1]==jog and velha[4]==jog and velha[7]==" ":
            velha[7]=jog
        elif velha[1]==jog and velha[4]==" " and velha[7]==jog:
            velha[4]=jog 
        elif velha[1]==" " and velha[4]==jog and velha[7]==jog:
            velha[1]=jog 
            
        elif velha[2]==jog and velha[5]==jog and velha[8]==" ":
            velha[8]=jog
        elif velha[2]==jog and velha[5]==" " and velha[8]==jog:
            velha[5]=jog 
        elif velha[2]==" " and velha[5]==jog and velha[8]==jog:
            velha[2]=jog
            
        #Diagonal
        elif velha[0]==jog and velha[4]==jog and velha[8]==" ":
            velha[8]=jog
        elif velha[0]==jog and velha[4]==" " and velha[8]==jog:
            velha[4]=jog 
        elif velha[0]==" " and velha[4]==jog and velha[8]==jog:
            velha[0]=jog
        
        elif velha[2]==jog and velha[4]==jog and velha[6]==" ":
            velha[6]=jog
        elif velha[2]==jog and velha[4]==" " and velha[6]==jog:
            velha[4]=jog 
        elif velha[2]==" " and velha[4]==jog and velha[6]==jog:
            velha[2]=jog
        
        #**Defesa**
        #posicao
        elif velha[0]==jog1 and velha[1]==jog1 and velha[2]==" ":
            velha[2]=jog
        elif velha[0]==jog1 and velha[1]==" " and velha[2]==jog1:
            velha[1]=jog 
        elif velha[0]==" " and velha[1]==jog1 and velha[2]==jog1:
            velha[0]=jog
            
        elif velha[3]==jog1 and velha[4]==jog1 and velha[5]==" ":
            velha[5]=jog
        elif velha[3]==jog1 and velha[4]==" " and velha[5]==jog1:
            velha[4]=jog 
        elif velha[3]==" " and velha[4]==jog1 and velha[5]==jog1:
            velha[3]=jog 
            
        elif velha[6]==jog1 and velha[7]==jog1 and velha[8]==" ":
            velha[8]=jog
        elif velha[6]==jog1 and velha[7]==" " and velha[8]==jog1:
            velha[7]=jog 
        elif velha[6]==" " and velha[7]==jog1 and velha[8]==jog1:
            velha[6]=jog       

        #Coluna    
        elif velha[0]==jog1 and velha[3]==jog1 and velha[6]==" ":
            velha[6]=jog
        elif velha[0]==jog1 and velha[3]==" " and velha[6]==jog1:
            velha[3]=jog 
        elif velha[0]==" " and velha[3]==jog1 and velha[6]==jog1:
            velha[0]=jog
            
        elif velha[1]==jog1 and velha[4]==jog1 and velha[7]==" ":
            velha[7]=jog
        elif velha[1]==jog1 and velha[4]==" " and velha[7]==jog1:
            velha[4]=jog 
        elif velha[1]==" " and velha[4]==jog1 and velha[7]==jog1:
            velha[1]=jog 
            
        elif velha[2]==jog1 and velha[5]==jog1 and velha[8]==" ":
            velha[8]=jog
        elif velha[2]==jog1 and velha[5]==" " and velha[8]==jog1:
            velha[5]=jog 
        elif velha[2]==" " and velha[5]==jog1 and velha[8]==jog1:
            velha[2]=jog
            
        #Diagonal
        elif velha[0]==jog1 and velha[4]==jog1 and velha[8]==" ":
            velha[8]=jog
        elif velha[0]==jog1 and velha[4]==" " and velha[8]==jog1:
            velha[4]=jog 
        elif velha[0]==" " and velha[4]==jog1 and velha[8]==jog1:
            velha[0]=jog
        
        elif velha[2]==jog1 and velha[4]==jog1 and velha[6]==" ":
            velha[6]=jog
        elif velha[2]==jog1 and velha[4]==" " and velha[6]==jog1:
            velha[4]=jog 
        elif velha[2]==" " and velha[4]==jog1 and velha[6]==jog1:
            velha[2]=jog
            
        #Se Quarta jogada
        elif nJogadas==3: 
            
            if((velha[0]==jog1 and velha[8]==jog1) or (velha[2]==jog1 and velha[6]==jog1)):           
                posicao = random.randrange(0,9)
                
                while (posicao!=1 and posicao!=3 and posicao!=5 and posicao!=7) or (velha[posicao]!=" "):
                    posicao = random.randrange(0,9)
                                        
                velha[posicao] = jog
                
            elif((velha[0]!=" " and velha[8]!=" ") or (velha[2]!=" " and velha[6]!=" ")):           
                posicao = random.randrange(0,9)
                
                while (posicao!=0 and posicao!=2 and posicao!=6 and posicao!=8) or (velha[posicao]!=" "):
                    posicao = random.randrange(0,9)
                                        
                velha[posicao] = jog
                
            elif velha[4]==" ":
                    velha[4]=jog            
            
            elif velha[3]==" " and velha[5]==" ":
                velha[3]=jog
            elif velha[1]==" " and velha[7]==" ":
                velha[1]=jog
            elif velha[0]==" " and velha[8]==" ":
                x = (1, 2, 3, 6)
                soma=0
                for i in x:
                    if velha[i]==jog1:
                        soma+=1
                if soma==2:
                    velha[0]=jog                
                else:
                    velha[8]=jog
                                
            elif velha[2]==" " and velha[6]==" ":
                soma=0
                x= (0, 1, 5, 8)
                for i in x:
                    if velha[i]==jog1:
                        soma+=1                   
                if soma==2:
                    velha[2]=jog
                else:
                    velha[6]=jog
                    
            
        #Se quinta jogada        
        elif nJogadas==4 and velha[4]==" ": #and ((velha[0]==jog1 and velha[4]!=" ") or (velha[8]!=jog1 and velha[4]!=" ") or (velha[2]==jog1 and velha[4]!=" ") or (velha[6]!=jog1 and velha[4]!=" ")):
            velha[4]=jog
        
        #Se sexta jogada    
        elif nJogadas==5 and ((velha[0]==" " and velha[8]==" ") or (velha[6]==" " and velha[2]==" ")):
            soma=0
            vazio=0
            if velha[0]==" " and velha[8]==" ":
                x= (1, 2)
                y = (3, 6)
                for i in x:
                    if velha[i]==jog1:
                        soma+=1
                    elif velha[i]==" ":
                        vazio+=1
                for i in y:
                    if velha[i]==jog1:
                        soma+=1
                    elif velha[i]==" ":
                        vazio+=1
                if soma==2 and vazio==2:
                    velha[0]=jog
                else:
                    velha[8]=jog
            else:
                x = (5, 8)
                for i in range(2):
                    if velha[i]==jog1:
                        soma+=1
                    elif velha[i]==" ":
                        vazio+=1
                for i in x:
                    if velha[i]==jog1:
                        soma+=1
                    elif velha[i]==" ":
                        vazio+=1
                if soma==2 and vazio==2:
                    velha[2]=jog
                else:
                    velha[6]=jog                                     
        
        else:            
            posicao = random.randrange(0,9)
            
            while velha[posicao] != " ":           
                posicao = random.randrange(0,9)
                
            velha[posicao] = jog                    
        
        nJogadas+=1
        vez=1 if v==2 else 2        
        
    if nJogadas>=4 and vencedor=="":
        vitoria=verificar_vitoria(jog)
        if vitoria==True:
            vencedor = v
            
def jogHumano(jog, v):
    global nJogadas
    global vez
    global vitoria
    global vencedor
    
    if vez==v and vitoria==False and nJogadas<9 and vencedor=="":
        posicao = int(input("Informe a posicao da jogada: "))
        
        while velha[posicao] != " ":
            print("Essa posição já está selecionada!")            
            posicao = int(input("Informe a posicao da jogada: "))
            
            
        velha[posicao] = jog
        nJogadas+=1
        
        if nJogadas>=4 and vencedor=="":
            vitoria=verificar_vitoria(jog) 
            if vitoria==True:
                vencedor = v
                           
    vez=1 if v==2 else 2
    
def jogIniciante(jog, v):
    global nJogadas
    global vez
    global vitoria
    global vencedor
    global velha
    
    if vez==v and vitoria==False and nJogadas<9:
        posicao = random.randrange(0,9)
        
        while velha[posicao] != " ":           
            posicao = random.randrange(0,9)
            
        velha[posicao] = jog
        nJogadas+=1
        
    if nJogadas>=4 and vencedor=="":
        vitoria=verificar_vitoria(jog)
        if vitoria==True:
            vencedor = v
                     
    vez=1 if v==2 else 2
    
def posicoesDisp(estado):
    return [i for i, celula in enumerate(estado) if celula == " "]
    
def escolherJogada(memoria, velha):
    estado = str(velha)
    vazio = posicoesDisp(velha)
    if memoria == {}:
        return random.choice(vazio)
    else:
        pontuacao = [memoria.get((estado, pos), 0) if pos in vazio else -float('inf') for pos in range(9)]
        max_pontuacao = max(pontuacao)
        melhores_jogadas = [pos for pos, pont in enumerate(pontuacao) if pont == max_pontuacao]
        return random.choice(melhores_jogadas)
    
def ler_memoria():
    if os.path.exists("memoria.txt"):
        with open("memoria.txt", "r") as f:
            jogadas = eval(f.read())
    else:
        jogadas = {}
    return jogadas                      
    
def jInteligente(jog, v):
    global nJogadas
    global vez
    global vitoria
    global vencedor
    global velha
    global partida
    global memoria
    
    if vez==v and vitoria==False and nJogadas<9:        
        
        posicao = escolherJogada(memoria, velha)
        partida.append((str(velha), posicao))
        #fazer a jogada            
        velha[posicao] = jog
       
        nJogadas+=1
        
    if nJogadas>=4 and vencedor=="":
        vitoria=verificar_vitoria(jog)
        if vitoria==True:
            vencedor = v
                     
    vez=1 if v==2 else 2                         
    
def verificar_vitoria(s):
    global velha
    global vitoria  
            
    #linha
    l = ((0, 1 , 2), (3, 4, 5), (6, 7, 8))
    for i in l:
        soma=0
        for j in i:                
            if velha[j]==s:
                soma+=1
        if(soma==3):
            vitoria=True
            break            
    
    #Colunas
    c = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
    for i in c:
        soma=0
        for j in i:                
            if velha[j]==s:
                soma+=1
        if(soma==3):
            vitoria=True
            break      
                
    #Diagonal
    soma=0
    diag= ((0, 4, 8), (2, 4, 6))        
    for i in diag:
        soma=0
        for j in i:                
            if velha[j]==s:
                soma+=1
        if(soma==3):
            vitoria=True
            break    
            
    return vitoria   

def resetar():
    global nJogadas
    global vez    
    global vitoria
    global vencedor
    global velha
    #os.system("cls")
        
    nJogadas = 0
    vez = 1     
    vitoria = False
    vencedor = ""
    velha = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
#Gerar arquivo exel    
def fileExel(jogar):
    global df
    if jogar==0:
        h = ["Partida", "Resultado", "Vitorias 1", "Vitorias 2", "Velhas"]
        df = pd.DataFrame(columns=h)        
        df.to_csv("ia.csv", sep=',', index=False)
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("ia.csv", sep=',', index=False)
    else:
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("ia.csv", sep=',', index=False)
        
#desenvolver...
def fileMatriz(jogar):
    global df
    if jogar==0:
        h = ["Partida", "Resultado", "Vitorias 1", "Vitorias 2", "Velhas"]
        df = pd.DataFrame(columns=h)        
        df.to_xml("braboXbrabo.csv", sep=',', index=False)
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("braboXbrabo.csv", sep=',', index=False)
    else:
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("braboXbrabo.csv", sep=',', index=False)  
        
def armazenar_memoria(jogadas):
    with open("memoria.txt", "w") as f:
        f.write(str(jogadas))


partida = []  

while jogar<10000:
    memoria = ler_memoria()
    while True:
        
        #tabuleiro(velha)
        jInteligente("X",1)
        #tabuleiro(velha)
        jogIniciante("O",2)        
        
        if (vitoria==True):
            #tabuleiro(velha)
            #print("*"*30)
            #print(f"Parabens '{vencedor}' foi o vencedor!")
            #print("*"*30)
            if vencedor==1:
                nVitorias1+=1
                for i in partida:
                    if memoria.get(i):
                        memoria[i] += 1
                    else:
                        memoria[i]=1
            elif vencedor==2:
                nVitorias2+=1
                for i in partida:
                    if memoria.get(i):
                        memoria[i] -= 1
                    else:
                        memoria[i]=-1
            fileExel(jogar)
            armazenar_memoria(memoria)
            jogar+=1
            break
        if nJogadas==9:
            #tabuleiro(velha)
            #print("*"*30)
            #print("Empatou!")
            #print("*"*30)
            vencedor = 0
            nEmpates+=1
            fileExel(jogar)
            jogar+=1            
            break
    #print(jogar)
    #jogar = input("Deseja jogar novamente?(s/n): ")
    resetar()
    
print("Vitorias jogador 1: " + str(nVitorias1))
print("Vitorias jogador 2: " + str(nVitorias2))
print("Empates: " + str(nEmpates))
fim = time.time()
print(f"Tempo total: {((fim-inicio)):.3f}")
