from map_display import show_map
def str2bin(num):
    test_flag=0
    if test_flag:
        temp_list = bin(int(num))
    else:
        temp_list = bin(int(num,16))
    temp_list = temp_list.replace('0b','')
    temp_list = list(temp_list)
    while (len(temp_list) < 8):
        temp_list.insert(0, '0')
    return temp_list


def get_x(num_list):
    x1 = int(num_list[0], 16) & 0xf0
    x2 = int(num_list[1], 16) & 0xf0
    x3 = int(num_list[2], 16) & 0xf0
    x = (x1 << 4) + x2 + (x3 >> 4)
    return x

def get_y(num_list):
    y1 = int(num_list[0], 16) & 0x0f
    y2 = int(num_list[1], 16) & 0x0f
    y3 = int(num_list[2], 16) & 0x0f
    y = (y1 << 8) + (y2 << 4 ) + y3
    return y

# 返回的是0，1，2
def parse_point_data(bin_list):
    data = ''.join(bin_list[2:])
    data = '0b'+data
    data = int(data, 2)
    temp=[]
    if bin_list[0]+bin_list[1] == '00':
        temp.append('0'*data)
    elif bin_list[0]+bin_list[1] == '01':
        temp.append('1'*data)
    elif bin_list[0]+bin_list[1] == '10':
        temp.append('2'*data)
    elif bin_list[0]+bin_list[1] == '11':
        for i in range(2,7,2):
            temp.append(str(int(bin_list[i]+bin_list[i+1],2)))
    return temp

def reset_limit(x1,y1,x2,y2):
    if a.x_min > x1:
        a.x_min = x1
    if a.x_max < x2:
        a.x_max = x2
    if a.y_min > y1:
        a.y_min = y1
    if a.y_max < y2:
        a.y_max = y2
def num_type(x1,y1,x2,y2,point_list,f_write):
    num_i = 0
    reset_limit(x1, y1, x2, y2)
    for i in range(x1, x2 ):
        for j in range(y1, y2 ):
            if(point_list[num_i]== '0'):
                temp_line = "$A" + '%d,%d!\n'%(i-512, j-512)
            if (point_list[num_i] == '1'):
                a.show_green(i,j)
                temp_line = "$F" + '%d,%d!\n'%(i-512, j-512)
            if (point_list[num_i] == '2'):
                a.show_red(i, j)
                temp_line = "$B" + '%d,%d!\n'%(i-512, j-512)
            if (point_list[num_i] == '3'):
                a.show_yellow(i,j)
                temp_line = "$C" + '%d,%d!\n'%(i-512, j-512)
            num_i = num_i + 1
            f_write.writelines(temp_line)
def new_whole_map(line):
    print(line.split(','))
    line.replace('\n','')
    line=line.split(' ')
    line_len=len(line)
    if(line_len < 8):
        return 0
    if(1):
        pass
    # try:
        line_index = int(line[0], 16)
        if(line_index==0):
            return
        line_reserve = int(line[1], 16)
        x1 = get_x(line[2:5])
        y1 = get_y(line[2:5])
        print("x1=%d,y1=%d"%(x1,y1))
        line_len = int(line[8], 16)
        x2 = x1 + line_len
        data_len = int(line[9], 16)
        temp_line=line[10:]
        bin_str=[]
        if data_len > len(temp_line):
            return 0
        elif data_len < len(temp_line):
            diff = data_len-len(temp_line)
            temp_line = temp_line[:diff]
        for num in temp_line:
            temp_list=str2bin(num)
            bin_str.append(parse_point_data(temp_list))

        point_list=[]
        for i in bin_str:
            for j in i:
                for k in j:
                    point_list.append(k)
        print(point_list)
        print("point_list_len=%d"%len(point_list))
        y2 = y1 + int(len(point_list)/line_len)
        # num_type(x1, y1, x2, y2, point_list, f_write)
        num_type(y1,x1,y2,x2, point_list, f_write)
    # except:
    if(0):
        print('error')
        return 0

    return (line_index,line_reserve,(x1, y1),(x2, y2))


if __name__ == '__main__':
    f_open=open('test.txt','r',encoding='utf8')
    f_write = open('write.txt', 'w')
    f_test = open('data.txt','w')
    a=show_map(1024)
    for line in f_open:
        line=line[10:]
        line=line.replace('new map debug:','')
        f_test.writelines(line)
        new_whole_map(line)
    a.show()
    f_write.close()
    '''
    test_case = [0x0, 0x0, 0x0, 0x43, 0x1f, 0x0, 0x44, 0x51, 0x8, 0x5, 0x47, 0x82, 0x46, 0xe1, 0x43, 0x3]
    test_case = str(test_case)
    test_line = test_case.replace(',', ' ')
    test_line = test_line.replace('[', '')
    test_line = test_line.replace(']', '')
    new_whole_map(test_line)
        '''