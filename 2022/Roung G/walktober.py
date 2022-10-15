for case in range(int(input())):
    M, N, P = input().split()
    x = [[int(j) for j in i] for i in [input().split() for _ in range(int(M))]]
    steps = 0
    for col in range(int(N)):
        stepsX = (max([(x[i][col]) for i in range(int(M))])) - x[int(P)-1][col]
        steps += (stepsX if  stepsX > 0 else 0)
    print(f'Case #{case + 1}: {steps}')