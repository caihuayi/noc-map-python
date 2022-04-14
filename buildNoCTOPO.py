
def buildNoCTOPO(mesh_x, mesh_y, mesh_z):
	topo = {}

	count = mesh_x * mesh_y * mesh_z
	for i in range(1, count+1):
		j = i-1
		edges = {}
		edges[i] = 0
		# 判断有无向前连接
		if (j//mesh_x) % mesh_y != 0:
			edges[i - mesh_y] = 1
		# 判断有无向后连接
		if (j//mesh_x) % mesh_y != mesh_y-1:
			edges[i + mesh_y] = 1
		# 判断有无向左连接
		if (j % mesh_x) != 0:
			edges[i-1] = 1
		# 判断有无向右连接
		if (j % mesh_x) != mesh_x-1:
			edges[i+1] = 1
		# 判断有无向下连接
		if (j // (mesh_x * mesh_y) != 0):
			edges[i - mesh_x*mesh_y] = 1
		# 判断有无向上连接
		if (j // (mesh_x * mesh_y) != mesh_z-1):
			edges[i + mesh_x * mesh_y] = 1
		topo[i] = edges	
	return topo

def main():
    mesh_x = 3
    mesh_y = 3
    mesh_z = 1
    topo = buildNoCTOPO(mesh_x, mesh_y, mesh_z)
    print (topo)

if __name__ == '__main__':
    main()
