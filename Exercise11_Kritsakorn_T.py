user_input = int(input())

for i in range(user_input):
    i+=1
    print(" " * (user_input - i) + "*" * ((i*2)-1))
