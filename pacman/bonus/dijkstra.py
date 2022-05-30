def find_by_location(location, nodes):
    for node in nodes:
        if node[0] == location:
            return node
    return []


def find_by_value(nodes, val):
    for n in nodes:
        if n[1] == val:
            return n

def initialize_map(pac_map, nodes, walls):
    x = 0
    y  = 0
    for l in pac_map:
        x = 0
        for ch in l:
            if ch == 'P':
                node = [(y, x), -84, False, (-1, -1)]
                nodes.append(node)
            if ch == 'F':
                node = [(y, x), 0, True, (-1, -1)]
                nodes.append(node)
            if ch == '0':
                node = [(y, x), float('inf'), False, (-1, -1)]
                nodes.append(node)
            if ch == '1':
                node = [(y, x), -42, False, (-1, -1)]
                walls.append(node)
            x = x + 1
        y = y + 1



def explore_edges(n, nodes, walls):
    location = n[0]
    nort = (location[0] - 1, location[1])
    ost = (location[0], location[1] + 1)
    sout = (location[0] + 1, location[1])
    we = (location[0], location[1] - 1)
    cost = n[1]
    north = find_by_location(nort, nodes)
    
    if north:
        if north[1] == -84:
            return True
        if (cost + 1) < north[1]:
            north[1] = cost + 1
            nodes.sort(key=lambda x: x[1])


    east = find_by_location(ost, nodes)
    if east:
        if east[1] == -84:
            return True
        if (cost + 1) < east[1]:
            east[1] = cost + 1
            nodes.sort(key=lambda x: x[1])

    south = find_by_location(sout, nodes)
    if south:
        if south[1] == -84:
            return True
        if (cost + 1) < south[1]:
            south[1] = cost + 1
            nodes.sort(key=lambda x:x[1])

    west = find_by_location(we, nodes)
    if west:
        if west[1] == -84:
            return True
        elif (cost + 1) < west[1]:
            west[1] = cost + 1
            nodes.sort(key=lambda x: x[1])
    
    nodes.remove(n)
    walls.append(n)

    for no in nodes:
        if no[1] != -84:
            if explore_edges(no, nodes, walls):
                return True

def run_dijkstra(pac_map):
    nodes = []
    walls = []
    initialize_map(pac_map, nodes, walls)
    start_node = find_by_value(nodes, 0)
    explore_edges(start_node, nodes, walls)

    #appending all the walls back when the algo is done
    for w in walls:
        nodes.append(w)
    nodes.sort(key=lambda x: x[0])
    return nodes

