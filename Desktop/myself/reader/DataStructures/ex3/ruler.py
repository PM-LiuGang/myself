# 4-2

def draw_line(tick_length, tick_label=''):
    '''用指定数量的破折号绘制一个单独的刻度线，并且在刻度线后打印一个可选的字符串标签'''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_lenght):
    '''根据刻度间隔中中央刻度线的长度来绘制刻度间隔之间副刻度线的序列'''
    if center_lenght > 0:
        draw_interval(center_lenght -1)
        draw_line(center_lenght)
        draw_interval(center_lenght - 1)

def draw_ruler(num_inches, major_lenght):
    '''整个标尺的创建，参数指定标尺的总长度及主刻度线的长度'''
    draw_line(major_lenght, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_lenght - 1)
        draw_line(major_lenght, str(j))


if __name__ == '__main__':
    draw_ruler(3, 3)