T = int(input())
for i in range(T):
    a,b = input().split()

    try :
        print(int(a) // int(b))
    except ZeroDivisionError :
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")