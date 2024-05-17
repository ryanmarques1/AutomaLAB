class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inic, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inic = estado_inic
        self.estados_finais = estados_finais


def minimiza_afd(afd):
    import os
    import base
    print("Minimiza AFD", end="\n")
    
    # Inicializar as partições
    
    particao = [{'0'}, set(afd.estados - {'0'})] #supondo que 0 seja o estado inicial
    
    # Refinar as partições até que ocorra alguma mudança nos estados
    
    while True:
        nova_particao = []
        for grupo in particao:
            novo_grupo = []
            for simbolo in afd.alfabeto:
                proximos_estados = set()
                for estado in grupo:
                    proximos_estados.add(afd.transioes.get((estado, simbolo), None))
                proximos_estados.discard(None)

         