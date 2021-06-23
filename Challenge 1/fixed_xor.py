import codecs

def fixed_xor(buff1, buff2):
    buff1 = bytes.fromhex(buff1)
    buff2 = bytes.fromhex(buff2)

    answer = b''
    for b1, b2 in zip(buff1, buff2):
        answer += bytes([b1^b2])

    return answer

# # Solution to Challenge 2
# xord = fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
# print(codecs.decode(xord))
# print(codecs.encode(xord, 'hex'))
