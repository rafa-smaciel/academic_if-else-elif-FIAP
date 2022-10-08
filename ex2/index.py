#No saldão da alegria os clientes podem pagar de duas formas: Boleto Bancário ou Cartão de Crédito.
#Caso escolham pagar por boleto, os clientes tem desconto de 5% no valor da sua compra. Caso escolham pagar por cartão de crédito, não tem direito a desconto, mas podem indicar o número de parcelas.
#Escreva um programa que leia o total da compra, a forma de apgamento e faça as devidas exibições.

print("Saldão da Alegria")

totaldascompras = float(input("Digite o valor da compra R$: "))

formadepagamento = input("Escolha a forma de pagamento: ")

if formadepagamento == "boleto":
    comprascomdesconto = totaldascompras * 0.95
    print(f"O valor das compras com desconto é R$: {comprascomdesconto:.0f}")
elif formadepagamento == "cartao":
    numerodeparcelas = int(input("Escolha o número de parcelas: "))
    valordasparcelas = totaldascompras / numerodeparcelas
    print(f"O valor das parcelas é R$: {valordasparcelas:.0f}")
else:print("Digite uma condição de pagamento válida")
    
print("Próximo cliente!")
                             
    