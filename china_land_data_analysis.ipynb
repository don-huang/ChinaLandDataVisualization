import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
# 设置中文字体支持 (根据您本地环境可能需要调整，如 'SimHei' 或 'Microsoft YaHei')
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 1. 准备数据
# ==========================================

# A. 土地供应数据 (单位: 万公顷)
land_data = {
    'Year': ['2022', '2023', '2024'],
    'Total Supply': [76.6, 74.9, 60.6],       # 总供应量
    'Infrastructure': [45.7, 49.0, 38.0],     # 基础设施用地
    'Real Estate': [11.0, 8.4, 7.2]           # 房地产用地
}
df_land = pd.DataFrame(land_data)

# B. 行业杠杆率对比数据 (单位: %)
leverage_data = {
    'Indicator': ['资产负债率\n(Asset Liability)', '净负债率\n(Net Gearing)'],
    '2015': [75.0, 74.0],   # 2015年数据 (扩张期)
    '2025': [74.5, 170.2]   # 2025年数据 (出清期)
}
df_leverage = pd.DataFrame(leverage_data)

# C. 房地产投资依赖度趋势 (模拟不同城市类型)
years = np.arange(2014, 2025)
# 模拟数据：高依赖城市 (如三亚/郑州高峰期) vs 一线城市
trend_high_risk = [32, 35, 38, 36, 30, 28, 26, 22, 18, 15, 12] 
trend_tier1 = [18, 19, 20, 18, 17, 16, 15, 14, 13, 12, 11]
trend_limit = [25] * len(years) # 黄奇帆理论的25%警戒线

# ==========================================
# 2. 绘制图表
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
plt.subplots_adjust(hspace=0.3, wspace=0.25)

# --- 图1: 建设用地供应趋势 (柱状图) ---
width = 0.25
x = np.arange(len(df_land['Year']))
ax1 = axes[0, 0]
ax1.bar(x - width, df_land['Total Supply'], width, label='供应总量', color='#1f77b4')
ax1.bar(x, df_land['Infrastructure'], width, label='基础设施', color='#ff7f0e')
ax1.bar(x + width, df_land['Real Estate'], width, label='房地产用地', color='#2ca02c')

ax1.set_xticks(x)
ax1.set_xticklabels(df_land['Year'], fontsize=12)
ax1.set_ylabel('供应面积 (万公顷)', fontsize=12)
ax1.set_title('2022-2024年 中国建设用地供应结构趋势', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# 标注数值
for i in range(len(x)):
    ax1.text(x[i]-width, df_land['Total Supply'][i]+1, str(df_land['Total Supply'][i]), ha='center', fontsize=10)
    ax1.text(x[i], df_land['Infrastructure'][i]+1, str(df_land['Infrastructure'][i]), ha='center', fontsize=10)
    ax1.text(x[i]+width, df_land['Real Estate'][i]+1, str(df_land['Real Estate'][i]), ha='center', fontsize=10)

# --- 图2: 房地产行业杠杆率对比 (分组柱状图) ---
ax2 = axes[0, 1]
x_lev = np.arange(len(df_leverage['Indicator']))
ax2.bar(x_lev - width/2, df_leverage['2015'], width, label='2015年 (扩张期)', color='#9467bd')
ax2.bar(x_lev + width/2, df_leverage['2025'], width, label='2025年 (出清期)', color='#d62728')

ax2.set_xticks(x_lev)
ax2.set_xticklabels(df_leverage['Indicator'], fontsize=12)
ax2.set_ylabel('比率 (%)', fontsize=12)
ax2.set_title('房地产行业杠杆率结构变化 (2015 vs 2025)', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# 标注数值
for i in range(len(x_lev)):
    ax2.text(x_lev[i]-width/2, df_leverage['2015'][i]+2, f"{df_leverage['2015'][i]}%", ha='center', fontsize=10)
    ax2.text(x_lev[i]+width/2, df_leverage['2025'][i]+2, f"{df_leverage['2025'][i]}%", ha='center', fontsize=10)

# --- 图3: 房地产投资依赖度走势 (折线图) ---
ax3 = axes[1, 0]
ax3.plot(years, trend_high_risk, marker='o', linewidth=2, label='高依赖型城市 (模拟)', color='#d62728')
ax3.plot(years, trend_tier1, marker='s', linewidth=2, label='稳健型城市 (模拟)', color='#1f77b4')
ax3.plot(years, trend_limit, linestyle='--', linewidth=2, label='25% 警戒线 (黄奇帆理论)', color='black')

ax3.set_ylabel('房地产投资占固定资产投资比重 (%)', fontsize=12)
ax3.set_title('中国城市房地产投资依赖度十年变迁', fontsize=14, fontweight='bold')
ax3.set_xticks(years)
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.5)
# 添加注释
ax3.annotate('去库存/棚改高峰', xy=(2016, 38), xytext=(2017, 42),
             arrowprops=dict(facecolor='black', shrink=0.05))

# --- 图4: 房地产用地占比变化 (面积图) ---
ax4 = axes[1, 1]
re_share = [11.0/76.6*100, 8.4/74.9*100, 7.2/60.6*100]
ax4.plot(df_land['Year'], re_share, marker='D', color='#2ca02c', linewidth=2, linestyle='-')
ax4.fill_between(df_land['Year'], re_share, color='#2ca02c', alpha=0.1)

ax4.set_ylabel('占比 (%)', fontsize=12)
ax4.set_title('房地产用地占总建设用地供应比例', fontsize=14, fontweight='bold')
ax4.set_ylim(0, 20)
ax4.grid(True, linestyle='--', alpha=0.5)

for i, v in enumerate(re_share):
    ax4.text(i, v+0.8, f"{v:.1f}%", ha='center', fontweight='bold', fontsize=11, color='#2ca02c')

plt.show()
