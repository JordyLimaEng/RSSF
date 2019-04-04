import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.pyplot as points

print("DIMENSÃO DA REDE: \n")
row = int(input("Dimension in x (km) = "))
col = int(input("Dimension in y (km) = "))

host_max = (row * col)
hosts_n = int(input("# OF HOSTS: "))

hosts_x = []
hosts_y = []

for i in range(hosts_n):
    print("Host - ", i)
    hosts_x.append(int(input("Host pos in x: ")))
    hosts_y.append(int(input("Host pos in y: ")))
    print("\n")

print(hosts_x)
print(hosts_y)

#Drawing the points
for i in range(hosts_n):
    points.plot([hosts_x], [hosts_y], 'ro') #Plot each hosts in their coordinates
    print(i)

#Expands the graph from 0 x 0 to col x row
points.axis([0, 0, 0, 0])
points.xlabel('Dist y')
points.ylabel('Dist x')
points.grid(True)
axes = points.gca()
axes.set_xlim([-0.8,col])
axes.set_ylim([-0.8,row])
points.show()

#Drawing the path between the points
fig, ax = plt.subplots()
Path = mpath.Path
path_data = []

for i in range(hosts_n):
    path_data.append((Path.MOVETO, (hosts_x[i], hosts_y[i]))) #Draw a line between the points

path_data.append((Path.MOVETO, (hosts_x[0], hosts_y[0]))) #Close the path

codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot points and connect lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
ax.grid()
ax.axis('equal')
plt.show()
