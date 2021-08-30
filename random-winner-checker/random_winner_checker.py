from datetime import *
import os
from random import randint


def choose_random(to_save_txt, *args):
    guess: int = randint(0, len(args) - 1)
    file_suffix: int = 0
    message: str = f'{args[guess]} is the winner !'

    print(f'{message}')

    if to_save_txt:

        if not os.path.exists('./random-winners-lists'):
            os.mkdir('./random-winners-lists')
        else:
            pass

        for index in os.listdir('./random-winners-lists'):
            if index.endswith('.txt'):
                if index.startswith('result_random_winner_'):
                    index = index.replace('result_random_winner_', '')
                    index = index.replace('.txt', '')
                    # print(index)
                    file_suffix = int(index)
                    # print(file_suffix)
                else:
                    pass

        f = open(f'./random-winners-lists/result_random_winner_{file_suffix + 1}.txt', 'w')
        message += f"\n\nCreated At - {datetime.today().strftime('%H')} : {datetime.today().strftime('%M')} : {datetime.today().strftime('%S')}"
        f.write(f'{message}')
        if not f.closed:
            f.close()


participants: list = [
    'Doraemon', 'Nobita', 'Shizuka', 'Gian', 'Suneo', 'Shinchan', 'Dora', 'Oggy', 'Jack', 'Bob'
]

choose_random(True, *participants)
