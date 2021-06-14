Lista_1 = [[2,4,2],[9,6,4],[6,7,3]]
Lista_2 = [[4,5,10],[89,4,12],[9,5,4]]
Lista = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            
            Lista[i][j]+= (Lista_1[i][k] * Lista_2[k][j])
        print (Lista[i][j])
            
            
print(Lista)