__author__ = 'admin'

#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt
#import numpy as np
from rpy2.robjects import r

r("library('maps')")
r("library('mapdata')")
class Mapplot(object):

    def __int__(self):
        pass

    def plot(self,city,value):
        pass


r("map('state', fill = TRUE, col = rainbow(209),mar = c(0, 0, 2, 0))")