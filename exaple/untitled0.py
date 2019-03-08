import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

a = np.random.random(100)*10.
a = a.reshape(10,10)

fig = plt.figure(figsize=(12,4))

N = 7
bounds = np.linspace(np.min(a), np.max(a), N+1)
print(bounds)
cmap = mpl.cm.get_cmap('RdBu', N) 

ax = fig.add_subplot(131)
cs = ax.pcolor(a, cmap=cmap) # вызываем метод pcolor. Вводим пользовательскую раскраску через cmap
print(u'Тип CS: %s' % type(cs))
cbar = fig.colorbar(cs, ax=ax) # рисуем шкалу colorbar для изображения cs. В качестве черточек шкалы указываем bounds. 
print(u'Тип CBAR: %s' % type(cbar))
# ticks=bounds
ax.set_title(u'Подбор делений под количество цветов')

# ---------------------------------------------------

ax2 = fig.add_subplot(132)
bounds = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
cmap = mpl.cm.get_cmap('ocean', len(bounds)-1)
cmap.set_over('red')
cmap.set_under('grey')
cs = ax2.pcolor(a, cmap=cmap, vmin=bounds[0], vmax=bounds[-1]) # Ставим границы для шкалы vmin и vmax.
cbar = fig.colorbar(cs, ax=ax2, ticks=bounds, extend='max', extendfrac=0.1)
ax2.set_title(u'Подбор количества цветов под заданные интервалы значений')
ax2.grid(True)
cmap.set_over('pink')

# ---------------------------------------------------

ax3 = fig.add_subplot(133)
cs = ax3.imshow(a, cmap=cmap,  vmin=bounds[0], vmax=bounds[-1]) # В методе pcolor/pcolormesh/imshow присваиваем пользовательские границы цветов norm
cbar = fig.colorbar(cs, ax=ax3, ticks=bounds, extend='both', extendfrac='auto',
                    orientation='horizontal')
ax3.set_title(u'Масштабирование цветовой шкалы')
ax3.grid(True)

plt.tight_layout()


plt.show()