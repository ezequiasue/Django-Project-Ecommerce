def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def cart_total_qtd(carrinho):
    # List Comprehension
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_totals(carrinho):
    # List Comprehension usada para tratar o preco total e promocional
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()

        ]

    )
