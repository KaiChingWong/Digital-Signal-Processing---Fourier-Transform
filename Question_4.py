# -*- coding: utf-8 -*-
"""
Digital Signal Processing 4

Assignment 1: Fourier Transform

By Kai Ching Wong (GUID:2143747W)
"""

"Task 4"

import numpy as np

import matplotlib.pyplot as plt
data = np.loadtxt('ending_7.dat') #Read data file from computer

Time7 = data[:,0] #Read 1st column from ending_7.dat
Ending7 = data[:,1] #Read 2nd column from ending_7.dat

Ending7 = (Ending7-min(Ending7))/(max(Ending7)-min(Ending7)) #Normailising
Ending7 = Ending7-np.mean(Ending7) #Remove offset

import scipy.io.wavfile as wavfile
wavfile.write('ending_7.wav',1000,Ending7) #Converting ending_7.dat to WAV file

plt.figure(0)
plt.plot(Time7,Ending7,linewidth=0.5)
plt.title('Phone Number of My Last Digit Matric Number')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.savefig('Phone Number of My Last Digit GUID Number.svg')

"Extracted starting time and ending time from Audacity then multiplied them by sampling rate to get the frequency"
num1 = Ending7[2261:2372]
num2 = Ending7[2670:2789]
num3 = Ending7[3099:3228]
num4 = Ending7[4532:4642]
num5 = Ending7[5106:5218]
num6 = Ending7[5615:5763]
num7 = Ending7[7348:7499]
num8 = Ending7[8091:8216]
num9 = Ending7[8703:8813]
num10 = Ending7[10135:10227]
num11 = Ending7[10580:10672]

"Fourier Tranformed each number"
xf1 = np.fft.fft(num1)
xf2 = np.fft.fft(num2)
xf3 = np.fft.fft(num3)
xf4 = np.fft.fft(num4)
xf5 = np.fft.fft(num5)
xf6 = np.fft.fft(num6)
xf7 = np.fft.fft(num7)
xf8 = np.fft.fft(num8)
xf9 = np.fft.fft(num9)
xf10 = np.fft.fft(num10)
xf11 = np.fft.fft(num11)

"Frequency x axis for each number"
f1 = np.linspace(0,1000,len(num1))
f2 = np.linspace(0,1000,len(num2))
f3 = np.linspace(0,1000,len(num3))
f4 = np.linspace(0,1000,len(num4))
f5 = np.linspace(0,1000,len(num5))
f6 = np.linspace(0,1000,len(num6))
f7 = np.linspace(0,1000,len(num7))
f8 = np.linspace(0,1000,len(num8))
f9 = np.linspace(0,1000,len(num9))
f10 = np.linspace(0,1000,len(num10))
f11 = np.linspace(0,1000,len(num11))

"Declaring array for plotting"
x=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]
y=[xf1,xf2,xf3,xf4,xf5,xf6,xf7,xf8,xf9,xf10,xf11]

"Using loop to plot each number"
for i in range(len(x)):
    plt.figure(i+1) # i+1 means plotting after plt.figure(0)
    plt.plot(x[i],abs(y[i]))
    plt.title('Number %i' %(i+1)) # %-operator for number variation
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Amplitude')
    plt.axis([0,500,0,max(abs(y[i]))]) #Enlarging each plot from 0 to 500Hz
    plt.savefig('Plot of Number %i.svg' %(i+1),format='svg') #Save plot as svg format
    
"""
###############################################################################
The following was Programmed by Samuel Chua
###############################################################################
def printing(num,x,y):
    plt.figure(num)
    plt.plot(x,abs(y))
    plt.title('Number %i' % (num))
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Amplitude')
    plt.axis([0,500,0,max(abs(y))])

for i in range(11):
   printing(i+1,x[i],y[i])
###############################################################################
"""