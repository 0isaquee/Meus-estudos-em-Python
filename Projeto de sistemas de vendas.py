estoque = ["Parafuso", "Arruela", "Martelo"]
quant0 = 35
quant1 = 90
quant2 = 10
formas = ["pix", "cartão de débito", "cartão de crédito", "dinheiro"]
total_geral = 0
#Apresentação da loja, pedido do cliente, quantidade de itens e total de cada item
print("Olá, somos a loja de materiais para instalação e reparo de imóveis")

while True:
    pedido_cliente = input("\nO que você deseja?: ").capitalize()

    if pedido_cliente == "pagar":
        break

    if pedido_cliente in estoque:
        print("Temos sim, vamos apenas checar o estoque.")
        
        # Lógica de preços e quantidades
        if pedido_cliente == estoque[0]:
            preco_unitario = 0.50
            print(f"Temos {quant0} {pedido_cliente}s")
        elif pedido_cliente == estoque[1]:
            preco_unitario = 0.25
            print(f"Temos {quant1} {pedido_cliente}s")
        else:
            preco_unitario = 20.00
            print(f"Temos {quant2} {pedido_cliente}s")

        escolha_c = int(input(f"Quantos(a) {pedido_cliente}s você deseja? ")) 

        if escolha_c <= 50:
            print("Temos essa quantidade!")
            
            valorT = escolha_c * preco_unitario
            total_geral += valorT
            print(f"Subtotal: R$ {valorT:.2f}")

            return_c = input("Deseja adicionar mais alguma coisa? (sim/nao): ")
            if return_c.lower() != "sim":
                break
        
        elif escolha_c < 10:
            print("Não vendemos abaixo de 10 unidades.")
        else:
            print("Não vendemos acima de 50 unidades.") 
    else:
        print("Não temos este produto.")

#Valor final e forma de pagamento
if total_geral > 0:
    while True:   
        forma_pay = input(f"\nO total da compra ficou em R$ {total_geral:.2f}. Qual a forma de pagamento? ")
        if forma_pay.lower() in formas:
            print(f"Certo, processando o pagamento...")      
            print("Tudo certo, obrigado e tenha um bom dia!")
            break
        else:
            print("Forma de pagamento inválida. Aceitamos: pix, dinheiro e cartões.")