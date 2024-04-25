import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import squarify
from matplotlib.font_manager import FontProperties
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
# 设置中文字体
font_path = "/Users/liuhaoyu/Library/Fonts/Alibaba-PuHuiTi-Regular.ttf"
font = FontProperties(fname=font_path, size=10)

# 读取Excel文件
df = pd.read_excel('//Users/liuhaoyu/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/5f020b8d593d4c9a337ed001af1964ad/Message/MessageTemp/0e778a893b7a9b760e66b94fdc9bb86b/File/D1-1_0420top产品需求 @浩宇/爱分享家居生活的-top产品-插座_实体统计.xlsx', sheet_name='功能功效')

# 按照“出现次数”列降序排序，并选取前20行
df_sorted = df.sort_values(by='出现次数', ascending=False).head(20)

# 获取绘图所需的数据
sizes = df_sorted['出现次数'].tolist()
labels = df_sorted['实体值'].tolist()
labels_1 = [f"{entity} ,{count}" for entity, count in zip(df_sorted['实体值'], df_sorted['出现次数'])]

# # 计算字体大小的逐渐减小步长
# font_sizes = np.linspace(20, 10, len(sizes))

# 设置字体大小的对数尺度的最大值和最小值
log_min_size = np.log10(8)  # 对应于最小字体大小10
log_max_size = np.log10(20)  # 对应于最大字体大小20

# 生成一个线性间隔的数组，这里的间隔是在对数尺度上的
log_sizes = np.linspace(log_min_size, log_max_size, len(sizes))

# 将线性间隔的数组转换回实际的字体大小
font_sizes = 10 ** log_sizes  # 应用10的指数函数得到实际的字体大小

# 如果需要将最大的字体大小应用于最小的值，则需要反转数组
font_sizes = font_sizes[::-1]


# 定义渐变色的起始色、中间色和结束色
color_start = '#792F2D'
color_mid = '#A44340'  # 这是中间值的颜色
color_end = '#E2C2C2'

# 定义渐变色的颜色映射
cmap = LinearSegmentedColormap.from_list('custom_cmap', [color_start, color_mid, color_end], N=len(labels))

# 你可以在这里指定一个颜色列表，或者生成一个颜色列表
colors = [cmap(i/float(len(labels))) for i in range(len(labels))]

# 绘制树状图
fig = plt.figure(figsize=(4.77*2, 3.10*2))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])

# 左侧添加树状图
ax1 = plt.subplot(gs[0])
squarify.plot(sizes=sizes, color=colors, alpha=1)  # 添加 vertical=False 参数
plt.axis('off')

# 手动在树状图矩形上添加文本
for rect, label, fs in zip(ax1.patches, labels_1, font_sizes):
    x, y, width, height = rect.get_bbox().bounds
    ax1.text(x + width/2, y + height/2, label,
             ha='center', va='center',
             fontproperties=FontProperties(fname=font_path, size=fs))

# 添加白色边框
for rectangle in ax1.patches:
    # 获取矩形的位置和大小
    x, y, w, h = rectangle.get_bbox().bounds
    # 绘制白色边框
    rect = plt.Rectangle((x, y), w, h, fill=False, edgecolor='white', linewidth=1)
    ax1.add_patch(rect)

plt.axis('off')

# 右侧添加对应的正方形和标签
ax2 = plt.subplot(gs[1], frameon=False)
ax2.axis('off')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, len(colors))
for i, color in enumerate(colors):
    ax2.add_patch(plt.Rectangle((0.2, len(colors)-i-1+0.2), 0.1, 0.6, color=color))  # 修改了矩形的宽度和高度
    ax2.text(0.4, len(colors)-i-0.55, labels[i], va='center',fontproperties=font)

plt.tight_layout()
plt.show()
