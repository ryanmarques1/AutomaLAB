import string
import random
alfabeto = ['0','1']
aux = alfabeto
print(aux)
def random_generator(size=6, chars=aux):
 return ''.join(random.choice(chars) for _ in range(size))

print(random_generator()) # M4ICUV
print(random_generator()) # 76QUM7