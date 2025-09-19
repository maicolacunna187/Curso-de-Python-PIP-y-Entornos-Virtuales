import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel, o tijera: ').lower()
    
    while user_option not in options:
        print('Esa opción no es valida.')
        user_option = input('piedra, papel, o tijera: ').lower()    

    computer_option = random.choice(options)

    print(f'User option: {user_option}')
    print(f'Computer option: {computer_option}')
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate. No cuenta la ronda.')
        return user_wins, computer_wins, False  # False = no contar ronda
    elif user_option == 'piedra':
        if computer_option == 'papel':
            print('Papel gana a piedra.')
            print('Computer gano.')
            computer_wins += 1
        else:
            print('Piedra gana a tijera.')
            print('User gano.')
            user_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra.')
            print('User gano.')
            user_wins += 1
        else:
            print('Tijera gana a papel.')
            print('Computer gano.')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'piedra':
            print('Piedra gana a tijera.')
            print('Computer gano.')
            computer_wins += 1
        else:
            print('Tijera gana a papel.')
            print('User gano.')
            user_wins += 1
    return user_wins, computer_wins, True  # True = sí contar ronda

def verify_winner(user_wins, computer_wins):
    print('RESULTADO FINAL: ')

    if user_wins == computer_wins:
        print('User and Computer: EMPATE.')

    elif user_wins > computer_wins:
        print('User: GANADOR.')
    else:
        print('Computer: GANADOR.')
        


def run_game():
    user_wins = 0
    computer_wins = 0
    round = 0
    
    while round < 3:
        print('*' * 10)
        print('ROUND', round)
        print('*' * 10)

        user_option, computer_option = choose_options()
        user_wins, computer_wins, round_count = check_rules(user_option, computer_option, user_wins,computer_wins)

        if round_count:  # solo avanza si no hubo empate
            round += 1

    verify_winner(user_wins, computer_wins)

    print(f'User wins: {user_wins}')
    print(f'Computer wins: {computer_wins}')
    print(f'Round: {round}')
        

if __name__ == "__main__":
    run_game()
