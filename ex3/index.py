#Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32kg sem nenhum custo adicional, enquanto os clientes do tipo gold podem levar malas de até 280kg sem nenhum custo adicional e todos os demais pagam por qualquer bagagem despachada.
#Com base no tipo do cliente e no peso informado da bagagem, podemos informar se ela está ou não nos lmites estabalecidos.

print("Limites de Kg")
limite_peso_premium = int(32)
limite_peso_gold = int(28)
limite_peso_geral = int(0)

tipo_cliente = input("Informar tipo de cliente: ")

peso_bagagem = int(input("Informe o peso da bagagem: "))

diferenca_reducao_premium = peso_bagagem - limite_peso_premium
diferenca_reducao_gold = peso_bagagem - limite_peso_gold

if tipo_cliente.lower() == "premium":
    if peso_bagagem > limite_peso_premium:
        print(f"Limite excedido para as regras de cliente premium. Por favor reduza sua bagagem em {diferenca_reducao_premium:.1f}kg, ou pague a diferença.") 
    else:print("Dentro dos limites")
elif tipo_cliente.lower() == "gold":
    if peso_bagagem > limite_peso_gold:
        print(f"Limite excedido para as regras de cliente gold. Por favor reduza sua bagagem em {diferenca_reducao_gold:.1f}kg, ou pague a diferença.") 
    else:print("Dentro dos limites")
elif tipo_cliente.lower() == "geral":
    print(f"Não há tolerância de peso para tipo geral. Pagar pelo transporte das bagagens. {peso_bagagem:.0f}kg") 
        