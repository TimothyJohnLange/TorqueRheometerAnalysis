import json
import os
import glob
import pandas

# read configuration file and expand ~ to user directory
with open('config.json') as f:
    config = json.load(f)
datadir = os.path.expanduser(config['datadir'])

def alldatafiles():
    return glob.glob(os.path.join(datadir, '**/*.txt'))


class DataFile:
    """ Class for holding data """
    def __init__(self, filename):
        # Split into directory and filename parts
        self.directory, self.filename = os.path.split(filename)
        # Load with pandas
        self.data = pandas.read_table(filename,
                                      skiprows = 4,
                                      sep = ';',
                                      usecols = range(6))

    def simple_data(self):
        time = self.data['t [min]'].values
        temp = self.data[self.data.columns[4]].values
        torque = self.data['M [Nm]'].values

        return time, temp, torque
