def generate(numRows):
    soln = []
    for i in range(numRows):
        ans = []
        if (i == 0):
            ans.append(1)
            # continue

        elif (i == 1):
            ans.append(1)
            ans.append(1)
            # continue
        else:  
            for j in range(i+1):
                if (j == 0 or j == i): 
                    ans.append(1)
                else:
                    # print(i, j)
                    # print(soln[i-1])
                    ans.append(soln[i-1][j-1] + soln[i-1][j])

        soln.append(ans)

    print(soln)



generate(30)