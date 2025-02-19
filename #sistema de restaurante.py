#sistema de restaurante que o cliente opta por 
#salada,macarronada,sorvete ou sanduiche
def restaurant():

    menu = {
        'salada':10.0,
        'macarronada':23.0,
        'hamburguer':30.0,
        'sorvete':5.0,
    }
    nome = input('digite seu nome:')
    print('seja bem vindo ao moon restaurante',nome)
    
    lista_valores = []
    lista_pedidos =[]
    p = input('quer fazer o pedido s/n')

    while p == "s":
        pedido = input('os codigos são salada,macarronada,sanduiche,sorvete')
        lista_pedidos.append(pedido)
        lista_valores.append(menu[pedido])
        s = sum(lista_valores)
        print(lista_pedidos, 'total', s)
        p = input('quer fazer o pedido s/n')
    print('Ate logo')    
restaurant()       