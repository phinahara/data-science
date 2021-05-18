# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

def increments(L): return [i+1 for i in L]

def cubes(L): return [i**3 for i in L]

## 1: (Problem 0.8.3) Tuple Sum
def tuple_sum(A, B): return [(A[i][0]+B[i][0],A[i][1]+B[i][1]) for i in range(len(A))]

    



## 2: (Problem 0.8.4) Inverse Dictionary
def inv_dict(d): return {d[key]:key for key in d.keys()}

    



## 3: (Problem 0.8.5) Nested Comprehension
def row(p, n): return [p+i for i in range(n)]

    

comprehension_with_row = [row(i,20) for i in range(15)]

comprehension_without_row = [[j+i for i in range(20)] for j in range(15)]





## 4: (Problem 0.8.10) Probability Exercise 1
Pr_f_is_even = 0.7
Pr_f_is_odd  = 0.3


## 5: (Problem 0.8.11) Probability Exercise 2
Pr_g_is_1    = .4
Pr_g_is_0or2 = .6

