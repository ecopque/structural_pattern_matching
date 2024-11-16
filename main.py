# FILE: /structural_pattern_matching/main.py

def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')
    print('...rest of the code')
execute_command('ls')

def execute_command(command: str):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _: #1:
            print('$ command not implemented')
execute_command('cd')


#1: Não é obrigatório usar 'case _:'. Este equivale ao 'else'.

# https://linktr.ee/edsoncopque