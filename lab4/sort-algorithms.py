# Name: Ruoling Yu
# Student Number: 500976267
# Q1 - Advanced Sorting Algorithms

def radixSort(vectors):
    digits = len(vectors[0])
    vecNum = len(vectors)
    for i in range(digits - 1, -1, -1):
        tempArr = [0 for i in range(vecNum)]
        countArr = [0 for a in range(10)]
        for j in range(vecNum):
            vec = vectors[j]
            digit = vec[i]
            countArr[digit] += 1
        for k in range(len(countArr)):
            if k != 0:
                countArr[k] = countArr[k-1] + countArr[k]
        for l in range(vecNum - 1, -1, -1):
            countArr[vectors[l][i]] -= 1
            index = countArr[vectors[l][i]]
            tempArr[index] = vectors[l]
        vectors = tempArr
    return(vectors)
    
vectors = []
print('Input')
num = int(input())
for i in range(num):
    vector_str = input()
    digits = vector_str.split()
    digits = list(map(int, digits))
    vectors.append(digits)

vectors = radixSort(vectors)

print('Output')
for i in range(len(vectors)):
    num = ''
    for j in range(len(vectors[i])):
        num += str(vectors[i][j]) + ";"
    print(num)


