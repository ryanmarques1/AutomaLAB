simbolo_vazio = " "
fita = {}
def inicia_fita(fita_entrada):
	fita_ini = {}
	for i in range(len(fita_entrada)): 
		fita_ini[i] = fita_entrada[i] #recebendo a fita de entrada e colocando na fita e enumerando.return fita_ini
	return fita_ini

def tamanho_fita(fita_entrada):
	aux = ""
	#pegar o tam inicial e final da fita.
	inicio = len(fita_entrada[0])
	for i in range(len(fita_entrada) + 1):
		fim = i
	aux = inicio, fim
	print(aux)
	return aux

class MaquinaTuring(object):
	def __init__(self, fita="", simbolo_vazio=" ", estado_inicial = "", estados_finais = None,
	regras_transicao = None): #construtor
		
		self.fita = inicia_fita(fita) 
		self.posicao_cabeca = 0
		self.estados_correntes = estado_inicial
		self.simbolo_vazio = simbolo_vazio
		if estados_finais is None:
			self.estados_finais = set() #Lista para os estados finais, usando função propria do python
		else:
			self.estados_finais = set(estados_finais)
		if regras_transicao is None:
			self.regras_transicao = {}
		else:
			self.regras_transicao = regras_transicao
	
	def retorna_fita(self): #retorna a fita.
		return str(self.fita)
	
	def eh_final(self):
		if self.estados_correntes in self.estados_finais:
			return True
		else:
			return False

	def maquina_atualizando(self): #Aplicações das regras.
		print("attt\n")
		simbolo_atual_cabeça = self.fita.get(self.posicao_cabeca, self.simbolo_vazio) #get para se caso não existir a posição ler o simbolo vazio
		chave = (self.estados_correntes, simbolo_atual_cabeça)
		if chave in self.regras_transicao:
			valor = self.regras_transicao[chave]
			self.fita[self.posicao_cabeca] = valor[1] #recebe novo simbolo
			if valor[2] == "R":
				self.posicao_cabeca += 1
			elif valor[2] == "L":
				self.posicao_cabeca -= 1
		self.estados_correntes = valor[0] #Se não for nem L nem R, mantém.

		#Livre de contexto.