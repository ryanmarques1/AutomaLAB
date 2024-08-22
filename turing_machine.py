class Turing_Machine: 
    def __init__(self, estado, cabeca_escrita, lista_de_fitas):
        self.estado = estado
        self.cabeca_escrita = cabeca_escrita
        self.lista_de_fitas = lista_de_fitas
        
    def obter_estado(self):
        return self.estado
    
    def cabeca(self):
        return self.cabeca_escrita

    def lista(self):
        return self.lista_de_fitas
    
    # Tabela de Regras
    
    def maquina_de_atualizacao(self, lista_de_caracteres):
        # Estado ínicial
        if (self.estado == 'q1'):
            if(self.lista_de_fitas[self.cabeca_escrita] != 0):
                # Estado # (p)
                ler = self.lista_de_fitas[self.cabeca_escrita]
                indices_de_caracteres = lista_de_caracteres.index(ler)
                self.estado = ''.join(['p'], str(indices_de_caracteres))
                # Escrever # (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move # (direita)
                self.cabeca_escrita += 1
            else:
                # Estado # (qy)
                self.estado = 'qy'
                # Escrever # (zero)
                self.lista[self.cabeca_escrita] = 0
                # Move # (direita)
                self.cabeca_escrita += 1
                
        elif (self.estado.comeca_com('pn')):
            if(self.lista_de_fitas[self.cabeca_escrita] != 0):
                # Estado # (inalterado)
                self.estado = self.estado
                # Escreve # (inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move # (direita)
                self.cabeca_escrita += 1
            else:
                # Estado # (r)
                self.estado = ''.join(['r', self.estado[1:]])
                # Escrever # (zero, inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move # (esquerda)
                self.cabeca_escrita -= 1
        elif (self.estado.comeca_com('rn')):
            ler = lista_de_caracteres[int(self.estado[1:])]
            if (self.lista_de_fitas[self.cabeca_escrita] != ler and self.lista_de_fitas[self.cabeca_escrita] != 0):
                # Estado # (qn)
                self.estado = 'qn'
                # Escreve # 
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move # (esquerda)
                self.cabeca_escrita -= 1
            else:
                # Estado # (q2)
                self.estado = 'q2'
                # Escreve # (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Mover # (esquerda)
                self.cabeca_escrita -= 1
        elif (self.estado == 'q2'):
            if (self.lista_de_fitas[self.cabeca_escrita] != 0):
                # Estado # (inalterado)
                self.estado = 'q2'
                # Escreve # (inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move # (esquerda)
                self.cabeca_escrita -= 1
            else:
                # Estado # (q1)
                self.estado = 'q1'
                # Escreve # (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move # (direita)
                self.cabeca_escrita += 1
                