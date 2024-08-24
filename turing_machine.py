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
        # Estado inicial
        if self.estado == 'q1':
            if self.lista_de_fitas[self.cabeca_escrita] != 0:
                # Estado (p)
                ler = self.lista_de_fitas[self.cabeca_escrita]
                indices_de_caracteres = lista_de_caracteres.index(ler)
                self.estado = f'p{indices_de_caracteres}'  # Corrigido
                # Escrever (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move (direita)
                self.cabeca_escrita += 1
            else:
                # Estado (qy)
                self.estado = 'qy'
                # Escrever (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move (direita)
                self.cabeca_escrita += 1
                
        elif self.estado.startswith('pn'):
            if self.lista_de_fitas[self.cabeca_escrita] != 0:
                # Estado (inalterado)
                self.estado = self.estado
                # Escrever (inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move (direita)
                self.cabeca_escrita += 1
            else:
                # Estado (r)
                self.estado = 'r' + self.estado[2:]  # Corrigido
                # Escrever (zero, inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move (esquerda)
                self.cabeca_escrita -= 1
        elif self.estado.startswith('rn'):
            ler = lista_de_caracteres[int(self.estado[2:])]
            if self.lista_de_fitas[self.cabeca_escrita] != ler and self.lista_de_fitas[self.cabeca_escrita] != 0:
                # Estado (qn)
                self.estado = 'qn'
                # Escrever
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move (esquerda)
                self.cabeca_escrita -= 1
            else:
                # Estado (q2)
                self.estado = 'q2'
                # Escrever (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Mover (esquerda)
                self.cabeca_escrita -= 1
        elif self.estado == 'q2':
            if self.lista_de_fitas[self.cabeca_escrita] != 0:
                # Estado (inalterado)
                self.estado = 'q2'
                # Escrever (inalterado)
                self.lista_de_fitas[self.cabeca_escrita] = self.lista_de_fitas[self.cabeca_escrita]
                # Move (esquerda)
                self.cabeca_escrita -= 1
            else:
                # Estado (q1)
                self.estado = 'q1'
                # Escrever (zero)
                self.lista_de_fitas[self.cabeca_escrita] = 0
                # Move (direita)
                self.cabeca_escrita += 1
