import pandas as pd
from matplotlib import pylab, mlab, pyplot
import seaborn as sns
plt = pyplot
plt.style.use('ggplot')

class SourceController():
    def readCSV(self, file):
        return pd.read_csv(file, sep=';', encoding='utf-8')
