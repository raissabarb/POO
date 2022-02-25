class Criptografia:
    def __init__(self):
        pass

    def criptografar(self, param):
        abrir_arq = open('mensagem.txt', 'r')
        msg_criptograf = ''
        with abrir_arq as file:
            for line in file:
                for letter in line:
                    novo_caract = chr(ord(letter) + int(param))
                    num_novo_caract = ord(novo_caract)
                    if num_novo_caract >= 127:
                        cont = num_novo_caract - 127
                        caract_alterado = chr(cont)
                        msg_criptograf = msg_criptograf + caract_alterado
                    else:
                        msg_criptograf = msg_criptograf + novo_caract
        return msg_criptograf


parametro = input('Digite um número que será usado como parâmetro: ')
msg = Criptografia()
criptog = msg.criptografar(parametro)
msg_criptografada = open('criptografia.txt', 'w+')
msg_criptografada.write(criptog)
