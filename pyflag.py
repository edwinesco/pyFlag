import matplotlib.pyplot as py
import matplotlib.patches as patch


rojo = patch.Rectangle((0,1), width=11, height=2, facecolor='#CE1126', edgecolor='grey')
azul = patch.Rectangle((0,3), width=11, height=2, facecolor='#0038A8', edgecolor='grey')
amarillo = patch.Rectangle((0,5), width=11, height=3, facecolor='#FCD116', edgecolor='grey')

eje = py.subplot()

eje.add_patch(rojo)
eje.add_patch(azul)
eje.add_patch(amarillo)

py.axis('equal')
py.show()