import os
if __name__ == '__main__':
    while True:
        x=input('what do you want to hear? ')
        command= f'say {x}'
        if x=='q':
            os.system('say ''bye bye''')
            break
        os.system(command)


