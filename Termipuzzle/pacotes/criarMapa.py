
# Criação de mapas

class Mapa:#{

    # Cria o mapa
    def criar(self, objetos, modo='auto'):#{

        self.objetos = objetos

        # Construção com níveis
        if modo == 'historia':#{

            pass

        #}

        # Construção de um nível randomico
        elif modo == 'auto':#{

            mapa = self.geracaoAutomatica()

            return mapa

        #}

        # Construção de um nível feito no script
        elif modo == 'manual':#{

            mapa = self.geracaoManual()

            return mapa

        #}

    #}

    def geracaoHistoria(self):#{

        pass

    #}

    def geracaoAutomatica(self):#{

        from random import randrange

        mapa = []
        altura = 10
        largura = 10

        for linha in range(0, altura):#{

            mapa.append([])

            for objeto in range(0, largura):#{

                mapa[linha].append(randrange(self.objetos))

            #}

        #}

        return mapa

    #}

    def geracaoManual(self):#{

        mapa = []

        return mapa

    #}

#}