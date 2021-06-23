import codecs

def hex_to_b64(encoded_hex):
    decoded = codecs.decode(encoded_hex, 'hex')
    print(decoded)
    b64 = codecs.encode(decoded, 'base64')
    return b64.decode()

encoded_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
transformed = hex_to_b64(encoded_hex)
print(transformed)
