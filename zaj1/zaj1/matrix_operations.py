def mat_mul(A,B):
    result = []
    for i in range(0, len(A)):
        result.append([])
        for k in range(0,len(B[0])):
            v = 0
            for j in range(0, min(len(A[i]), len(B))):
                v+=A[i][j]*B[j][k]
            result[i].append(v)
    return result
