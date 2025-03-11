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
    

