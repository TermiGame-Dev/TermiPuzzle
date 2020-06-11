# Gerencia informações do jogo

class Logic:
    def __init__(self, map):
        self.map = map

    def player_pos(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == 'player':
                    self.player_pos_y = i
                    self.player_pos_x = j
                    return self.player_pos_x, self.player_pos_y

    def key_pressed(self, pos, key):
        if key == 'move_up':
            if pos[1]-1 >= 0:
                if self.map[pos[1]-1][pos[0]] == 'floor':
                    self.map[pos[1]][pos[0]] = 'floor'
                    self.map[pos[1]-1][pos[0]] = 'player'
                    return 1, self.map, 0
                elif self.map[pos[1]-1][pos[0]] == 'roll':
                    if pos[1]-2 >= 0:
                        if self.map[pos[1]-2][pos[0]] == 'floor':
                            self.map[pos[1]][pos[0]] = 'floor'
                            self.map[pos[1]-1][pos[0]] = 'player'
                            self.map[pos[1]-2][pos[0]] = 'roll'
                            return 1, self.map, 0
                        else:
                            return 0, self.map, 0
                    else:
                        return 0, self.map, 0
                else:
                    a = self.interact(self.map[pos[1]-1][pos[0]])
                    return a[0], self.map, a[1]
            else:
                return 0, self.map, 0
        if key == 'move_down':
            if pos[1] < len(self.map)-1:
                if self.map[pos[1]+1][pos[0]] == 'floor':
                    self.map[pos[1]][pos[0]] = 'floor'
                    self.map[pos[1]+1][pos[0]] = 'player'
                    return 1, self.map, 0
                else:
                    if self.map[pos[1]+1][pos[0]] == 'roll':
                        if pos[1]+2 < len(self.map[0]):
                            if self.map[pos[1]+2][pos[0]] == 'floor':
                                self.map[pos[1]][pos[0]] = 'floor'
                                self.map[pos[1]+1][pos[0]] = 'player'
                                self.map[pos[1]+2][pos[0]] = 'roll'
                                return 1, self.map, 0
                            else:
                                return 0, self.map, 0
                        else:
                            return 0, self.map, 0
                    else:
                        a = self.interact(self.map[pos[1]+1][pos[0]])
                        return a[0], self.map, a[1]
            else:
                return 0, self.map, 0
        if key == 'move_lefth':
            if pos[0]-1 >= 0:
                if self.map[pos[1]][pos[0]-1] == 'floor':
                    self.map[pos[1]][pos[0]] = 'floor'
                    self.map[pos[1]][pos[0]-1] = 'player'
                    return 1, self.map, 0
                else:
                    if self.map[pos[1]][pos[0]-1] == 'roll':
                        if pos[0]-2 >= 0:
                            if self.map[pos[1]][pos[0]-2] == 'floor':
                                self.map[pos[1]][pos[0]] = 'floor'
                                self.map[pos[1]][pos[0]-1] = 'player'
                                self.map[pos[1]][pos[0]-2] = 'roll'
                                return 1, self.map, 0
                            else:
                                return 0, self.map, 0
                        else:
                            return 0, self.map, 0
                    else:
                        a = self.interact(self.map[pos[1]][pos[0]-1])
                        return a[0], self.map, a[1]
            else:
                return 0, self.map, 0
        if key == 'move_right':
            if pos[0]+1 <= len(self.map[pos[1]])-1:
                if self.map[pos[1]][pos[0]+1] == 'floor':
                    self.map[pos[1]][pos[0]] = 'floor'
                    self.map[pos[1]][pos[0]+1] = 'player'
                    return 1, self.map, 0
                else:
                    if self.map[pos[1]][pos[0]+1] == 'roll':
                        if pos[0]+2 >= 0:
                            if self.map[pos[1]][pos[0]+2] == 'floor':
                                self.map[pos[1]][pos[0]] = 'floor'
                                self.map[pos[1]][pos[0]+1] = 'player'
                                self.map[pos[1]][pos[0]+2] = 'roll'
                                return 1, self.map, 0
                            else:
                                return 0, self.map, 0
                        else:
                            return 0, self.map, 0
                    else:
                        a = self.interact(self.map[pos[1]][pos[0]+1])
                        return a[0], self.map, a[1]
            else:
                return 0, self.map, 0
        if key == 'none':
            return 0, self.map, 0

    def spawn(self, summon):
        if len(summon) != 0:
            for i in range(0, len(summon)):
                if summon[i][0] == 'player':
                    if (len(self.map) % 2) != 0:
                        middle = int((len(self.map) - 1 ) / 2)
                    else:
                        middle = int(len(self.map) / 2)
                    if (len(self.map[middle]) % 2) != 0:
                        middle2 = int((len(self.map[middle]) - 1) / 2)
                    else:
                        middle2 = int(len(self.map[middle]) / 2)
                    self.map[middle][middle2] = 'player'
                else:
                    if summon[i][1] <= (len(self.map)*len(self.map[0]))-1:
                        from random import randint
                        for j in range(0, summon[i][1]):
                            posy = randint(0, len(self.map)-1)
                            posx = randint(0, len(self.map[0])-1)
                            if self.map[posy][posx] != 'player' and self.map[posy][posx] not in summon:
                                self.map[posy][posx] = summon[i][0]
            return 1, self.map

    def interact(self, obj):
        if obj == 'fire':
            return [1, -1]
        elif obj == 'block':
            return [0, 0]
        else:
            return [0, 0]

    def mob_mov(self, mob):
        from random import randint
        mobs_pos = []
        cont = 0
        if mob == 'fire':
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    if self.map[i][j] == mob:
                        mobs_pos.append([i, j])
            for i in range(0, len(mobs_pos)):
                r_move = randint(0, 100000)
                if r_move == 1 and mobs_pos[i][0]+1 < len(self.map):
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]] = 'floor'
                    self.map[mobs_pos[i][0]+1][mobs_pos[i][1]] = mob
                    cont += 1
                elif r_move == 2 and mobs_pos[i][0]-1 >= 0:
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]] = 'floor'
                    self.map[mobs_pos[i][0]-1][mobs_pos[i][1]] = mob
                    cont += 1
                elif r_move == 3 and mobs_pos[i][1]+1 < len(self.map[0]):
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]] = 'floor'
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]+1] = mob
                    cont += 1
                elif r_move == 4 and mobs_pos[i][1]-1 >= 0:
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]] = 'floor'
                    self.map[mobs_pos[i][0]][mobs_pos[i][1]-1] = mob
                    cont += 1
                else:
                    return 0, self.map, 0
        if cont != 0:
            return 1, self.map, 0
        else:
            return 0, self.map, 0
