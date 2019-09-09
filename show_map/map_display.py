import numpy as np
import matplotlib.pyplot as plt
class show_map():
    map_size=0
    x_min = 2048
    x_max = 0
    y_min = 2048
    y_max = 0
    def __init__(self,size):
        self.map_size = (size,size,3)
        self.map_point_list = np.ones(self.map_size,dtype='int')*255

    def show_red(self,x,y):
        red ="255 0 0"
        self.map_point_list[x][y]=red.split()

    def show_green(self, x, y):
        green = "124 252 0"
        self.map_point_list[x][y] = green.split()

    def show_yellow(self, x, y):
        yellow = "255 255 0"
        self.map_point_list[x][y] = yellow.split()

    def show(self):
        plt.imshow(self.map_point_list)
        plt.ylim(self.x_min-20, self.x_max+20)
        plt.xlim(self.y_min-20, self.y_max+20)
        plt.show()
        pass
if __name__ == '__main__':
    a = show_map(1024)
    a.show()
