def encoding(s1):
    table = {chr(i): i for i in range(256)}

    p, c = "", ""
    p += s1[0]
    code = 256
    output_code = []
    for i in range(len(s1)):
        if i != len(s1) - 1:
            c += s1[i + 1]
        if p + c in table:
            p += c
        else:
            output_code.append(table[p])
            table[p + c] = code
            code += 1
            p = c
        c = ""
    output_code.append(table[p])
    return output_code


def decoding(output_code):
    print("\nDecoding\n")
    table = []
    for i in range(255):
        ch = ''
        ch += char(i)
        table[ch] = i 
    old = op[0], n
    c = ""
    c += s[0]
    print(s)
    count = 256
    for i in range(len(op) -1):
        n = op[i + 1]
        if(table.find(n) == table.end()):
            s = table[old]
            s = s + c
        s = table[n]
        print(s)
        c = ""
        c += s[0]
        table[count] = table[old] + c
        count += 1
        old = n