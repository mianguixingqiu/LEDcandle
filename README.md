# LEDcandles
本仓库主要用于记录用于电子蜡烛的arduino程序与视频处理工具。
## 单片机程序
**该项目基于arduino编程**

### 前期准备：

安装airmcu库，和tm16xx led and buttons库。

准备一个ch340模块，需安装驱动，一搜就有，很多。

电路设计详见立创开源平台：[电子蜡烛v2](https://oshwhub.com/mgxq/dian-zi-la-zhu-v2)

### 相关资料：

主控： [AIR001文档](https://c.vue2.cn/attachment/20230721175506039_AIR001%E8%8A%AF%E7%89%87%E6%95%B0%E6%8D%AE%E6%89%8B%E5%86%8C1.0.4.pdf)
[AIR001在线文档](https://wiki.luatos.com/chips/air001/index.html)

led驱动：[TM1640文档](https://atta.szlcsc.com/upload/public/pdf/source/20210125/C41327_2B9DB4F40466A73C374D651D231B64AE.pdf)

串口转usb模块：[ch340文档](https://atta.szlcsc.com/upload/public/pdf/source/20240313/115CDE92081B1D6CB446704AD5D0F5F2.pdf)

## 视频转换工具
使用python来处理，需要安装opencv2，如果没有安装请使用`pip install opencv-python`

## 火焰生成函数
使用python的matplotlib的库，主要使用指数函数和三次幂函数。之后再采样一下，就可以用于点阵火焰了。
两个示例视频，都是来源于B站。

火焰视频来源：[B站](https://www.bilibili.com/video/BV1gZ4y1S7E6)up主：分享素材的小曼

badapple视频来源：[B站](https://www.bilibili.com/video/BV1xx411c79H)up主：折射
