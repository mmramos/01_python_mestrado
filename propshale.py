import numpy as np

def rhosh(RHOb,PHIN,pma,pf):
    
    print
    print "f(RHOb,PHIN,RHOmatriz,RHOfluido,DTPmatriz,DTPfluido)"
    
    phi_t_D   = [] # Porosidade Total (perfil Densidade)
    phi_dif_a = [] # Diferenca (porosidade total(D) - Porosidade Neutronica)
    
    for i in range (len(PHIN)):
        
        # ----------------------------- Calculo da Porosidade total -----------------------------------
        
        phi_t_D0 = (RHOb[i] - pma)/(pf - pma)  # Porosidade total - perfil densidade
        phi_t_D.append(phi_t_D0)
        
        phi_dif_a0 = PHIN[i] - (phi_t_D0*100)
        
        phi_dif_a.append(phi_dif_a0)
        
        # ---------------------------------------------------------------------------------------------
    
    for i in range (len(phi_dif_a)):
        if phi_dif_a[i] == max(phi_dif_a): 
            locmax2 = i
            
    psh = RHOb[locmax2]
    print
    print psh, 'g/cm3 densidade do folhelho'
    print locmax2,'posicao do max(PHI_n - PHI_T_D)'
    print max(phi_dif_a),'valor max da diferenca'
    
    return psh

def dtpsh(RHOb,DTP,PHIN,pma,pf):
    
    print
    print "f(RHOb,DTP,PHIN,RHOmatriz,RHOfluido)"
    
    phi_t_D   = [] # Porosidade Total (perfil Densidade)
    phi_dif_a = [] # Diferenca (porosidade total(D) - Porosidade Neutronica)
    
    for i in range (len(PHIN)):
        
        # ----------------------------- Calculo da Porosidade total -----------------------------------
        
        phi_t_D0 = (RHOb[i] - pma)/(pf - pma)  # Porosidade total - perfil densidade
        phi_t_D.append(phi_t_D0)
        
        phi_dif_a0 = PHIN[i] - (phi_t_D0*100)
        
        phi_dif_a.append(phi_dif_a0)
        
        # ---------------------------------------------------------------------------------------------
    
    for i in range (len(phi_dif_a)):
        if phi_dif_a[i] == max(phi_dif_a): 
            locmax2 = i
            
    dtsh = DTP[locmax2]
    print
    print dtsh, 'us/ft vagarosidade do folhelho'
    print locmax2,'posicao do max(PHI_n - PHI_T_D)'
    print max(phi_dif_a),'valor max da diferenca'
    
    return dtsh