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
    
    particao = [{afd.estado_inic}, set(afd.estados - {afd.estado_inic})]
    
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
                for sub_grupo in particao:
                    if proximos_estados <= sub_grupo:
                        novo_grupo.append(sub_grupo)
                        break
            if len(novo_grupo) > 0:
                nova_particao.extend(novo_grupo)
            else:
                nova_particao.append(grupo)
        if nova_particao == particao:
            break
        particao = nova_particao

         