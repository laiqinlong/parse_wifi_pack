class map_pack():
    data_len = 0
    def __init__(self,line):
        if(len(line)<10):
            self.flag = 0
            return
        self.line_index = int(line[0], 16)
        line_reserve = int(line[1], 16)
        self.x1,self.y1 = self.get_start_point(line[2:5])
        self.line_len = int(line[8], 16)
        self.data_len = int(line[9], 16)
        temp_line = line[10:]
        bin_str = []
        flag = self.is_true(line)
        if flag:
            for num in temp_line:
                temp_list = self.str2bin(num)
                bin_str.append(self.parse_point_data(temp_list))
            point_list = []
            for i in bin_str:
                for j in i:
                    for k in j:
                        point_list.append(k)
            self.x2 = self.x1 + self.line_len
            self.y2 = self.y1 + int(len(point_list) / self.line_len)
    def is_true(self,line):
        if self.data_len > len(self.temp_line):
            return 0
        elif self.data_len < len(self.temp_line):
            diff = self.data_len - len(self.temp_line)
            temp_line = self.temp_line[:diff]
            return 1
    def get_start_point(num_list):
        x1 = int(num_list[0], 16) & 0xf0
        x2 = int(num_list[1], 16) & 0xf0
        x3 = int(num_list[2], 16) & 0xf0
        x = (x1 << 4) + x2 + (x3 >> 4)
        y1 = int(num_list[0], 16) & 0x0f
        y2 = int(num_list[1], 16) & 0x0f
        y3 = int(num_list[2], 16) & 0x0f
        y = (y1 << 8) + (y2 << 4) + y3
        return (x,y)
    # 返回的是二进制
    def str2bin(num):
        test_flag = 0
        if test_flag:
            temp_list = bin(int(num))
        else:
            temp_list = bin(int(num, 16))
        temp_list = temp_list.replace('0b', '')
        temp_list = list(temp_list)
        while (len(temp_list) < 8):
            temp_list.insert(0, '0')
        return temp_list

    # 返回的是0，1，2
    def parse_point_data(bin_list):
        data = ''.join(bin_list[2:])
        data = '0b' + data
        data = int(data, 2)
        temp = []
        if bin_list[0] + bin_list[1] == '00':
            temp.append('0' * data)
        elif bin_list[0] + bin_list[1] == '01':
            temp.append('1' * data)
        elif bin_list[0] + bin_list[1] == '10':
            temp.append('2' * data)
        elif bin_list[0] + bin_list[1] == '11':
            for i in range(2, 7, 2):
                temp.append(str(int(bin_list[i] + bin_list[i + 1], 2)))
        return temp
