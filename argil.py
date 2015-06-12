import numpy as np

def igr(GR):
    
    print "Equacao com 1 parametro, indique apenas uma unidade de GR (Raio Gama)"
    print

    IGR_Schlumberger = []   #Indice de Raio Gama
        
    for i in range (len(GR)):      
        
        if GR[i] == min(GR): 
            GR_locmin = i # determina a posicao do valor minimo do Gama Ray no perfil
        if GR[i] == max(GR):
            GR_locmax = i # determina a posicao do valor maximo do Gama Ray no perfil
            
        IGR0 = (GR[i] - min(GR))/(max(GR) - min(GR)) # Indice de Raio Gama (basica, Schlumberger)
        IGR_Schlumberger.append(IGR0)
        
    print "O indice de raio gama pussui a variavel IGR_Schlumberger e tem media",np.median(IGR_Schlumberger)
    print

    return IGR_Schlumberger

def larionov(GR):
    
    print "Equacao com 1 parametro, indique apenas uma unidade de GR (Raio Gama)"
    print

    IGR_Schlumberger = []   #Indice de Raio Gama
    VSH_Larionov     = []   #Argilosidade Larionov
        
    for i in range (len(GR)):      
        
        if GR[i] == min(GR): 
            GR_locmin = i # determina a posicao do valor minimo do Gama Ray no perfil
        if GR[i] == max(GR):
            GR_locmax = i # determina a posicao do valor maximo do Gama Ray no perfil
            
        IGR0 = (GR[i] - min(GR))/(max(GR) - min(GR)) # Indice de Raio Gama (basica, Schlumberger)
        
        Larionov0 = 0.083*((2**(3.70*IGR0))-1)       # Correcao de Larionov para Argilosidade
        VSH_Larionov.append(Larionov0)
        
    print "A correcao de Larionov possui a variavel VSH_Larionov e tem media",np.median(VSH_Larionov)
    print
        
    return VSH_Larionov
