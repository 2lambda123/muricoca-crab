# Authors: Marcel Caraciolo <marcel@muricoca.com>
#          Bruno Melo <bruno@muricoca.com>
# License: BSD Style.

import csv
import shutil
from os import environ
from os.path import dirname
from os.path import join
from os.path import exists
from os.path import expanduser
from os.path import isdir
from os import listdir
from os import makedirs
import numpy as np


def load_movielens100k():
    module_path = dirname(__file__)
    data_file = csv.reader(open(join(module_path, 'data', 'movielens100k.csv')))
    temp = data_file.next()
    n_samples = int(temp[0])
    n_features = int(temp[1])
    data = np.empty((n_samples, n_features))
    for i, ir in enumerate(data_file):
        data[i] = np.asanyarray(ir, dtype=np.int)
    return data
