import base
import os

def converte_afn_afd():
    pasta_afn = "AFNs/"
    pasta_afd = "AFDs/"
    delta_afn = base.converte_txt_dict(pasta_afn)

    estados_finais, alfabeto, estado_inicial = base.push_ini_fini_alfabeto(pasta_afn, estado_inicial, estados_finais, alfabeto)

<<<<<<< Updated upstream
    print(estados)
=======
    

>>>>>>> Stashed changes
