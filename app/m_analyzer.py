def contains_artifact_clue(manuscript: list[str]) -> bool:
    if not manuscript or not all(len(row) == len(manuscript[0]) for row in manuscript):
        return False

    n_rows, n_cols = len(manuscript), len(manuscript[0])  # Tamaño de la matriz para definir límites

    #Funcion para los caracteres 
    def character_four(seq: str) -> bool:
        for i in range(len(seq) - 3):
            if seq[i] == seq[i + 1] == seq[i + 2] == seq[i + 3]:
                return True
        return False 

    # Recorrido horizontal
    for row in manuscript:
        if character_four(row):
            return True

    # Recorrido vertical
    for col in range(n_cols):
        column = ''.join(manuscript[row][col] for row in range(n_rows))
        if character_four(column):
            return True

   # Diagonal hacia abajo (Izq-Der, \\)
    for row in range(n_rows - 3):
        for col in range(n_cols - 3):
            diag = [manuscript[row][col], manuscript[row + 1][col + 1], 
                    manuscript[row + 2][col + 2], manuscript[row + 3][col + 3]]
            #print(f"Diagonal \\ en ({row},{col}): {diag}")  #DEBUG
            if diag[0] == diag[1] == diag[2] == diag[3]:
                return True

# Diagonal hacia arriba (Der-Izq, //)
    for row in range(3, n_rows):  # Empezamos desde la fila 3 para evitar índices negativos
        for col in range(n_cols - 3):
            diag = [manuscript[row][col], manuscript[row - 1][col + 1], 
                    manuscript[row - 2][col + 2], manuscript[row - 3][col + 3]]
            #print(f"Diagonal / en ({row},{col}): {diag}")  # DEBUG
            if diag[0] == diag[1] == diag[2] == diag[3]:
                return True
    return False