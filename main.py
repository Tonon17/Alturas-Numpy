import numpy as np


alturas = np.array([1.80, 1.76, 2.01, 1.75, 1.62, 1.75, 1.70, 1.80])

media_altura = np.mean(alturas)
print(f"Média das alturas:{media_altura:.2f}")

max_altura = np.max(alturas)
min_altura = np.min(alturas)
print(f"Altura máxima: {max_altura}")
print(f"Altura mínima: {min_altura}")



                       