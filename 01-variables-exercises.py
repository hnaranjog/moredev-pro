# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
name: str = "Hector Naranjo Gallego"

# â€¢	age: un nÃºmero entero que represente tu edad.
age: int = 45

# â€¢	height: un nÃºmero flotante que represente tu altura.

height: float = 1.84

# â€¢	Imprime cada variable en una lÃ­nea separada.

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.

age_str = str(age)

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.

is_student: bool = True

# 4. Usa la función len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
print(len(name))

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Hector", "Naranjo", "Pereira"

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color = input("What is your favorite color? ")
print(color)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "apple"
print(fruit)
fruit = "banana"
print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price: float = 10.5
price: int = price
print(price)
print(type(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len = len("Calle 123")
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone: int = 1234567890
phone = 9876543210
print(type(phone))