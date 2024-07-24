def main():
    x, y, z = input('Expression: ').split(' ') # Takes user input expression string and splits it into three different variables with whitespace passed as an argument for split() to say it is a seperator
    x = float(x) # assign x and z as floats of their strs
    z = float(z)
    if y == '+': # else-of control flow that checks what operator the user intended and uses that operator in the eval of x and z
        evalOutput = x + z
    elif y == '-':
        evalOutput = x - z
    elif y == '*':
        evalOutput = x * z
    else:
        evalOutput = x / z

    print(evalOutput)

main()
