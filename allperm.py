# Assignment 7, Task 1
# Name: Anuvit Kulanusataporn
# Collaborators: 
# Time Spent: -

def all_perm(n):
    if n == 1:
        return {(1,)}
    if n == 2:
        return {(1,2),(2,1)}
    else:
        result = all_perm(n-1)
        give_out = []
        for this_perm in result:
            for j in range(n):
                small_container = ()
                index = 0
                for k in range(n):
                    if k == j:
                        small_container += (n,)
                    else:
                        small_container += (this_perm[index],)
                        index += 1
                give_out.append(small_container,)
        return set(give_out)