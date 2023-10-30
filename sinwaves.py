
from scipy import fft
import numpy as np
from main import *

MAX_SAMPLES = 3000

class sinwaves():
   def __init__(self,amplitude=1,frequency=1):
      
      self.amplitude = amplitude
      self.frequency = frequency
      self.Xaxis=np.linspace(0,2*np.pi,MAX_SAMPLES)
      self.Yaxis=(self.amplitude)/(np.sin(self.Xaxis*self.frequency*2*np.pi))

      def add(self,sinwaves1):
         return sinwaves1.Yaxis + self.Yaxis
      def Getfrequncy(self):
         return self.frequency