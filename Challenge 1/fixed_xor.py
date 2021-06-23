import codecs

def fixed_xor(buff1, buff2):
    buff1 = bytes.fromhex(buff1)
    buff2 = bytes.fromhex(buff2)

    answer = b''
    for b1, b2 in zip(buff1, buff2):
        answer += bytes([b1^b2])

    answer = codecs.encode(answer, 'hex')
    return answer.decode()

xord = fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print(xord)
print(codecs.decode(xord, 'hex'))
