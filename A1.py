m = [ [1, 0, 2, 0, 1],  
      [0, 9, 2, 1, 3],  
      [1, 0, 1, 9, 2],  
      [9, 3, 0, 2, 1],  
      [0, 1, 2, 0, 9] ]
rua = 0
Casa= 0
Hospital = 0 
Gerador_emergência = 0 
Areadestr_ = 0
for linha in (range(len(m))):

    for coluna in (range(len(m[linha]))):
        print(m[linha][coluna], end=' ' )
        if m[linha][coluna] == 0:
            rua += 1
        if m[linha][coluna] == 1:
            Casa += 1     
        if m[linha][coluna] == 2:
            Hospital += 1 
            seguro = True    
            energia = True
            if coluna+1 < len(m): 
                if m[linha][coluna +1] == 9:
                    seguro = False                
            if coluna-1 > (0): 
                if m[linha][coluna -1] == 9:
                   seguro = False 
            if linha+1 < len(m): 
                if m[linha+1][coluna] == 9:
                    seguro = False
            if linha-1 > (0): 
                if m[linha -1][coluna] == 9:
                    seguro = False
            if seguro:        
                print(f"Hospital em{linha,coluna} SEGURO")
            else :
                print(f"Hospital em{linha,coluna}:EM PERIGO! Vizinho destruído detectado.")
        if m[linha][coluna] == 3:
            Gerador_emergência += 1
            if m[linha][coluna] == 3:
            
            
        if energia:        
                print(f"Hospital em{linha,coluna} SEGURO")
        else :
                print(f"Hospital em{linha,coluna}:EM PERIGO! Vizinho destruído detectado.")
            
            
            
            
            
            
                
        if m[linha][coluna] == 9:
            Areadestr_ += 1     
    print("\n")       
p =("Rua "+(str(rua))), ("Casa "+(str(Casa))),("Hospital "+(str(Hospital))),("Gerador_emergência "+(str(Gerador_emergência))),("Areadestr_ "+(str(Areadestr_)))
print(p)          














