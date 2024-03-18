from operation import Operation

import math

class Variations(Operation): # O(n)
        def __init__(self): # O(n)
            self.n = int(input("Ingrese la cantidad de elementos (n): ")) # O(0)
            self.r = int(input("Ingrese la cantidad de grupos (r): ")) # O(0)
            while True: # O(n)
                try: # O(n)
                    if self.n <= 0 or self.r <= 0 or not isinstance(self.n, int) or not isinstance(self.r, int): # O(n)
                        raise ValueError("n y r deben ser enteros positivos mayores y diferentes a cero.") # O(n)
                    break  # O(n)
                except ValueError: # O(n)
                    print("Error por favor intente de nuevo con números enteros mayores a cero.") # O(n)
                    # Solicitar nuevamente los valores de n y r
                    self.n = int(input("Ingrese la cantidad de elementos (n): ")) # O(n)
                    self.r = int(input("Ingrese la cantidad de grupos (r): ")) # O(n)
        # Entonces la complejidad de esta parte es: 2 O(0) + 9 O(n) = O(n)
        
        def ordinary_operation(self): # O(n)
            while True: # O(n)
                try: # O(n) 
                    if self.n == 0 or self.r == 0: # O(n)
                        raise ValueError("n y r deben ser números enteros mayores a cero.") # O(n)
                    result = self.n ** self.r # O(n)
                    return result # O(n)
                except ValueError as e: # O(n)
                    print("Error:", e) # O(n)
                    # Solicitar nuevamente los valores de n y r 
                    n = int(input("Ingrese la cantidad de elementos (n): ")) # O(n)
                    r = int(input("Ingrese la cantidad de grupos (r): ")) # O(n)
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n # O(n) 
                    self.r = r # O(n)
                except TypeError: # O(n) 
                    print("Error: n y r deben ser números enteros.") # O(n)
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): ")) # O(n)
                    r = int(input("Ingrese la cantidad de grupos (r): ")) # O(n)
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n # O(n)
                    self.r = r # O(n)
        # Entonces la complejidad de esta parte es: 18 O(n) = O(n)

        def variation_operation(self): # O(n)
            while True: # O(n)
                try: # O(n)
                    result = math.factorial(self.n) // math.factorial(self.n - self.r) # O(n)
                    return result # O(n)
                except ValueError: # O(n)
                    print("Error por favor intente de nuevo con números enteros mayores a cero.") # O(n)
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): ")) # O(n)
                    r = int(input("Ingrese la cantidad de grupos (r): ")) # O(n)
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n # O(n)
                    self.r = r # O(n)
                except TypeError: # O(n)
                    print("Error: n y r deben ser números enteros.") # O(n) 
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): ")) # O(n)
                    r = int(input("Ingrese la cantidad de grupos (r): ")) # O(n)
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n # O(n) 
                    self.r = r # O(n)
        # Entonces la complejidad de esta parte es: 16 O(n) = O(n)
        
# Entonces la complejidad total del algoritmo es: 3 O(n) = O(n)