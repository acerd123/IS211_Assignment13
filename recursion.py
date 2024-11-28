


def fibonacci(n):
    
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
   
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
   
    if not s1 and not s2:  
        return 0
    if not s1:  
        return -1
    if not s2:  
        return 1

    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == "__main__":
    
    print("Fibonacci Sequence:")
    for i in range(1, 11):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    
    print("\nEuclid's GCD Algorithm:")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"gcd(101, 103) = {gcd(101, 103)}")

    
    print("\nString Comparison:")
    print(f'compareTo("apple", "banana") = {compareTo("apple", "banana")}')
    print(f'compareTo("grape", "grape") = {compareTo("grape", "grape")}')
    print(f'compareTo("zebra", "aardvark") = {compareTo("zebra", "aardvark")}')
