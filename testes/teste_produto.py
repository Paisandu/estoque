from     produtos.produto    import   Produto
p1=Produto()
p1.nome="macarrao parafuso"
p1.quantidade=5
#criação de objeto 2
p2=Produto()
p2.nome="molho de tomate"
p2.quantidade=3

print(p1.listar_produtos())
print(p2.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos())

p1.retirada(10) 
print(p1.listar_produtos())

if p1.retirada(100):
    print("Saida registrada")
else:
    print("Saida recusada")

print(p1.listar_produtos())