# 实验结果与对比图

## 1. 一张结果图先定义问题

示例：
- Accuracy 是否随 displacement amplitude 退化？
- Camera disturbance 加强后谁先失效？
- Reliability mask 是否真的减少 outliers？
- 模态高阶成分是否被恢复？

## 2. 曲线图

### Time history
- reference：黑/深灰
- proposed：主色
- baseline：次级色
- raw/no correction：低饱和色

如果序列长：
- 主图看整体
- inset 看局部
- 不要把 6 个点位全部堆在一个坐标轴上；可用 small multiples

### Spectrum
统一：
- frequency range
- normalization
- peak detection
- y-axis scale

推荐：
- reference peak 虚线
- detected peak marker
- false peak 用淡色/特殊 marker

以上“reference/false”标签必须有独立依据；没有真值时只标检测峰。各自峰值归一化要同时保留绝对谱，并在图注声明只能比较谱形。观测缺失/拒识不等于零；滤波的有效连续区间、窗函数、单位和归一化分母应可查。

速度与版本对比应显示相同输入和任务边界，拆分冷启动、读帧、跟踪、选带及导出。关闭对照臂、少读帧或跟踪提前失败应明确标注；若精度/覆盖降低，不能单凭时间柱宣称改进。

## 3. Error vs difficulty

这是最有信息量的鲁棒性图之一。

横轴：
- noise level
- displacement
- interference RMS
- SNR
- illumination
- occlusion ratio
- frequency prior width

纵轴：
- RMSE / MAE / MAPE / failure rate

读者一眼可看出：
- 方法在哪个区间有优势
- 什么时候性能开始崩

## 4. Bar chart

只适合类别少、结果离散。

必须：
- 从零起点是否合理
- 显示数值或 errorbar
- 不使用 3D
- 不用过宽 bar
- group 间有留白

## 5. Box / violin

用于：
- repeated trials
- 50 次鲁棒性测试
- 多测点 error distribution

优先比只报 mean 更可信。

## 6. Heatmap

适合：
- FL × FH
- parameter A × B
- operating condition × method
- point × mode MAC

必须有：
- colorbar
- bad/good 方向说明
- invalid region mask
- 统一 color range

## 7. 模态图

比较 mode shape：
- 固定横坐标测点
- mode 可独立归一化，但比较双方使用同一 normalization
- sign ambiguity 要对齐
- 多阶模态使用 small multiples
- 给 MAC 在 panel subtitle 或 table

## 8. Full-field / optical flow

- 比较图必须统一 color limits
- outlier mask 可单独 panel
- vector density 适当下采样
- 保留结构轮廓
- 不让 colormap 掩盖实际 geometry

## 9. 表格与图如何分工

图：展示趋势、分布、机制。
表：展示精确数字。

不要让表和图逐项完全重复。

