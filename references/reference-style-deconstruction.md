# 用户参考图风格拆解与可迁移模板

本文件基于用户给出的高水平期刊参考图，只提取设计语言与证据组织，不复制具体论文图。

## 模式 A：3D pointwise error + summary bars

参考特征：
- (a)–(d)：不同 motion magnitude；
- X：point index；
- Y：method；
- Z：absolute error；
- (e)：MAE；
- (f)：RMSE。

优点：
- 既看到逐点误差的结构，又看到汇总指标；
- proposed 接近 0 时非常直观；
- 可以暴露某方法在特定 motion magnitude 下的剧烈波动。

适用：
- tracking accuracy；
- 多测点 displacement error；
- 多工况 point-wise reliability。

不适用：
- 方法超过 5 个；
- point 数太少；
- 3D 透视遮挡严重。

可编辑实现：Origin。

---

## 模式 B：大方法总览图 + stage 分区

参考特征：
- 顶部是真实应用场景；
- 中部是核心增强方法；
- 底部是异常检测/修复；
- 每一 stage 有浅灰标题带；
- 内部用蓝色细边框再分 module；
- 真实 frame、phase/amplitude、waveform、FFT 都嵌在图中。

关键：
这不是传统“方框流程图”，而是**evidence-rich overview**。

适用：
- 一篇文章有 2–4 个互补模块；
- 每个模块有可视化中间表示；
- 需要 Fig.1 就让 reviewer 明白“输入→机制→输出”。

可编辑实现：Visio 总版式 + Origin 子图。

---

## 模式 C：filter / confidence mechanism schematic

参考特征：
- 左边显示不同方向 filter kernel；
- 中间 previous/current frame；
- 右边显示每个方向对应的 confidence surface；
- 用箭头建立“filter → image → confidence”的直接映射。

优点：
- 抽象公式被视觉化；
- orientation 的作用一眼可见；
- confidence 不是一个黑盒 scalar。

适用：
- Gabor orientation；
- CSP scale/orientation；
- reliability map；
- PNL sensitivity；
- filter bank。

可编辑实现：Visio + Origin 3D surface。

---

## 模式 D：大范围曲线 + correction comparison + zoom

参考特征：
- 左列展示“before correction / homography / proposed / reference”的全局时域；
- 右列只显示 reference vs proposed 的局部；
- 多测点采用 vertically stacked small multiples。

这比把所有测点堆一张图好。

适用：
- camera motion correction；
- dynamic ROI；
- multi-point displacement；
- 低频 drift + 高频 vibration 混合。

可编辑实现：Origin。

---

## 模式 E：三级 zoom 精度验证

参考特征：
- 左：完整 10 s；
- 中：局部 2 s；
- 右：极局部若干采样点；
- 绿色 ROI 框/connector 指示 zoom 来源；
- 每个 condition 一行。

强项：
- 同时证明 waveform 一致和 subpixel-level 差异。

适用：
- 与传感器对比；
- displacement accuracy；
- phase vs DIC/ICGN；
- amplitude preservation。

可编辑实现：Origin；connector 也可在 Visio 最终拼版。

---

## 模式 F：tracking feedback framework

参考特征：
- reference/current frame 在最上方；
- training 和 tracking 两种箭头；
- HOG/response map/template update；
- threshold gate 决定 correction 或 detection；
- correction 输出反向更新 tracker。

强项：
- 不是单向 pipeline，而是**conditional feedback system**。

适用：
- confidence-aware tracker；
- redetection；
- template update；
- coarse/fine correction。

可编辑实现：Visio。

---

## 模式 G：3D signal anomaly detection / repair

参考特征：
- 原始 signal 在前景平面；
- local statistic 或 repaired reference 抬高到另一个 plane；
- threshold 形成半透明平面；
- anomaly zone 用半透明 box；
- 虚线连接对应位置。

强项：
- 时间、统计量、阈值、异常窗口同时出现，逻辑非常浓缩。

风险：
- 容易遮挡；
- 期刊缩小后文字难读；
- 需要同步提供简单 2D 版本用于检查。

可编辑实现：Origin 3D + Visio 注释。

---

## 共同视觉基因

这些参考图并不追求极简“Nature 风”，而是偏工程期刊：

- 高信息密度；
- 黑/灰轴线；
- Serif 字体；
- panel label 明确；
- 彩色但饱和度适中；
- 图内公式少量出现；
- zoom connector 很常见；
- 中间结果真实；
- 颜色用于区分方法或算法角色；
- 留白用于分层，而不是大面积装饰。

因此 Skill 的目标不应是“统一把所有图做成现代扁平设计”，而应支持两种风格：

1. **Engineering journal dense style**：适合 MSSP/Measurement/AEI；
2. **Minimal analytical style**：适合简单机制/单一比较。

默认根据参考论文和图的证据密度选择。
