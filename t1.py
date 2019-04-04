import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.pyplot as points

'''
fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (0, 0)),
    (Path.MOVETO, (1, 1)),
    (Path.MOVETO, (2, 2)),
    (Path.MOVETO, (3, 1)),
    (Path.MOVETO, (5, 6)),
    (Path.MOVETO, (4, 2)),
    (Path.MOVETO, (3, 5)),
    (Path.MOVETO, (2, 8)),
    (Path.MOVETO, (6, 8)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
ax.axis('equal')
plt.show()
'''

print("DIMENSÃO DA REDE: \n")
row = int(input("Dimensão em x (km) = "))
col = int(input("Dimensão em y (km) = "))

host_max = (row * col)
hosts_n = int(input("NUMEROS DE HOSTS: "))

hosts_x = []
hosts_y = []

for i in range(hosts_n):
    print("Host - ", i)
    hosts_x.append(int(input("Host pos em x: ")))
    hosts_y.append(int(input("Host pos em y: ")))
    print("\n")

print(hosts_x)
print(hosts_y)
    
for i in range(hosts_n):
    points.plot([hosts_x], [hosts_y], 'ro')


points.axis([0, 0, 0, 0])
points.xlabel('Dist y')
points.ylabel('Dist x')
points.grid(True)
axes = points.gca()
axes.set_xlim([-0.8,col])
axes.set_ylim([-0.8,row])
points.show()