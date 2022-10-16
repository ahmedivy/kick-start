def subarrays(array):
    return [array[j:i] for i in range(len(array) + 1) for j in range(i)] 

def isHappy(array):
    return all([(sum(subarray[0:i]) >= 0) for i in range(len(array)+1)])

for case in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    happySum = 0
    for subarray in subarrays(A):
        if isHappy(subarray):
            happySum += sum(subarray)
    print(f'Case #{case+1}: {happySum}')
