def monitorar_consumo():

    n = int(input('Digite a quantidade de dias: '))


    dias_acima_meta = 0
    dias_abaixo_meta = 0
    soma_consumo = 0
    maior_consumo = -1  # Valor menor que qualquer consumo
    menor_consumo = 10000000  # Um valor alto suficiente para inicializar o menor consumo
    meta_consumo = 150


    for e in range(1, n + 1):
        consumo = int(input(f'Insira seu consumo de energia no dia {e}: '))


        soma_consumo += consumo


        if consumo >= meta_consumo:
            dias_acima_meta += 1
        else:
            dias_abaixo_meta += 1


        if consumo > maior_consumo:
            maior_consumo = consumo
        if consumo < menor_consumo:
            menor_consumo = consumo


    media_consumo = soma_consumo / n


    if dias_acima_meta == n:
        print('Parabéns! Todos os dias cumpriram a meta de consumo sustentável.')
    elif dias_acima_meta == 0:
        print('Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.')
    else:
        print(f'{dias_acima_meta} dias cumpriram a meta e {dias_abaixo_meta} dias não cumpriram a meta.')

    print(
        f'A média de consumo foi de {media_consumo:.2f} kWh. O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} kWh.')



monitorar_consumo()
