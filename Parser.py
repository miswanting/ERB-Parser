import configparser
import csv
import os


def handleConfig():
    # csv/_default.config
    # emuera.config
    with open('emuera.config', 'r', encoding='shift-jis') as f:
        s = f.read()
    config = configparser.ConfigParser()
    config.read_string('[default]\n'+s)
    # print(dir(config))
    # print(config.sections())

    # for key in config['default']:
    #     print(key)

    # csv/_fixed.config


def handleCSV():
    def loadCSV(path):
        with open(path) as f:
            r = csv.reader(f)
            for row in r:
                # for each in row:
                #     print(each.replace(' ', ''))
                print(list(map(lambda x: x.replace(' ', ''), row)))

    def loadOnce(path):
        # *.csv 广度优先
        with os.scandir(path) as it:
            folders = []
            for entry in it:
                if entry.is_dir():
                    folders.append(entry)
                if entry.is_file() and entry.name.upper().endswith('.CSV'):
                    loadCSV(entry)
            for entry in folders:
                loadOnce(entry)
    loadOnce('csv/_Replace.csv')
    loadOnce('csv/_Rename.csv')
    loadOnce('csv')


def handleERH():
    def loadERH(path):
        print(path.name)

    def loadOnce(path):
        # *.erh 广度优先
        with os.scandir(path) as it:
            folders = []
            for entry in it:
                if entry.is_dir():
                    folders.append(entry)
                if entry.is_file() and entry.name.upper().endswith('.ERH'):
                    loadERH(entry)
            for entry in folders:
                loadOnce(entry)


def handleERB():
    def loadERH(path):
        print(path.name)

    def loadOnce(path):
        # *.erb 深度优先
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_dir():
                    loadOnce(entry)
                if entry.is_file() and entry.name.upper().endswith('.ERH'):
                    loadERH(entry)


if __name__ == "__main__":
    handleConfig()
    handleCSV()
    handleERH()
    handleERB()
