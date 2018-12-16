"""
Digital Signal Processing 4

Assignment 1: Fourier Transform

By Kai Ching Wong (GUID:2143747W)
"""

###############################################################################
"Task 2"

import numpy as np

import scipy.io.wavfile as wavfile
fs,data = wavfile.read('Rickys_Voice.wav') #Read WAV file from computer

import matplotlib.pyplot as plt

time = len(data)/fs #Finding the length of time for the audio sample
t = np.linspace(0,time,len(data))

plt.figure(1,figsize=(10,5))
plt.plot(t,data,linewidth=0.05)
plt.title('Voice Recording before Noise Filtering in Time Domain')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.savefig('My_Recording_in_Time_Domain.svg')

xf = np.fft.fft(data) #Fourier Transform the audio sample to frequency in Hz
f = np.linspace(0,fs,len(data))
###############################################################################

###############################################################################
"Task 3"

k1 = int(len(xf)/fs*0) #Indices correspond to 0Hz to 30Hz
k2 = int(len(xf)/fs*30)
k3 = int(len(xf)/fs*4000)  #Indices correspond to 4000 to 22000Hz
k4 = int(len(xf)/fs*22000)
xf[k1:k2+1]=0 #Remove noises 
xf[k3:k4+1]=0 #Remove noises

r1 = int(len(xf)/fs*(fs-30)) #Mirror of k2
r2 = int(len(xf)/fs*(fs-0)) #Mirror of k1
r3 = int(len(xf)/fs*(fs-22000)) #Mirror of k4
r4 = int(len(xf)/fs*(fs-4000)) #Mirror of k3
xf[r1:r2+1]=0 #Remove mirror
xf[r3:r4+1]=0 #Remove mirror
###############################################################################

###############################################################################
"Task 3 Part 2"

A1 = int(len(xf)/fs*4250) #Indices correspond to 4250 to 4500Hz
A2 = int(len(xf)/fs*4500)
xf[A1:A2+1]=xf[A1:A2+1]*2 #Amplified range

rA1 = int(len(xf)/fs*(fs-4500)) #Mirror of A2
rA2 = int(len(xf)/fs*(fs-4250)) #Mirror of A1
xf[rA1:rA2+1]=xf[rA1:rA2+1]*2 #Amplified mirror range
###############################################################################

###############################################################################
"Plotting code for Task 2 and 3"

ixf = np.fft.ifft(xf) #Transform back to time domain
ixf = (ixf-min(ixf))/(max(ixf)-min(ixf)) #Normalising
ixf = np.real(ixf-np.mean(ixf)) #Remove offset from the audio sample

plt.figure(2,figsize=(10,5))
plt.plot(t,ixf,linewidth=0.05) #Plot for time domain

plt.title('Voice Recording before Noise Filtering in Time Domain') #Used for Task 2
plt.title('Voice Recording after Noise Filtering in Time Domain') #Used for Task 3
plt.title('Voice Recording after Noise Filtering and Amplification in Time Domain') #Used for Task 3 part 2

plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

plt.savefig('My_Recording_in_Time_Domain.svg') #Used for Task 2
plt.savefig('My_Recording_in_Time_Domain_after_Filtering.svg') #Used for Task 3
plt.savefig('My_Recording_in_Time_Domain_after_Filtering_and_Amplification.svg') #Used for Task 3 part 2

plt.figure(3,figsize=(10,5))
plt.plot(f,abs(xf),linewidth=0.05) #Plot for frequency domain

plt.title('Voice Recording before Noise Filtering in Frequency Domain') #Used for Task 2
plt.title('Voice Recording after Noise Filtering in Frequency Domain') #Used for Task 3
plt.title('Voice Recording after Noise Filtering and Amplification in Frequency Domain') #Used for Task 3 part 2

plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

plt.savefig('My_Recording_in_Frequency_Domain.svg') #Used for Task 2
plt.savefig('My_Recording_in_Frequency_Domain_after_Filtering.svg') #Used for Task 3
plt.savefig('My_Recording_in_Frequency_Domain_after_Filtering_and_Amplification.svg') #Used for Task 3 part 2

wavfile.write('Filtered_Voice.wav',fs,ixf) #Used for Task 3
wavfile.write('Filtered_and_Amplified_Voice.wav',fs,ixf) #Used for Task 3 part 2
###############################################################################

###############################################################################
"Task 5"

data = data/1000 #data/1000 due to overflow
data = (data-min(data))/(max(data)-min(data)) #Normalising
data = np.real(data-np.mean(data))

AE = np.fft.fft(data) #Using the same data from Rickys Voice for the Aural Exciter
AEC = np.zeros(len(AE),dtype = complex)
c1 = int(len(AE)/fs*5000) #Starting point for adding non-linearlity
c2 = int(len(AE)/fs*(fs-5000)) #Ending point for adding non-linearlity
AEC[c1:c2+1] = AE[c1:c2+1] #Using Highpass filter

iAE = np.fft.ifft(AE)

iAE = np.arctan(iAE*0.5)/5 #atan non-linearlity
Output = iAE+data #Aural Exciter 
Output = np.real(Output)

plt.figure(4)
plt.plot(t,Output,linewidth=0.05)
plt.title('Voice Recording with Non-linearlity Added')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.savefig('Aural Exciter.svg')

wavfile.write('Added_Non-linearity_Voice.wav',fs,Output)
###############################################################################

###############################################################################
"For zooming in the plot"

#plt.axis([0,10000,0,max(abs(xf))])

###############################################################################