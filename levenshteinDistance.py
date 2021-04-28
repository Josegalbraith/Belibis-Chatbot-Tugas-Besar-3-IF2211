def levenshteinDistance(stringA,stringB):
    distanceMatrix = [[0 for j in range(len(stringA)+1)] for i in range(len(stringB)+1)]
    for i in range(len(stringB)+1):
        for j in range(len(stringA)+1):
            if j == 0:
                distanceMatrix[i][j] = i
            if i == 0:
                distanceMatrix[i][j] = j
            if (j-1 >= 0 and i!= 0):
                distanceMatrix[i][j] = min(distanceMatrix[i][j-1], distanceMatrix[i-1][j-1],distanceMatrix[i-1][j])
                if (stringA[j-1] != stringB[i-1]):
                    distanceMatrix[i][j] += 1 
    return distanceMatrix[len(stringB)-1][len(stringA)-1]

def missWordRecc(text, kataPenting, missThreshold):
    result = []
    for mismatch in (text.split()):
        for keyword in kataPenting:
            editDistance = levenshteinDistance(mismatch,keyword)
            mismatchPercentage = float(editDistance/max(len(keyword),len(mismatch)))
            if (mismatchPercentage <= missThreshold):
                result.append(keyword)
    return result