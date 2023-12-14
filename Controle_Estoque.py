Bebidas = int(input('Quantas Bebidas Temos No estoque agora?'))
Alimentos = int(input('Quantos Alimentos Temos No estoque agora?'))
Limpeza = int(input('Quantos Produtos de limpeza Temos No estoque agora?'))

if Bebidas >= 75 and (Alimentos >= 50) and (Limpeza >= 30):
    print('Estoque Completo!, Quantidade: Bebidas {}, Alimentos {}, Limpeza {}'.format(Bebidas, Alimentos, Limpeza))

else:
    print('Alguns Itens precisam ser Reabastecidos!')
    print('COMO DEVE ESTAR: Bebidas: 75, Alimentos: 50, Limpeza: 30')
    print('COMO ESTA AGORA: Bebidas: {}, Alimentos: {}, Limpeza: {}' .format(Bebidas, Alimentos, Limpeza))