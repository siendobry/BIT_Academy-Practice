class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        self.__map = T
        self.__x = x
        self.__y = y
        self.__battery = b
        if b <= 0:
            self.__status = 1
            T[x][y] = "X"  
        elif T[x][y] == "T":
            self.__status = 0
            T[x][y] = "R"
        elif T[x][y] == "B":
            self.__status = 0
            self.__battery += 10
            T[x][y] = "R"
        elif T[x][y] == "G":
            self.__status = 2
            T[x][y] = "X"
        elif T[x][y] == "W":
            self.__status = 3
            T[x][y] = "X"
        self.__curr = T[x][y]

    def left(self, val = 1):
        if val > 0 and self.__status == 0:
            for i in range(val):
                if self.__y <= 0 or self.__map[self.__x][self.__y - 1] == "G":
                    self.__status = 2
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x][self.__y - 1] == "W":
                    self.__y -= 1
                    self.__status = 3
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x][self.__y - 1] == "B":
                    self.__map[self.__x][self.__y - 1] = "T"
                    self.__battery += 10
                self.__y -= 1
                self.__map[self.__x][self.__y] = self.__curr
                self.__curr = self.__map[self.__x][self.__y]
                self.__map[self.__x][self.__y] = "R"
                self.__battery -= 1
                if self.__battery == 0:
                    self.__status = 1
                    self.__map[self.__x][self.__y] = "X"
                    break
        return self
                

    def right(self, val = 1):
        if val > 0 and self.__status == 0:
            for i in range(val): 
                if self.__y >= len(self.__map[0]) - 1 or self.__map[self.__x][self.__y + 1] == "G":
                    self.__status = 2
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x][self.__y + 1] == "W":
                    self.__y += 1
                    self.__status = 3
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x][self.__y + 1] == "B":
                    self.__map[self.__x][self.__y + 1] == "T"
                    self.__battery += 10
                self.__y += 1
                self.__map[self.__x][self.__y] = self.__curr
                self.__curr = self.__map[self.__x][self.__y]
                self.__map[self.__x][self.__y] = "R"
                self.__battery -= 1
                if self.__battery == 0:
                    self.__status = 1
                    self.__map[self.__x][self.__y] = "X"
                    break
        return self
            
    def up(self, val = 1):
        if val > 0 and self.__status == 0:
            for i in range(val):
                if self.__x <= 0 or self.__map[self.__x - 1][self.__y] == "G":
                    self.__status = 2
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x - 1][self.__y] == "W":
                    self.__x -= 1
                    self.__status = 3
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x - 1][self.__y] == "B":
                    self.__map[self.__x - 1][self.__y] == "T"
                    self.__battery += 10
                self.__x -= 1
                self.__map[self.__x][self.__y] = self.__curr
                self.__curr = self.__map[self.__x][self.__y]
                self.__map[self.__x][self.__y] = "R"
                self.__battery -= 1
                if self.__battery == 0:
                    self.__status = 1
                    self.__map[self.__x][self.__y] = "X"
                    break
        return self
            
    def down(self, val = 1):
        if val > 0 and self.__status == 0:
            for i in range(val):
                if self.__x >= len(self.__map) - 1 or self.__map[self.__x + 1][self.__y] == "G":
                    self.__status = 2
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x + 1][self.__y] == "W":
                    self.__x += 1
                    self.__status = 3
                    self.__map[self.__x][self.__y] = "X"
                    self.__battery -= 1
                    break
                elif self.__map[self.__x + 1][self.__y] == "B":
                    self.__map[self.__x + 1][self.__y] == "T"
                    self.__battery += 10
                self.__x += 1
                self.__map[self.__x][self.__y] = self.__curr
                self.__curr = self.__map[self.__x][self.__y]
                self.__map[self.__x][self.__y] = "R"
                self.__battery -= 1
                if self.__battery == 0:
                    self.__status = 1
                    self.__map[self.__x][self.__y] = "X"
                    break
        return self

    def get_status(self):
        return self.__status

    def get_battery(self):
        return self.__battery

    def get_map(self):
        return self.__map

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
