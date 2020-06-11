
# Entrada do teclado
# Retorna um comando

class clickTeclado:#{

    # Construtor
    def __init__(self):#{

        from msvcrt import kbhit

        # Lista de comandos do jogo
        self.listaDeComandos = {
            'w': 'andarCima',
            'a': 'andarEsquerda',
            's': 'andarBaixo',
            'd': 'andarDireira'
        }

        # Verifica se alguma tecla foi pressionada
        self.clickEsperando = kbhit()

    #}

    # Somente espera clicar
    def clickSemRetorno(self):#{

        from msvcrt import getwch

        getwch()

    #}

    # Retorna o comando referente ao botão clicado
    def clickComRetorno(self, processe=True):#{

        from msvcrt import getwch

        # Se alguma tecla for pressionada
        if self.clickEsperando:#{

            self.click = getwch()

            # Se quiser que retorne a string com o comando
            if processe:#{

                return self.listaDeComandos[self.click]

            #}

            else:#{

                return self.click

            #}

        #}

        else:#{

            return None

        #}

    #}

#}