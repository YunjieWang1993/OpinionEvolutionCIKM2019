import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import math

#x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#x = np.arange(0,15,1)
y = [1-0.3025518688498352,1-0.41635407890335485,1-0.8753566494779202,1-0.39843955654566965,1-0.7628673499850989,1-0.9,1-0.13846972147065117,1-0.1,1-0.7597959310406731,1-0.5051650309318338,1-0.2960883986386996,1-0.7064869633198523,1-0.37286075068331115,1-0.35842162717201986,1-0.7401057273055922]
# y = [0.9,
#      0.3975484399156892,
#      0.22764723719031843,
#      0.1585577459172346,
#      0.2685386047915196,
#      0.23608081249423196,
#      0.2146665183074533,
#      0.24957080906655604,
#      0.18138884410186717,
#      0.1454260081211547,
#      0.25157643477466607,
#      0.21082221364897946,
#      0.28112432436651746,
#      0.3411871786829521,
#      0.2809449774067414,
#      0.14267967401602433,
#      0.09999999999999998,
#      0.1402352557597667,
#      0.11631858696482944,
#      0.14949923493116613,
#      0.3156053890771311,
#      0.1489818647260741,
#      0.2086265501045197,
#      0.2028029369586497]
# y = [0.0,
#      0.09999999999999998,
#      0.09999999999999998,
#      0.31692711979329014,
#      0.46507825262462776,
#      0.25111977480850856,
#      0.7775841757841628,
#      0.518820195446879,
#      0.4343145011697369,
#      0.9,
#      0.4097356583140135,
#      0.3537289295451309,
#      0.8515978098866971,
#      0.3935432680798704,
#      0.6039499796812081,
#      0.7775841757841628,
#      0.4278123894287589,
#      0.5140193901658933,
#      0.6210959789462712]
y_decay = []
yy_event_Fourier = []
for i in x:
    y_decay.append(2*math.pow(math.e,float(-2*i)))
yy = fft(y)
#print(yy)
xx = np.arange(len(y))
yy_IFFT = ifft(yy)
yy_decay = fft(y_decay)
#print(yy_decay)
xx_decay = np.arange(len(y_decay))
yy_decay_IFFT = ifft(yy_decay)
for i in x:
    yy_event_Fourier.append(yy[i]/yy_decay[i])
#print(yy_event_Fourier)
xx_event_Fourier = xx_decay
y_event = ifft(yy_event_Fourier)
print(y_event)
#print(y_event[1])
y_output = {}
for i in x:
    y_output[i] = y_event[i]
y_output = sorted(y_output.items(),key = lambda x:x[1],reverse = True)
print(y_output)
#xnew = np.linspace(0,14,300)
#smooth = spline(x,y,xnew)
plt.subplot(421)
plt.plot(x,y)
plt.title('sentiment shift')
plt.subplot(422)
plt.plot(xx,yy,'r')
plt.title('FFT_sentiment shift')
plt.subplot(423)
plt.plot(x,yy_IFFT)
plt.title('IFFT_sentiment shift')
plt.subplot(424)
plt.plot(x,y_decay)
plt.title('Decay Function')
plt.subplot(425)
plt.plot(xx_decay,yy_decay)
plt.title('FFT_Decay Function')
plt.subplot(426)
plt.plot(x,yy_decay_IFFT)
plt.title('IFFT_Decay Function')
plt.subplot(427)
plt.plot(xx_event_Fourier,yy_event_Fourier)
plt.title('Events_Fourier')
plt.subplot(428)
plt.plot(x,y_event)
plt.title('Events')
plt.show()