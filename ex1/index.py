#No restaurante "Quilão do Andrezão" existe uma promoção: Os clientes cujos pratos ultrapassarem 1kg pagam um valor único de R$80,00.
#Crie um programa que receba o peso do prato do cliente, o valor cobrado por kg e exiba o total do prato e se o cliente tem direito a pagar o valor único.

print("Quilão do Andrezão")
peso_prato = float(input("Por favor, conforme o peso do prato em kg: "))
valor_quilo = float(input("Por favor, informe o valor cobrado por kg: "))

valor_total = peso_prato * valor_quilo

print(f"Para este prato, o valor cbrado é de R${valor_total:.2f}")

if peso_prato >= 1: 
    print("Mas, como o prato ultrapassou 1kg e, portanto, o cliente só pagará o valor fixo de R$80,00")