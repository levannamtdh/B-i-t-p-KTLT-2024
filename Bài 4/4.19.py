print("Sinh vien: Le Van Nam")
print("MSSV: 235752021610085")
print("################################")
#########################################

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False  
    return [x for x in range(2, limit + 1) if is_prime[x]]
limit = 10**6
P = tuple(sieve_of_eratosthenes(limit))
print(len(P))
print(P[:10])  

    
    





