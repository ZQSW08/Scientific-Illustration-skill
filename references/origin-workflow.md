# Origin / OriginPro 科研绘图工作流

## 1. 适用图型

优先用于：
- 多方法时域曲线；
- FFT / PSD；
- MAE/RMSE 柱状；
- error vs motion magnitude；
- 3D waterfall；
- 3D threshold/confidence plane；
- heatmap；
- multi-panel zoom-in comparison。

## 2. 自动化策略

在 Windows + Origin 环境中，优先使用 Origin 官方 Python 包 `originpro`。

执行前：
```python
try:
    import originpro as op
    ORIGIN_AVAILABLE = True
except Exception:
    ORIGIN_AVAILABLE = False
```

不要自动 pip install，除非用户明确允许。

外部 Python 场景下，通常由 `originpro` 通过 COM 与本地 Origin 通信。脚本结束前必须显式保存 project；调试时不要因为 Python 退出导致未保存的 Origin project 消失。

## 3. 推荐 source package

```text
source/
├── build_figure.py
├── style.json
└── figure.opju
data/
├── raw.csv
└── summary.csv
```

`build_figure.py` 负责从数据重建图；`.opju` 允许用户手工微调。

## 4. 参考图 1：不同方法误差的 3D 分层线图

不要把它理解成“炫技 3D”。它实际编码：
- X = point index
- Y = method category
- Z = absolute error

适合：
- 点位很多；
- 方法较少；
- 想同时看误差随点位的波动和方法间整体差异。

建议同时配：
- MAE bar；
- RMSE bar。

这样“逐点行为 + 汇总指标”形成闭环。

Origin 中应保留：
- 每个方法一列或一组数据；
- category Y 位置；
- 相同 X；
- Z axis 统一；
- 主方法线条不必最粗，但必须全篇同色。

## 5. 参考图 2：多级 zoom 时域曲线

三列布局：
```text
whole signal → local window → sub-pixel detail
```

适合证明：
- 大尺度趋势一致；
- 局部振幅/相位一致；
- 极小误差区域仍可见差异。

要求：
- zoom ROI 由矩形框指出；
- connector 颜色低饱和；
- 三列单位一致；
- 最右 panel 不得偷偷改变 normalization。

## 6. 参考图 3：3D anomaly detection / repair

3D 的第三维并不是装饰，而是把不同信号层分开：
- 原始 signal；
- local std；
- threshold plane；
- anomaly window。

如果 2D 更清楚，则不要坚持 3D。

推荐同时输出一个 2D reviewer-friendly 版本，防止 3D 透视遮挡。

## 7. Origin style preset

建议维护一个 `style.json`，至少包含：
- font_family
- font_size_axis
- font_size_legend
- line_width_reference
- line_width_proposed
- marker_size
- panel_label_size
- role colors
- single_column_width_mm
- double_column_width_mm

不要把这些值散落在几十行脚本中。

## 8. Origin 项目中必须可编辑的对象

- axes；
- tick；
- legend；
- plot；
- error bars；
- inset layer；
- panel labels；
- annotations；
- ROI rectangle；
- connectors（若使用）。

## 9. 导出

至少：
- SVG 或 PDF；
- 600 dpi PNG 预览（按期刊需求调整）；
- `.opju`。

不要只导 JPG。

## 10. 数据完整性

任何 smoothing/interpolation：
- 必须在数据层留下新列；
- 原始列不能覆盖；
- 图例/README 说明处理；
- 不得为了视觉平滑而悄悄改变结果。
