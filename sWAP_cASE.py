def swap_case(s):
    result = ''
    for char in s:
        if 'a' <= char <='z':
            result += chr(ord(char) - 32)
        elif  'A'<= char <='Z':
            result += chr(ord(char) + 32)
        else :
            result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)