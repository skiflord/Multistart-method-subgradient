import matplotlib.pyplot as plt
import os

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def plot_chart(data, vec3, *args):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data)

    x_line_tracking = []
    y_line_tracking = []

    for a in vec3:
        (x_value,y_value,haar_length) = a
        y_start = y_value + 10
        y_end = y_value - 10
        x_carrier_right = x_value + haar_length
        x_carrier_left = x_value - haar_length
        x = [x_carrier_left, x_value, x_value, x_carrier_right]
        y = [y_start, y_start, y_end, y_end]
        ax.plot(x, y, '-', color='black', linewidth=1)
        x_line_tracking.append(x_value)
        y_line_tracking.append(y_value)

    #plt.errorbar(point,data[point],fmt='ro')
    ax.plot(x_line_tracking, y_line_tracking, '-', color='red', linewidth=1)
    ax.grid(True)
    
    i = args[0]
    h = args[1]
    # save('pic_i%d_h%d'%(i,h), fmt='png')
    plt.cla()
    ax.clr()
    
    # if args != None:
    #     i = args[0]
    #     h = args[1]
    #     save('pic_i%d_h%d'%(i,h), fmt='png')
    # else:
    #     plt.show()