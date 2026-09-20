# Scientific-Illustration-skill

面向工程、计算机视觉、结构动力学、信号处理与视觉测量论文的科研制图 Skill。

它不是“美化图片教程”，而是把高水平论文中的图形逻辑提炼为可复用规范：**一图一问题、图证据与论文 claim 对齐、颜色承担语义、方法总览图建立层级、中间过程图证明机制、结果图建立公平对比。**

## 核心能力

- 方法总览图 / pipeline
- 机制图 / 原理图
- 中间过程与 failure→repair 图
- 时域、频域、误差、敏感性和鲁棒性图
- 实验装置与场景图
- 光流、位移场、模态振型等 full-field 图
- 多面板 figure 编排
- 颜色、线型、字体与投稿导出审查

## 目录

- `SKILL.md`：主技能
- `references/method-overview.md`
- `references/intermediate-evidence.md`
- `references/result-comparison.md`
- `references/visual-language.md`
- `references/corpus-figure-patterns.md`
- `references/export-quality.md`
- `assets/figure-evidence-map.md`
- `assets/method-overview-wireframe.md`
- `assets/figure-review-checklist.md`

## 核心原则

> Figure = compressed argument.

不要把论文所有结果都塞进一张图。每张主图应对应一个清晰问题和一个可验证结论。


## Editable-first v2

本 Skill 现在默认要求保留可编辑源文件，而不只输出图片。

推荐职责：
- Origin / OriginPro：时域、频域、误差、3D waterfall/surface、柱状、heatmap、多面板 zoom 图。
- Visio：方法总览图、流程图、实验示意、feedback system、最终组合版式。
- MATLAB / Python：数据计算、批处理、自动化。
- SVG / PDF：软件之间的矢量交换。
- PNG / TIFF：预览或投稿位图，不作为唯一源文件。

新增文档：
- `references/editable-local-workflow.md`
- `references/origin-workflow.md`
- `references/visio-workflow.md`
- `references/reference-style-deconstruction.md`
- `assets/editable-figure-deliverables.md`

尤其适配：
- 3D point-wise error + MAE/RMSE 汇总
- 大方法总览图 + 真实中间结果
- Gabor/filter/confidence mechanism schematic
- 多测点 correction time histories
- 三级 zoom 精度验证
- tracking feedback framework
- 3D anomaly detection / repair
