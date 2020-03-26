import glob
import os
from sys import argv, exit
import argparse
from logger import logger
from __init__ import __version__

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', '-f', nargs='?',
                        help='Folder containing the json files')
    parser.add_argument('--version', '-v', '-V', action='store_true',
                        help='View version of program')
    args = parser.parse_args()
    config_from_args = args.__dict__
    fil = config_from_args.pop('folder')
    ver = config_from_args.pop('version')
    if ver is not None and ver is True:
        logger.info('Version: '+__version__)
    elif fil is not None and os.path.isdir(fil):
        folder = fil
        f = []
        f = glob.glob(folder+"/*.json")
        if f.__len__() == 0:
            logger.error(fil + ' doesn`t contain any json files')
        else:
            json_to_dataset(f)
    elif fil is not None and os.path.isdir(fil) is False:
        logger.fatal(fil + ' is not a folder')
    else:
        print(os.system('python2.7 ~/Development/json_to_dataset.py -h'))

def json_to_dataset(folder):
    for file in folder:
        print('Processing ' + file + '\n\r')
        print(os.system('labelme_json_to_dataset ' + file))
main()
