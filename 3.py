import numpy as np
def levenshtein(s1,s2):
    sizex=len(s1)+1
    sizey=len(s2)+1
    matrix=np.zeros((sizex,sizey))
    for x in range(sizex):
        matrix[x,0]=x
    for y in range(sizey):
        matrix[0,y]=y

    for x in range(1,sizex):
        for y in range(1,sizey):
            if s1[x-1]==s2[y-1]:
                matrix[x,y]=min(matrix[x-1,y-1]+1,matrix[x,y-1]+1)
            else:
                matrix[x,y]=min(matrix[x-1,y]+1,matrix[x,y-1]+1)
    print(matrix)
    return (matrix[sizex-1,sizey-1])

levenshtein("hello","hello")
