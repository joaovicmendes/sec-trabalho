import codecs
from fixed_xor import fixed_xor
THRESHOLD = 1.0001

def char_frequecy(text):
    '''
        Dado um texto, retorna um dicionário com pares 'caracter': 'frequencia',
        onde frequencia é (número de ocorrências) / (caracteres unicos no texto).
    '''
    frequency_list = {}
    for char in text:
        if char in frequency_list:
            frequency_list[char] += 1
        else:
            frequency_list[char] = 1
    for key in frequency_list:
        frequency_list[key] = frequency_list[key]/len(frequency_list)
    return frequency_list


def padd_hex_string(hex_string, lenth):
    '''
        Dado uma string de um número hexadecimal, replica seu valor até que tenha o
        comprimento informado.
    '''
    if len(hex_string) == 1:
        hex_string = '0' + hex_string
    return hex_string*(lenth//2)


def is_text(text, alphabet_frequency_list):
    '''
        Dado um texto e uma lista de frequências de caracter de determinado idioma,
        retorna uma probabilidade desse texto ser uma frase no idioma.
    '''
    fitness = 0
    text_frequency = char_frequecy(text)

    for key in alphabet_frequency_list:
        if key not in text_frequency.keys():
            text_frequency[key] = 0
        fitness += abs( text_frequency[key] - alphabet_frequency_list[key] )

    return fitness/len(alphabet_frequency_list)


def single_byte_xor_cipher(buffer, frequency_list):
    prob_list = []
    answer    = []
    for i in range(256):
        # Deixando a chave com o mesmo tamanho do buffer
        hex_str = padd_hex_string(hex(i)[2:], len(buffer))

        # Gerando texto plano
        try:
            plain_text = codecs.decode(fixed_xor(buffer, hex_str))
            fitness = is_text(plain_text, frequency_list)
        except:
            fitness = float('inf')

        # Guardando tuplas (texto, chave, fit)
        encryption_key = chr(i)
        prob_list.append((fitness, plain_text, encryption_key))

    # Filtrando as strings cujo fitness está a um limiar de distancia do mínimo
    min_fitness = min(prob_list)[0]
    for prob, txt, key in prob_list:
        if prob < min_fitness*THRESHOLD:
            answer.append((txt, key))
    return answer

def main():
    # Char frequency from an external piece of text
    with open("message.txt") as text:
        text = text.read()
    frequency_list = char_frequecy(text)

    # Decrypting key
    encrypted = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    candidates = single_byte_xor_cipher(encrypted, frequency_list)
    for candidate in candidates:
        # print(candidate)
        print('Texto plano:     ' + candidate[0])
        print('Chave candidata: ' + candidate[1])
        print("===")

if __name__ == "__main__":
    main()
