import cv2
import matplotlib.pyplot as plt

video_path = 'D:/Jupyter/函数生成火焰/火焰视频处理/fire.mp4'  # 替换为你的视频路径
x,y,w=1086,60,375
h=w*2#裁剪区域的高,裁剪后应该是16*8
#h=w#裁剪区域的高,裁剪后应该是8*8
step=w//8+1#采样步长,采样后应该是16*8
jumpframe=10#前面跳过的帧数
readframe=600#读取的帧数，适用于8*8
readframe=300#读取的帧数，适用于16*8
file_name = 'D:/Jupyter/函数生成火焰/火焰视频处理/fire.txt'

# plt显示彩色图片,调试使用
def plt_show0(img):
    b,g,r= cv2.split(img)
    img=cv2.merge([r,g,b])
    plt.imshow(img)
    plt.show()
#plt显示灰度图片,调试使用
def plt_show(img):
    plt.imshow(img, cmap='gray')
    plt.show()

cap = cv2.VideoCapture(video_path)# 读取视频文件

outfile= open(file_name, "w")#读取txt文件
for i in range(jumpframe):#跳过前面的帧
    ret, frame = cap.read()
for i in range(readframe):#读取帧
    ret, frame = cap.read()
    if not ret:
        print("无法读取视频")
        break
    else:
        # 转换为灰度图
        cropped=frame[y:y+h,x:x+w]#裁剪
        bincropped=cropped[::step,::step]#下采样
        #下面有些混乱，本着能跑就不要动的原则，就不动了
        _, bingary = cv2.threshold(bincropped, 127, 255, cv2.THRESH_BINARY)
        bingray = cv2.cvtColor(bincropped, cv2.COLOR_BGR2GRAY)
        # 二值化处理
        _, binary = cv2.threshold(bingray, 127, 255, cv2.THRESH_BINARY)
        binary=binary//255
        #print(binary)
        binary_str = "{" + ",".join("B"+"".join(map(str, row)) for row in binary) + "}"
        #转换成arduino支持的格式：{B00000000,...,B00000000},{B00000000,...,B00000000}...
        
        print(binary_str+",",file=outfile)#把数据写入txt文件
        #以下调试用
        # 显示结果（使用你已有的plt_show函数）
        #plt_show(binary)  # 显示二值化图像
        #bin816=binary[::47,::47]
        #plt_show(bin)  # 显示二值化图像
        #print(bin816) 
        #plt_show0(bincropped)  # 显示原始第一帧对比
        #break  # 只显示第一帧，然后退出循环

# 释放资源
cap.release()
outfile.close()
# 读取txt文件,删除最后一个逗号
with open(file_name, 'r+') as f:
    content = f.read()
    f.seek(0)
    f.write(content[:-1])
    f.truncate()