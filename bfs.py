import sys
import math


# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

def proximiter(matrice, kr, kc):
    res={}
    if  kr != 0 and matrice[kr-1][kc] != "#":
        res['UP'] = (kr-1,kc,matrice[kr-1][kc])
    if kr != r-1 and  matrice[kr+1][kc] != "#":
        res['DOWN'] = (kr+1,kc,matrice[kr+1][kc])   
    if kc != 0 and  matrice[kr][kc-1] != "#":
        res['LEFT'] = (kr,kc-1,matrice[kr][kc-1])
    if kc != c-1 and  matrice[kr][kc+1] != "#":
        res['RIGHT'] = (kr,kc+1,matrice[kr][kc+1])
    
    return res

def proximiter_pt(matrice, kr, kc):
    res={}
    if  kr != 0 and matrice[kr-1][kc] != "#"and matrice[kr-1][kc] != "?":
        res['UP'] = (kr-1,kc,matrice[kr-1][kc])
    if kr != r-1 and  matrice[kr+1][kc] != "#" and  matrice[kr+1][kc] != "?":
        res['DOWN'] = (kr+1,kc,matrice[kr+1][kc])   
    if kc != 0 and  matrice[kr][kc-1] != "#" and  matrice[kr][kc-1] != "?":
        res['LEFT'] = (kr,kc-1,matrice[kr][kc-1])
    if kc != c-1 and  matrice[kr][kc+1] != "#" and  matrice[kr][kc+1] != "?":
        res['RIGHT'] = (kr,kc+1,matrice[kr][kc+1])
    
    return res

def dist_pt(ac,ar,bc,br):
    return abs(ac-bc) + abs(ar-br)

def find_path_bfs(maze,goal,start,que_pt):
    queue = [start]
    visited = set()
    chemins = {start: tuple()}
    while queue:
        current = queue.pop()
        
        if current[2] == goal:
            return chemins[current]

        if current in visited:
            continue
        
        visited.add(current)
        
        if que_pt:
            for direction, coord in proximiter_pt(maze,current[0],current[1]).items():
                if chemins.get(coord) is None: 
                    queue.insert(0,coord)
                    chemins[coord] = chemins[current] + tuple([direction]) 

        
        else:
            for direction, coord in proximiter(maze,current[0],current[1]).items():
                if chemins.get(coord) is None: 
                    queue.insert(0,coord)
                    chemins[coord] = chemins[current] + tuple([direction]) 

    return "NO WAY!"

# game loop
c_visited = False
tc = None
tr = None
cc = None
cr = None
c_found = False
turn=0
while True:
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    turn+=1

    kr, kc = [int(i) for i in input().split()]
    if kr == cr and kc == cc:
        c_visited = True
    matrice =[['?' for j in range(c) ]for i in range(r)]
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        matrice[i]= [*row]
        if row.find('T') != -1:
            tc = row.find('T')
            tr = i
        if row.find('C') != -1:
            cc = row.find('C')
            cr = i
            c_found = True
        if i == kr: 
            liste = [*row] 
            liste[kc] = '@'
            row = "".join(liste)
        print(row, file=sys.stderr, flush=True)
    if c_found:
        
        chemin_pt= find_path_bfs(matrice,'T',(cr,cc,matrice[kr][kc]),True) 
        longueur_chemin = len(chemin_pt)


        if longueur_chemin <= a and chemin_pt != 'NO WAY!':
            print('chemin plus court trouvé', file=sys.stderr, flush=True)
            if c_visited:
                chemin_retour = find_path_bfs(matrice,'T',(kr,kc,matrice[kr][kc]),True) 
                print(chemin_retour[0])
            else:
                chemin = find_path_bfs(matrice,'C',(kr,kc,matrice[kr][kc]),True)
                print(chemin[0])
        else:
            chemin = find_path_bfs(matrice,'?',(kr,kc,matrice[kr][kc]),False)
            print(chemin[0])
    else:
        chemin = find_path_bfs(matrice,'?',(kr,kc,matrice[kr][kc]),False)
        print(chemin[0])

       
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Rick's next move (UP DOWN LEFT or RIGHT).