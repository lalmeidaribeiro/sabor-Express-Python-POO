#4- Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e 
# armazene em uma variável chamada categoria.

class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.categoria = 'categoria'

print(restaurante_praca.categoria)