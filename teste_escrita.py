contatos = open("dados/contatos.csv", encoding="Latin_1", mode="a+")

contatos.write("1, Bento José, bento@jose.com.br\n")
contatos.write("2, Inácio Francisco, inacio@francisco.com.br\n")

contatos.flush()

contatos.seek(0)

for linha in contatos :
    print(linha, end="")