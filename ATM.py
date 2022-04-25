def solve(n):
    counter = 0
    banknotes = [10,20,50,100,200,500]
    i = 5
    if n%10 != 0:
        return -1
    else:
        while n!=0:
            if n - banknotes[i] >= 0:
                counter += n//banknotes[i]
                n -= banknotes[i]*(n//banknotes[i])
            i -= 1
        return counter


print(solve(1550))


