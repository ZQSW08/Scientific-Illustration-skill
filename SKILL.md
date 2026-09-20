---
name: scientific-illustration-skill
description: 面向工程、计算机视觉、结构动力学、信号处理与视觉测量论文的科研制图技能。用于规划和审查方法总览图、机制示意图、中间过程验证图、算法流程图、实验装置图、时频曲线、误差对比、消融图、鲁棒性图、模态/位移场图以及多面板期刊图。重点学习 MSSP、Measurement、JSV、AEI 等高水平论文的“图像叙事”：一图一问题、颜色语义一致、从输入到输出的层级清晰、图与 claim-evidence 对齐。不得伪造实验图、数据、误差条或不存在的中间结果。
---

# Scientific Illustration Skill

## 目标

科研图不是“把结果画漂亮”，而是让审稿人用 5–15 秒看懂：

1. 问题在哪里；
2. 方法如何解决；
3. 关键中间变量是否按预期变化；
4. 最终结果是否优于 baseline；
5. 方法在哪些条件下失效。

核心原则：

> **Figure = compressed argument。**

每一张主图都应该对应论文中的一个 claim。

---

## 制图前先建立 Figure Evidence Map

使用 `assets/figure-evidence-map.md`。

对每张图先写：

```text
Question:
Claim:
Evidence:
Visual encoding:
Expected reader takeaway:
```

如果无法写出“Question”，不要先画图。

---

## 图的四个层级

### Level A — Method overview
回答“方法总体怎么走”。

### Level B — Mechanism / intermediate evidence
回答“为什么某个模块真的有效”。

### Level C — Quantitative comparison
回答“比谁好、好多少、在哪些条件下好”。

### Level D — Field / physical interpretation
回答“真实场景中结果是否仍具物理意义”。

高水平论文通常不是只有 Level C。

---

## 方法总览图：默认结构

优先使用左→右的数据流：

```text
Input
→ Challenge / disturbance
→ Stage 1
→ Intermediate representation
→ Stage 2
→ Reliability / correction
→ Output
```

当方法是多阶段时，每个 stage 用一个大容器，而不是把每个函数都画成独立小框。

每个容器只保留：
- stage 名
- 1 个代表性视觉对象
- 1–2 个关键操作
- 明确输出

详细规范见 `references/method-overview.md`。

---

## 中间过程验证图

不要只画“raw vs final”。

优先展示：

```text
raw failure
→ diagnostic map
→ module action
→ corrected intermediate
→ final physical signal
```

例如：
- phase wrap → coarse compensation → residual phase
- raw optical flow → confidence map → abnormal mask → refined flow
- gust-contaminated waveform → anomaly score → repaired waveform
- tracking result → local detection → correction → stable trajectory

详细规范见 `references/intermediate-evidence.md`。

---

## 定量对比图

### 方法数量 ≤ 4
优先 line / grouped bar / errorbar。

### 工况 × 方法较多
优先 heatmap、small multiples、matrix table + highlight。

### 需要展示稳定性
不要只画 mean：
- error distribution
- box/violin
- P95
- failure rate
- worst case
- repeated-trial polar/radar 仅在维度本身有周期/方向意义时使用

### Sweep
横轴必须是“困难程度或可解释参数”，例如：
- displacement amplitude
- interference RMS
- SNR
- illumination
- frequency overlap
- prior bandwidth

这样图本身会讲“robustness curve”。

---

## 颜色系统

颜色必须承担语义，不能只为好看。

推荐建立固定角色：

- **Proposed method**：全篇唯一主色
- **Reference / ground truth**：黑或深灰
- **Strong baseline**：次级强调色
- **Other baselines**：低饱和灰/蓝灰
- **Invalid / disturbance / outlier**：警示色
- **Confidence / reliability**：连续色图

同一个方法在全文所有图中保持相同颜色。

禁止：
- 同一方法在不同图换颜色
- 彩虹色图用于连续误差
- 红/绿作为唯一类别区分
- 过度渐变、阴影、3D bar

更多见 `references/visual-language.md`。

---

## 多面板图的叙事

面板顺序优先按读者推理顺序，而不是代码输出顺序：

```text
(a) scene/input
(b) failure / raw result
(c) proposed intermediate
(d) comparison
(e) quantitative summary
```

局部放大图：
- 必须有明确 ROI box / connector
- zoom 区域要证明某个差异，不要随机放大
- 主图与 inset 的坐标/颜色语义一致

---

## 方法图视觉层级

使用三层视觉权重：

### 一级：Stage
大标题、浅底色容器、足够留白。

### 二级：Operation
简洁标签 + 图标/示意。

### 三级：Variable
只标最关键符号，例如：
`d_int`、`d_sub`、confidence、mask。

不要把公式全部放进总览图。

---

## 图中文字

- 图中尽量用英文，保持投稿通用性。
- 标签使用名词短语：`Coarse localization`、`Residual phase`。
- 避免整句说明。
- 公式只保留最核心的 1–2 个。
- 图注负责解释，不让图内塞满文字。

---

## 曲线图

必须明确：
- unit
- sampling/time base
- normalization 是否存在
- filtered / raw 的处理差异
- peak 标注规则

频谱图：
- 标出 target/reference frequency
- 不要只截图 FFT
- 若比较多方法，统一频率范围和归一化方式
- 对噪声底、harmonic、spurious peak 应有视觉区分

时域图：
- 若差异只在局部，主图 + zoom inset
- 不要用线宽/透明度让 baseline 消失

---

## 位移场、光流、模态与全场图

优先：
- 几何形态 + 连续场颜色
- 统一 colorbar
- 相同工况必须固定 color limits
- 如果比较 shape，避免每个 panel 自己 autoscale 导致“看起来都一样好”
- 矢量场过密时采样显示，不遮住底图
- mode shape 比较应统一符号/相位方向或说明 sign ambiguity

---

## 期刊导出

优先矢量：
- PDF / SVG / EPS（期刊允许时）

位图：
- line art 需要高分辨率
- combination art 次之
- photograph/halftone 至少保证最终版尺寸下清晰

最终检查：
- 单栏缩放后文字仍可读
- 线宽不会消失
- 黑白打印仍能区分
- 色盲模式不丢关键信息

见 `references/export-quality.md`。

---

## 按任务加载参考文件

- 方法总览 / 流程图：`references/method-overview.md`
- 中间过程、消融、机制证据：`references/intermediate-evidence.md`
- 结果对比、曲线、表格、场图：`references/result-comparison.md`
- 配色、字体、线型、布局：`references/visual-language.md`
- 从高水平视觉测振论文蒸馏图形模式：`references/corpus-figure-patterns.md`
- 导出投稿：`references/export-quality.md`
- 新建图前：`assets/figure-evidence-map.md`
- 总览图草图：`assets/method-overview-wireframe.md`
- 投稿前审查：`assets/figure-review-checklist.md`

---

## 强制检查

- [ ] 一图只回答一个主问题。
- [ ] proposed/reference/baseline 颜色全篇一致。
- [ ] 没有用视觉效果夸大微小差异。
- [ ] 所有对比使用相同坐标范围或明确说明不同。
- [ ] error bar / confidence interval 有定义。
- [ ] 图中单位完整。
- [ ] 图注能独立读懂。
- [ ] raw → intermediate → final 的证据链可追踪。
- [ ] 方法图没有代码级细节污染。
- [ ] 没有伪造、插值成“更好看”或隐藏失败样本。
