# Infix to postfix conversion

strings_to_convert = []
for _ in range(int(input())):
    strings_to_convert.append(str(input()))
# (a+(b*c)) -> abc*+
result = []
letters = 'abcdefghijklmnopqrstuvwxyz'
for string in strings_to_convert:
    stack = []
    r = ''
    for i in string:
        if i in letters:
            r += i
        elif i == '(':
            stack.append(i)
        elif i not in letters and i != ')':
            stack.append(i)
        elif i == ')':
            for j in stack:
                r += stack[-1]
                stack.pop()
                if j == '(':
                    stack.pop()
                    break
    result.append(r)
for i in result:
    print(i)
