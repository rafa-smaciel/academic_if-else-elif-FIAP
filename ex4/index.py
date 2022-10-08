#Um sistema precisa fazer o controle de usuários que acessam com base no username e no password.
#Só deverá ser "logado" no sistema o usuário "admin" com senha "123".

print("Sistema de Controle de Usuário")

usuario = "admin"
senha = "123"

usuario_digitado = input("Digite usuario: ")
senha_digitado = input("Digite senha: ")

if usuario_digitado == "admin" and senha_digitado == "123":
    print("Usuário e senha corretos")
else:print("usuarios e senhas incorretas")
    