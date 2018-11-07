
class Usuario:
    def __init(self):
        self.email = ""
        self.senha = ""
    def __str__(self):
        return "email =" + self.email


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    linhas = arquivo.readlines()

    usuarios = []
    for linha in linhas:
        linha = linha.replace("\n", "")
        lista_u = linha.split(";")
        usuario = Usuario()
        usuario.email = lista_u[0]
        usuario.senha = lista_u[1]
        usuarios.append(usuario)

    arquivo.close()
    return usuarios


def criar_usuario(email, senha):
    usuario = Usuario()
    usuario.email = email
    usuario.senha = senha
    return usuario


def esta_logado(usuario, usuarios):
    encontrado = False
    for u in usuarios:
        if usuario.email == u.email and usuario.senha == u.senha:
            encontrado = True
    return encontrado


usuarios = ler_arquivo("usuarios.csv")


email = input("Email: ")
senha = input("Senha: ")

usuario = criar_usuario(email, senha)

logado = esta_logado(usuario, usuarios)

print(logado)
*professor o senhor pode colocar também o arquivo usuarios.csv* "valeu luis" 
