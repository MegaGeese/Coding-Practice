def stepOne(tree):
    output = [tree[0][0]]

    for i in tree[0]:
        for j in tree[1]:
            output.append(i * j)
            for k in tree[2]:
                output.append(i * j * k)
                for l in tree[3]:
                    output.append(i * j * k * l)
                    for m in tree[4]:
                        output.append(i * j * k * l * m)
                        for n in tree[5]:
                            output.append(i * j * k * l * m * n)
                            for o in tree[6]:
                                output.append(i * j * k * l * m * n * o)
    return output

def stepTwo(products):
    for i in range(len(products)):
        if i % 2 == 0 and i < len(products) - 1:
            products[i], products[i + 1] = products[i + 1], products[i]

    return products[::-1]

def stepThree(products):
    character = []
    for i in products:
        order = i % 26 + 97
        character.append(order)

    return character

def stepFour(character):
    a = ''
    b = ''
    char = ''
    bitwiseAnd = ''

    for i in character:
        char += str(bin(i)[2:])

    a = char[:16]
    b = char[-16:]

    for i in range(len(a)):
        bitA = a[i]
        bitB = b[i]

        if bitA == bitB and bitA == '1':
            bitwiseAnd += '1'
        else:
            bitwiseAnd += '0'

    return int(bitwiseAnd, 2)

def stepFive(value):
    value = str(value)
    total = 0

    for i in range(0, len(value), 2):
        total += int(value[i:i+2])

    return str(total)

def stepSix(total):
    a = 365 ** 5
    b = 52 ** 10
    c = 7 ** 20
    d = -457981573849226022
    return -(a + b + c - d - int(total))

def stepSeven(SBS):
    SBS = str(SBS)
    key = ''

    for i in range(0, len(SBS), 2):
        key += chr(int(SBS[i:i+2]) % 26 + 97)

    return key



temp = []

example = [[15], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[8], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[20], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[1], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[12], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[17], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[8], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))
example = [[9], [3, 20, 18, 4, 14, 12, 3], [9, 16, 11, 18, 18, 16, 7, 19], [14, 10, 14, 1, 14, 13, 2, 14], [2, 15, 14, 11], [16, 8, 18, 20, 2, 3], [20, 6, 14, 18, 16, 19]]
temp.append(stepFive(stepFour(stepThree(stepTwo(stepOne(example))))))

result = ''.join(temp)
print(stepSeven(stepSix(result)))

"""

products = stepOne(example)
products = stepTwo(products)
character= stepThree(products)
value = stepFour(character)
total = stepFive(value)
key = stepSix(total)
key = stepSeven(key)


"""