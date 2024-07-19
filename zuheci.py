import pandas as pd
from itertools import product

# 读取Excel文件
file_path = 'c:\\Users\\ROG\\Desktop\\饭煲三项概念研究搜索词库清单.xlsx'
sheet_name = '电商好口感搜索词'

# 读取指定的sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 提取指定范围的单元格数据
col1 = df.iloc[0:27, 0].dropna().tolist()  # 第一列数据范围为A2:A27
col2 = df.iloc[0:6, 1].dropna().tolist()   # 第二列数据范围为B2:B6

# 生成两两组合并组合成一个词
combinations = [''.join(pair) for pair in product(col1, col2)]

# 打印所有新的组合词
for combination in combinations:
    print(combination/n)

# # 转换为DataFrame
# combinations_df = pd.DataFrame(combinations, columns=['组合搜索词'])

# # 保存结果到新的Excel文件
# output_path = 'c:\\Users\\ROG\\Desktop\\组合搜索词combinations_output.xlsx'
# combinations_df.to_excel(output_path, index=False)

# print(f'组合结果已保存到 {output_path}')


