from modelos.restaurante import Restautante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restautante('Praça', 'Gourmet')
#restaurante_praca.receber_avaliacao('Lari', 10)
#restaurante_praca.receber_avaliacao('Bru',8)
#restaurante_praca.receber_avaliacao('JJ',2)
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
#restaurante_pizza.receber_avaliacao('Lele', 5)
#restaurante_pizza.receber_avaliacao('Tata',8)
#restaurante_pizza.receber_avaliacao('Ju',3)

restaurante_manoel = Restautante('Seu Manoel', 'Francesa')
#restaurante_manoel.receber_avaliacao('Lele', 7)
#restaurante_manoel.receber_avaliacao('Tata',10)
#restaurante_manoel.receber_avaliacao('Ju',10)

#restaurante_praca.alternar_estador()
#restaurante_manoel.alternar_estador()


def main():
    #Restautante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()