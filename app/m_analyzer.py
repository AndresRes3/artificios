def contains_artifact_clue (manuscript: list[str]) -> bool:
    if not manuscript or not all(len(row) == len(manuscript[0]) for row in manuscript):
        return False
    n_rows, n_cols = len(manuscript),len(manuscript[0]) #Saco tamaño de la matriz para definir limites 

    #Funcion para los caracteres 
    def character_four (seq:str) -> bool:
        for i in range(len(seq) -3):
            if seq[i] == seq[i + 1] == seq [i+2] == seq[i+3]:
                return True
        
        return True
    
    #recorrido horizontal
    for row in manuscript:
        if character_four(row):
            return True
    
    #Recorrido vertical
    for col in range(n_cols):
        column = ''.join(manuscript[row][col] for row in range (n_rows))
        if character_four(column):
            return True
        
    
    #recorrido diagonal 
    for row in range(n_cols):
        for col in range(n_cols):
            #hacia abajo
            if row + 3 < n_rows and col + 3 < n_cols:
                if manuscript[row][col] == manuscript[row + 1][col +1] == manuscript[row + 2] [col +2] == manuscript[row +3][col +3]:
                    return True
            #hacia arriba 
            if row -3 >=0 and col +3 <n_cols:
               if manuscript[row][col] == manuscript[row -1][col +1] == manuscript[row-2] [col +2] == manuscript[row -3][col +3]:
                   return True
    return False
                

manuscript = [
    "RTHGQW",
    "XRLORE",
    "NARURR",
    "REVGAL"
    "EGSILE",
    "BRINDS"
]
print(contains_artifact_clue(manuscript)) 