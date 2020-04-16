import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

# Параметры антенной решётки
N = 10
lmb = 3
d = lmb/2
k = 2*math.pi/lmb

nn = 400 # Точность угла тета (число отсчётов)
theta = np.zeros(nn)
DN = np.zeros(theta.size)

#for i in range(1, theta.size):
#    theta[i] = i*math.pi/nn
#    psi = k * d * math.sin(theta[i])
#    DN[i] = (math.sin(N*psi/2))/(N*math.sin(psi/2))
#DN[0]=1

#print(theta)
#print(DN)

for i in range(0, theta.size):
    theta[i] = i*2*math.pi/nn-math.pi
    summ = 0
    for x in range(0, N):
        summ += cmath.exp(-1j * k * x * d * math.sin(theta[i]))
    DN[i] = 20*math.log10(abs(summ)/N)
    #theta[i] *= 180/math.pi

fig, ax = plt.subplots(figsize=(15, 8)) # figsize(,) задаёт размер картинки
ax.plot(theta*180/math.pi, DN, color="blue", linewidth=2, linestyle='-', label="DN(Theta)") #labels=['DN(Theta)', '-', '-'])
ax.set_title('F(Theta)')
ax.legend(loc='upper left')
ax.set_xlabel('Theta')
ax.set_ylabel('Field')
ax.grid(True)
ax.set_xlim(xmin=-90, xmax=90)    #ax.set_xlim(xmin=theta[0], xmax=theta[-1])
ax.set_ylim(ymin=-60, ymax=max(DN))
ax.grid(True, axis='y', color='g', linewidth=1, linestyle='--')
ax.grid(True, axis='x', color='g', linewidth=1, linestyle='--')
fig.tight_layout()
plt.show()

fig2 = plt.figure(figsize=(20,20)) # зададим явно размер полотна, чтобы графики не перекрывались
ax2 = fig2.add_subplot(231, projection='polar')
ax2.plot(theta, DN, color='r', linewidth=2)
ax2.set_ylim(ymin=-50, ymax=max(DN))
    # Так как 0 и 2*pi - это одна и та же точка, то значение в ней должно быть одно
    # Однако, будет разрыв между последней точкой и нулевой.
    # Чтобы его убрать, искусственно соединим эти точки.
    # Замыкаем (соединяем конец с началом)
#ax2.plot((theta[-1],theta[0]),(DN[-1],DN[0]), color='r', linewidth=1.)
ax2.grid(True, color='green', linestyle='--')
ax2.set_title("F(Theta)", loc='center')
plt.tight_layout()
plt.show()

lag = math.pi/nn
phi = np.arange(-math.pi/2, math.pi/2 , lag)
DN2 = np.zeros(nn)
for i in range (nn):
    DN2[i] = DN[i]*DN[i]


a = np.trapz(DN2[(theta >= -math.pi/2) & (theta <= math.pi/2)])
print(a)
#KND = 4*math.pi / (())    

#np.trapz(y[(x >= 11) & (x < 18)])