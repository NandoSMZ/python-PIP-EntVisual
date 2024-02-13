import random

count = 1
resultado_user = 0
resultado_computer = 0
rounds = int(input("Cuantas Rondas quieres Jugar =>"))


def choice_optiones():
    opciones = ("piedra", "papel", "tijera")  # Tupla apra que nunca sea modificado
    user_option = input("Piedra, Papel o Tijera ==>")
    user_option = user_option.lower()  # Poner respuesta de usuario en Minuscula siempre
    computer_option = random.choice(opciones)

    if not user_option in opciones:
        return None, None

    print("User option ==>", user_option)
    print("Computer option ==>", computer_option)

    return user_option, computer_option


def final_result(r_computer, r_user):
    if r_computer == r_user:
        print('*' * 20)
        print('EMPATADOS')
        print('*' * 20)
    elif r_user > r_computer:
        print('*' * 20)
        print(f'De {rounds} rondas ganaste {resultado_user} rondas, Felicidades User')
        print('*' * 20)
    else:
        print('*' * 20)
        print(f'De {rounds} rondas ganaste {r_computer} rondas, Felicidades PCMONSTER')
        print('*' * 20)


while count <= rounds:
    print('*' * 10)
    print('ROUND', count)
    print('*' * 10)

    u_option, c_option = choice_optiones()
    if u_option is None and c_option is None:
        print(print('Opcion no Valida, ingrese nuevamente'))
    else:
        if u_option == c_option:
            print("empate")
        elif u_option == "piedra":
            if c_option == "tijera":
                print("Piedra gana a Tijera")
                print("User gano")
                resultado_user += 1
            else:
                print("Papel gana a Piedra")
                print("Computer gano")
                resultado_computer += 1
        elif u_option == "tijera":
            if c_option == "papel":
                print("Tijera gana a Papel")
                print("User gano")
                resultado_user += 1
            else:
                print("Piedra gana Tijera")
                print("Computer gano")
                resultado_computer += 1
        elif u_option == "papel":
            if c_option == "tijera":
                print("Tijera gana a Papel")
                print("Pc gano")
                resultado_computer += 1
            else:
                print("Papel gana a Piedra")
                print("User gano")
                resultado_user += 1
    count += 1

final_result(resultado_computer, resultado_user)
