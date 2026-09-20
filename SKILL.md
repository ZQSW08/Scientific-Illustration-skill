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
>
> **原始数据与变换代码是证据源；可编辑图文件是呈现源，二者不能混淆。**

每一张主图都应该对应论文中的一个 claim。最终交付不能只剩 PNG/JPG；除非用户明确只要位图，否则必须同时保留可编辑源文件、原始数据和可重复生成脚本。

---

## Editable-first：默认交付契约

科研制图默认采用“可编辑源 → 矢量导出 → 位图预览”三级交付，而不是只输出截图。

### A. 数据驱动图（曲线、频谱、误差、3D surface/waterfall、柱状图、多面板）

优先沿用用户指定或工程已有的可复现工具。MATLAB工程可直接交付 `.m + .fig + MAT/CSV + PNG`，按需另导出矢量PDF/SVG；`.fig`保存为可直接打开的Visible=on。Python工程同样可用脚本、数据及矢量输出。不要仅因安装了Origin就强制迁移。

当用户需要Origin编辑或现有图已基于Origin时，可使用：

```text
raw / processed data
→ CSV / XLSX
→ Origin workbook + graph
→ .opju
→ SVG / EMF / PDF
→ PNG preview
```

必须尽量保留：
- worksheet 数据；
- graph layer；
- axis / legend / label；
- zoom / inset；
- plot group；
- 可重复执行的 Python/LabTalk 脚本。

Origin 的 `.opju` 是该工作流的可编辑呈现源，不能替代原始数据与生成记录；MATLAB `.fig`亦然。

### B. 方法总览图、流程图、实验示意图、带大量箭头/框/局部图像的组合图

当用户选择Visio或已有Visio工程时，可生成：

```text
.vsdx + assets/ + SVG/PDF/PNG export
```

要求：
- Stage 容器可编辑；
- 文本可编辑；
- 箭头与 connector 可编辑；
- ROI 框、callout、panel label 可编辑；
- 每个 imported plot/image 独立放置，不把整页 flatten 成一张图。

Visio 的 `.vsdx` 是该工作流的可编辑呈现源；原生SVG、draw.io或其他已有可编辑布局同样可用。

### C. 混合型 Figure

对于“方法框图 + 数据图 + 原始视频帧 + 公式/箭头”的高信息密度图，按项目选择可编辑组合方式，例如：

```text
Origin：负责数据图
Visio：负责总版式和连接关系
```

Origin 图以 SVG/EMF/PDF 等矢量形式导出后放入 Visio；需要修改数值曲线时回到 `.opju` 修改，再重新导出并替换。不要把 Origin 曲线截图后当作最终源。

### D. 软件不可用时

不要伪造 `.opju` 或 `.vsdx`。

回退顺序：
1. SVG + CSV + 生成脚本；
2. draw.io / editable SVG；
3. PPTX（适合组合图与少量流程图）；
4. PNG 仅作为 preview。

如果用户要求“本地可编辑”，必须明确告诉用户当前交付的 source-of-truth 格式。

详细规则见 `references/editable-local-workflow.md`。

---

## 本地软件调用规则

当本 Skill 在用户 Windows 本机、Codex 或其他具有桌面软件访问能力的 agent 中运行时：

### Origin

仅当采用Origin工作流时检查Python是否可导入 `originpro`，再核对可用API。不要为了普通MATLAB/Python结果图启动其他软件、猜安装路径或擅自安装依赖。

### Visio

仅当采用Visio工作流时检查COM automation是否可用。使用时创建原生shape、text、connector并保存 `.vsdx`，不要把整张位图塞入文件冒充可编辑。

### 软件职责不能混淆

- Origin：**数据图**
- Visio：**结构图 / 方法图 / 总版式**
- MATLAB/Python：**数据计算、可复现数据图与自动化生成**
- SVG/PDF：**交换格式**
- PNG/TIFF：**投稿预览或位图要求**

---

## 用户参考图所体现的目标风格

当用户给出类似高水平期刊参考图时，优先学习其“组织方式”，不要逐像素复制。

本轮参考图显示出的目标风格包括：

1. **高信息密度，但有明确层级。** 方法总览图可包含真实场景、算法中间图、波形和箭头，但必须用 Stage 容器、灰色标题带、虚线边界或留白分区。
2. **真实数据作为方法节点。** 流程图中的节点不只用图标；可以嵌入真实 frame、response map、phase/amplitude map、confidence surface。
3. **中间过程必须可见。** 例如 raw signal → local statistic → threshold plane → anomaly zone → repaired signal。
4. **局部放大用于证明精度。** 多层 zoom-in 通过 ROI 框和 connector 连接，放大的是“差异发生的位置”，而不是装饰。
5. **3D 可以使用，但必须有信息意义。** 3D line/waterfall 用于把不同方法分层，3D surface/plane 用于展示 confidence、threshold、anomaly region；禁止纯装饰性 3D 柱图和透视。
6. **颜色承担流程语义。** 例如 training / tracking / proposed step 使用固定的箭头颜色；同一方法在全文保持同色。
7. **主结果 + 汇总指标共同出现。** 上半部分展示逐点误差或时域曲线，下半部分用 MAE/RMSE 等 summary panel 收束。
8. **Serif 论文排版感。** 图内文本优先统一为 Times New Roman / Cambria 一类期刊兼容字体；panel label 使用粗体 `(a)`、`(b)`；避免 UI 风格圆角卡片泛滥。

详细拆解见 `references/reference-style-deconstruction.md`。

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

- 图中文字遵循用户语言和目标用途；中文工程诊断可用中文，正式英文投稿图再采用对应语言。没有指定期刊时，不把个人风格当作投稿要求。
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
- 只有存在独立真值时才标出真值频率，并注明来源；否则标“检测峰”或“候选”，不根据期望答案给峰贴正确/错误标签
- 不要只截图 FFT
- 若比较多方法，统一频率范围和归一化方式
- 对噪声底、harmonic、spurious peak 应有视觉区分

滤波测量图同时保留绝对幅值信息；各自峰值归一化要明确标注，不能用来证明幅值保真。区分原始观测、实际时域滤波、拟合/重建与被滤除部分；被滤除部分不自动等于大运动真值。无效和拒识画缺口/状态而非全零，不拼接不连续样本生成频谱。速度图同时披露处理帧数、有效覆盖和输出任务，不能把跟踪早退画成有效加速。

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
- 用户参考图风格拆解：`references/reference-style-deconstruction.md`
- Origin / Visio / SVG 的可编辑本地工作流：`references/editable-local-workflow.md`
- Origin 自动化细则：`references/origin-workflow.md`
- Visio 自动化细则：`references/visio-workflow.md`
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
- [ ] 除非用户明确只要图片，否则已保留可编辑 source-of-truth。
- [ ] 数据图保留原始/处理后数据；组合图没有被整页 flatten。
- [ ] 沿用用户选择的可复现工具，已明确数据源、生成脚本和可编辑呈现文件；不因安装了其他软件而强制迁移。

