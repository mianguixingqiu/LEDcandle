import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
#振动幅度,越大越平缓，推荐值4
amp=4
#火焰胖瘦，越大越瘦,推荐数2
thick=2
#火焰妖娆程度，越大越妖娆，推荐值0.5
fi=0.5
#火焰高度，推荐值6
h=6
# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
# 添加中文字体设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义 y 的范围
y = np.linspace(0, 2 * np.pi, 1000)

# 创建图形和坐标轴
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)  # 增加底部空间以容纳更多滑块

# 添加参数滑块
axfi = plt.axes([0.25, 0.3, 0.65, 0.03])
fi_slider = Slider(axfi, '妖娆值(越大越妖娆)', 0.1, 2.0, valinit=fi)#axfi, '名字', 最小值, 最大值, 初始值

axamp = plt.axes([0.25, 0.25, 0.65, 0.03])
amp_slider = Slider(axamp, '振幅值(越大越缓)', 1, 10, valinit=amp)

axthick = plt.axes([0.25, 0.2, 0.65, 0.03])
thick_slider = Slider(axthick, '胖瘦值(越大越瘦)', 0.1, 3, valinit=thick)

axh = plt.axes([0.25, 0.15, 0.65, 0.03])
h_slider = Slider(axh, '高度(越大越高)', 1, 6, valinit=h)

# 初始化线条
# 初始化线条时添加label参数
line, = ax.plot([], [], lw=2, label='主火焰')
line1, = ax.plot([], [], lw=2, label='右边缘') 
line2, = ax.plot([], [], lw=2, label='左边缘')
line3, = ax.plot([], [], lw=2, label='线条3')#后面没用了，懒得去了

# 创建动画(移除cache_frame参数)
# 先定义所有需要的函数
def init():
    line.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line,line1,line2,line3

def update(frame):
    t = frame
    amplitude = y*(y-h_slider.val)**2*0.18/(h_slider.val**2*thick_slider.val)
    x = np.sin(fi_slider.val*y + t)*(np.exp(0.8*y-amp_slider.val)-np.exp(-4))*0.1
    display_indices = (y >= 0) & (y <= h_slider.val)
    y_display = y[display_indices]
    
    line.set_data(x[display_indices], y_display)
    line1.set_data((x+amplitude)[display_indices], y_display)
    line2.set_data((x-amplitude)[display_indices], y_display)
    line3.set_data(np.full_like(y_display, 100), y_display)
    return line, line1, line2, line3

# 然后再创建动画
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 15),
                  init_func=init, blit=True, interval=100)

ax.legend()
# 设置坐标轴范围
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(0, 2 * np.pi)
# 修改标题和标签设置
ax.set_xlabel(' ')#没有标签防止
ax.set_ylabel(' ') #没有标签
ax.set_title('火焰摆动效果')

# 初始化函数
def init():
    line.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line,line1,line2,line3

# 更新函数
def update(frame):
    t = frame
    amplitude = y*(y-h)**2*0.18/(h**2*thick)
    x = np.sin(fi_slider.val*y + t)*(np.exp(0.8*y-amp)-np.exp(-4))*0.1  # 使用滑块值
    
    # 计算要显示的区间索引 (0到h对应的索引)
    display_indices = (y >= 0) & (y <= h)
    y_display = y[display_indices]
    
    line.set_data(x[display_indices], y_display)
    line1.set_data((x+amplitude)[display_indices], y_display)
    line2.set_data((x-amplitude)[display_indices], y_display)
    line3.set_data(np.full_like(y_display, 100), y_display)
    return line, line1, line2, line3

# 创建动画

plt.show()
