# Your code here
#n = 4
#i = 1
#matriz = []
def matrix_builder(n):
    matrix = [] 

    for i in range(n):
        row = []
        for j in range(n):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(3)

print(result)

#n = 4
#i = 1
#matriz = []
#def matrixBuilder(n):
#    matriz = []
#    matriz = [[i for columna in range(n)] for fila in range(n)]
#    return matriz
#
#print(matriz)