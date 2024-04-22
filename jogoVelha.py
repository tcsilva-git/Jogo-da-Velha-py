import os
import random
import time
from openpyxl.workbook import Workbook
import pandas as pd

inicio = time.time()
nJogadas = 0
vez = 1
simb1 = "X"
simb2="O"
vitoria = False
vencedor = ""
velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
jogar = "s"
nVitorias1=0 
nVitorias2=0   
jogar=0
nEmpates=0
df="" #data frame

def tabuleiro(velha):
    #os.system('cls')
    print("    0   1   2")   
    print("0:  "+ velha[0][0] + " | "+ velha[0][1]+ " | "+ velha[0][2])
    print("   -----------")
    print("1:  "+ velha[1][0] + " | "+ velha[1][1]+ " | "+ velha[1][2])
    print("   -----------")
    print("2:  "+ velha[2][0] + " | "+ velha[2][1]+ " | "+ velha[2][2])
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
            velha[0][0]=jog
            
        #Se Segunda jogada
        elif nJogadas==1:
            
            #Se oponente iniciou pelo meio
            if velha[1][1]!=" ":
                linha = random.randrange(0,3)
                coluna = random.randrange(0,3)                 
                while (linha==0 and coluna==1) or (linha==1 and coluna==0) or (linha==1 and coluna==2) or (linha==2 and coluna==1)  or (linha==1 and coluna==1):                             
                    linha = random.randrange(0,3)
                    coluna = random.randrange(0,3)
                velha[linha][coluna] = jog
                
            #Se oponente iniciou pelas pontas centrais
            elif velha[1][1]==" ":
                velha[1][1]=jog
                
            
            
                             
        #Se Terceira jodada    
        elif nJogadas==2:
            if velha[0][1]!=" " or velha[0][2]!=" " or velha[1][2]!=" " or velha[2][1]!=" " or velha[2][2]!=" ":
                velha[2][0] = jog
            elif velha[1][0]!=" " or velha[2][0]!=" ":
                velha[0][2]=jog
            else:
                velha[2][2]=jog                                         
                                         
        #**Ataque**
        #Linha
        elif velha[0][0]==jog and velha[0][1]==jog and velha[0][2]==" ":
            velha[0][2]=jog
        elif velha[0][0]==jog and velha[0][1]==" " and velha[0][2]==jog:
            velha[0][1]=jog 
        elif velha[0][0]==" " and velha[0][1]==jog and velha[0][2]==jog:
            velha[0][0]=jog
            
        elif velha[1][0]==jog and velha[1][1]==jog and velha[1][2]==" ":
            velha[1][2]=jog
        elif velha[1][0]==jog and velha[1][1]==" " and velha[1][2]==jog:
            velha[1][1]=jog 
        elif velha[1][0]==" " and velha[1][1]==jog and velha[1][2]==jog:
            velha[1][0]=jog 
            
        elif velha[2][0]==jog and velha[2][1]==jog and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[2][0]==jog and velha[2][1]==" " and velha[2][2]==jog:
            velha[2][1]=jog 
        elif velha[2][0]==" " and velha[2][1]==jog and velha[2][2]==jog:
            velha[2][0]=jog
            
        #Coluna
        elif velha[0][0]==jog and velha[1][0]==jog and velha[2][0]==" ":
            velha[2][0]=jog
        elif velha[0][0]==jog and velha[1][0]==" " and velha[2][0]==jog:
            velha[1][0]=jog 
        elif velha[0][0]==" " and velha[1][0]==jog and velha[2][0]==jog:
            velha[0][0]=jog
            
        elif velha[0][1]==jog and velha[1][1]==jog and velha[2][1]==" ":
            velha[2][1]=jog
        elif velha[0][1]==jog and velha[1][1]==" " and velha[2][1]==jog:
            velha[1][1]=jog 
        elif velha[0][1]==" " and velha[1][1]==jog and velha[2][1]==jog:
            velha[0][1]=jog 
            
        elif velha[0][2]==jog and velha[1][2]==jog and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[0][2]==jog and velha[1][2]==" " and velha[2][2]==jog:
            velha[1][2]=jog 
        elif velha[0][2]==" " and velha[1][2]==jog and velha[2][2]==jog:
            velha[0][2]=jog
            
        #Diagonal
        elif velha[0][0]==jog and velha[1][1]==jog and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[0][0]==jog and velha[1][1]==" " and velha[2][2]==jog:
            velha[1][1]=jog 
        elif velha[0][0]==" " and velha[1][1]==jog and velha[2][2]==jog:
            velha[0][0]=jog
        
        elif velha[0][2]==jog and velha[1][1]==jog and velha[2][0]==" ":
            velha[2][0]=jog
        elif velha[0][2]==jog and velha[1][1]==" " and velha[2][0]==jog:
            velha[1][1]=jog 
        elif velha[0][2]==" " and velha[1][1]==jog and velha[2][0]==jog:
            velha[0][2]=jog
        
        #**Defesa**
        #Linha
        elif velha[0][0]==jog1 and velha[0][1]==jog1 and velha[0][2]==" ":
            velha[0][2]=jog
        elif velha[0][0]==jog1 and velha[0][1]==" " and velha[0][2]==jog1:
            velha[0][1]=jog 
        elif velha[0][0]==" " and velha[0][1]==jog1 and velha[0][2]==jog1:
            velha[0][0]=jog
            
        elif velha[1][0]==jog1 and velha[1][1]==jog1 and velha[1][2]==" ":
            velha[1][2]=jog
        elif velha[1][0]==jog1 and velha[1][1]==" " and velha[1][2]==jog1:
            velha[1][1]=jog 
        elif velha[1][0]==" " and velha[1][1]==jog1 and velha[1][2]==jog1:
            velha[1][0]=jog 
            
        elif velha[2][0]==jog1 and velha[2][1]==jog1 and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[2][0]==jog1 and velha[2][1]==" " and velha[2][2]==jog1:
            velha[2][1]=jog 
        elif velha[2][0]==" " and velha[2][1]==jog1 and velha[2][2]==jog1:
            velha[2][0]=jog       

        #Coluna    
        elif velha[0][0]==jog1 and velha[1][0]==jog1 and velha[2][0]==" ":
            velha[2][0]=jog
        elif velha[0][0]==jog1 and velha[1][0]==" " and velha[2][0]==jog1:
            velha[1][0]=jog 
        elif velha[0][0]==" " and velha[1][0]==jog1 and velha[2][0]==jog1:
            velha[0][0]=jog
            
        elif velha[0][1]==jog1 and velha[1][1]==jog1 and velha[2][1]==" ":
            velha[2][1]=jog
        elif velha[0][1]==jog1 and velha[1][1]==" " and velha[2][1]==jog1:
            velha[1][1]=jog 
        elif velha[0][1]==" " and velha[1][1]==jog1 and velha[2][1]==jog1:
            velha[0][1]=jog 
            
        elif velha[0][2]==jog1 and velha[1][2]==jog1 and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[0][2]==jog1 and velha[1][2]==" " and velha[2][2]==jog1:
            velha[1][2]=jog 
        elif velha[0][2]==" " and velha[1][2]==jog1 and velha[2][2]==jog1:
            velha[0][2]=jog
            
        #Diagonal
        elif velha[0][0]==jog1 and velha[1][1]==jog1 and velha[2][2]==" ":
            velha[2][2]=jog
        elif velha[0][0]==jog1 and velha[1][1]==" " and velha[2][2]==jog1:
            velha[1][1]=jog 
        elif velha[0][0]==" " and velha[1][1]==jog1 and velha[2][2]==jog1:
            velha[0][0]=jog
        
        elif velha[0][2]==jog1 and velha[1][1]==jog1 and velha[2][0]==" ":
            velha[2][0]=jog
        elif velha[0][2]==jog1 and velha[1][1]==" " and velha[2][0]==jog1:
            velha[1][1]=jog 
        elif velha[0][2]==" " and velha[1][1]==jog1 and velha[2][0]==jog1:
            velha[0][2]=jog
            
        #Se Quarta jogada
        elif nJogadas==3: 
            
            if((velha[0][0]==jog1 and velha[2][2]==jog1) or (velha[0][2]==jog1 and velha[2][0]==jog1)):           
                linha = random.randrange(0,3)
                coluna = random.randrange(0,3)
                while ((linha!=0 or coluna!=1) and (linha!=1 or coluna!=0) and (linha!=1 or coluna!=2) and (linha!=2 or coluna!=1)) or (velha[linha][coluna]!=" "):
                    linha = random.randrange(0,3)
                    coluna = random.randrange(0,3)                    
                velha[linha][coluna] = jog
                
            elif((velha[0][0]!=" " and velha[2][2]!=" ") or (velha[0][2]!=" " and velha[2][0]!=" ")):           
                linha = random.randrange(0,3)
                coluna = random.randrange(0,3)
                while ((linha!=0 or coluna!=0) and (linha!=0 or coluna!=2) and (linha!=2 or coluna!=0) and (linha!=2 or coluna!=2)) or (velha[linha][coluna]!=" "):
                    linha = random.randrange(0,3)
                    coluna = random.randrange(0,3)                    
                velha[linha][coluna] = jog
                
            elif velha[1][1]==" ":
                    velha[1][1]=jog            
            
            elif velha[1][0]==" " and velha[1][2]==" ":
                velha[1][0]=jog
            elif velha[0][1]==" " and velha[2][1]==" ":
                velha[0][1]=jog
            elif velha[0][0]==" " and velha[2][2]==" ":
                soma=0
                for i in range(1, 3):
                    if velha[0][i]==jog1:
                        soma+=1
                    if velha[i][0]==jog1:
                        soma+=1
                if soma==2:
                    velha[0][0]=jog
                else:
                    velha[2][2]=jog
                                
            elif velha [0][2]==" " and velha[2][0]==" ":
                soma=0
                for i in range(2):
                    if velha[0][i]==jog1:
                        soma+=1
                    if velha[i+1][2]==jog1:
                        soma+=1
                if soma==2:
                    velha[0][2]=jog
                else:
                    velha[2][0]=jog
                    
            
        #Se quinta jogada        
        elif nJogadas==4 and velha[1][1]==" ": #and ((velha[0][0]==jog1 and velha[1][1]!=" ") or (velha[2][2]!=jog1 and velha[1][1]!=" ") or (velha[0][2]==jog1 and velha[1][1]!=" ") or (velha[2][0]!=jog1 and velha[1][1]!=" ")):
            velha[1][1]=jog
        
        #Se sexta jogada    
        elif nJogadas==5 and ((velha[0][0]==" " and velha[2][2]==" ") or (velha[2][0]==" " and velha[0][2]==" ")):
            soma=0
            vazio=0
            if velha[0][0]==" " and velha[2][2]==" ":
                
                for i in range(1, 3):
                    if velha[0][i]==jog1:
                        soma+=1
                    elif velha[0][i]==" ":
                        vazio+=1
                    if velha[i][0]==jog1:
                        soma+=1
                    elif velha[i][0]==" ":
                        vazio+=1
                if soma==2 and vazio==2:
                    velha[0][0]=jog
                else:
                    velha[2][2]=jog
            else:
                for i in range(2):
                    if velha[0][i]==jog1:
                        soma+=1
                    elif velha[0][i]==" ":
                        vazio+=1
                    if velha[i+1][2]==jog1:
                        soma+=1
                    elif velha[i+1][2]==" ":
                        vazio+=1
                if soma==2 and vazio==2:
                    velha[0][2]=jog
                else:
                    velha[2][0]=jog                                     
        
        else:            
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
            while velha[linha][coluna] != " ":           
                linha = random.randrange(0,3)
                coluna = random.randrange(0,3)
            velha[linha][coluna] = jog                    
        
        nJogadas+=1
        vez=1 if v==2 else 2        
        
    if nJogadas>=4 and vencedor=="":
        vitoria=verificar_vitoria()
        if vitoria==True:
            vencedor = v
            
def jogHumano(jog, v):
    global nJogadas
    global vez
    global vitoria
    global vencedor
    
    if vez==v and vitoria==False and nJogadas<9 and vencedor=="":
        linha = int(input("Informe a linha da jogada: "))
        coluna = int(input("Informe a coluna da jogada: "))
        while velha[linha][coluna] != " ":
            print("Essa posição já está selecionada!")            
            linha = int(input("Informe a linha da jogada: "))
            coluna = int(input("Informe a coluna da jogada: "))
            
        velha[linha][coluna] = jog
        nJogadas+=1
        
        if nJogadas>=4 and vencedor=="":
            vitoria=verificar_vitoria() 
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
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna] != " ":           
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
        velha[linha][coluna] = jog
        nJogadas+=1
        
    if nJogadas>=4 and vencedor=="":
        vitoria=verificar_vitoria()
        if vitoria==True:
            vencedor = v
                     
    vez=1 if v==2 else 2                            
    
def verificar_vitoria():
    global velha
    global vitoria
    simbolos = [simb1, simb2]
    
    for s in simbolos:
        #Linha
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            
            if(soma==3):
                vitoria=True
                break
            il+=1            
        
        #Colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            
            if(soma==3):
                vitoria=True
                break
            ic+=1    
                    
        #Diagonal
        soma=0
        diag=0
        
        while diag<3:
            if(velha[diag][diag]==s):
                soma+=1
            diag+=1
        if(soma==3):
            vitoria=True
            break
        
        soma=0
        diagL=0
        diagC=2
        
        while diagC>=0:
            if(velha[diagL][diagC]==s):
                soma+=1
            diagL+=1
            diagC-=1
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
    velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    
#Gerar arquivo exel    
def fileExel(jogar):
    global df
    if jogar==0:
        h = ["Partida", "Resultado", "Vitorias 1", "Vitorias 2", "Velhas"]
        df = pd.DataFrame(columns=h)        
        df.to_csv("dados.csv", sep=',', index=False)
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("dados.csv", sep=',', index=False)
    else:
        df.loc[jogar] = [jogar, vencedor, nVitorias1, nVitorias2, nEmpates]
        #print(df)
        df.to_csv("dados.csv", sep=',', index=False)
    

while jogar<10000:
    while True:
        
        #tabuleiro(velha)
        jogadorBrabo(simb1,2)
        #tabuleiro(velha)
        jogIniciante(simb2,1)        
        
        if (vitoria==True):
            #tabuleiro(velha)
            #print("*"*30)
            #print(f"Parabens '{vencedor}' foi o vencedor!")
            #print("*"*30)
            if vencedor==1:
                nVitorias1+=1
            elif vencedor==2:
                nVitorias2+=1
            fileExel(jogar)
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
    print(jogar)
    #jogar = input("Deseja jogar novamente?(s/n): ")
    resetar()
    
print("Vitorias jogador 1: " + str(nVitorias1))
print("Vitorias jogador 2: " + str(nVitorias2))
print("Empates: " + str(nEmpates))
fim = time.time()
print(f"Tempo total: {((fim-inicio)):.3f}")
