
# Renderiza os objetos do jogo
# No terminal

def Renderizar(mapa, objetosCores=False):#{

    import colorama
    colorama.init(autoreset=True)

    pixel = '██'

    cores = {
        'verde': f'{colorama.Fore.GREEN}{pixel}',
        'azul': f'{colorama.Fore.BLUE}{pixel}',
        'cinza': f'{colorama.Fore.LIGHTBLACK_EX}{pixel}',
        'vermelho': f'{colorama.Fore.RED}{pixel}',
        'vazio': '  '
    }

    cloneMapa = []

    for linha in range(0, len(mapa)):#{

        cloneMapa.append([])

        for objeto in range(0, len(mapa[linha])):#{

            cloneMapa[linha].append('')

            if objetosCores != False:#{

                cloneMapa[linha][objeto] = cores[objetosCores[mapa[linha][objeto]]['cor']]

            #}

            else:#{

              cloneMapa[linha][objeto] = cores[mapa[linha][objeto]]

            #}

        #}

    #}

    for linha in cloneMapa:#{

      print(*linha, sep='')

    #}

#}