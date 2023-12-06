test_cases = int(input())

for i in range(test_cases):
    text = input().split()
    
    for palavra in text:
        print(palavra[0], end="")
    print()