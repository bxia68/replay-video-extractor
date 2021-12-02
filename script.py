from os import listdir, startfile, getcwd
from os.path import isfile, join
from time import sleep
import psutil
from datetime import datetime


def main():
    path = r'Replays/Record'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for i in files:
        print(f'opening {i}            {datetime.now().strftime("%H:%M:%S")}')
        startfile(f'{getcwd()}\\replays\\{i}')
        sleep(30)
        while "WorldOfWarships64.exe" in (p.name() for p in psutil.process_iter()):
            sleep(3)
        print(f'replay ended            {datetime.now().strftime("%H:%M:%S")}')


if __name__ == '__main__':
    main()
