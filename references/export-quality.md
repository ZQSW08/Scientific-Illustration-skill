# 投稿导出与技术质量

## 1. 首选矢量

适合：
- line plot
- bar
- flowchart
- schematic
- vector field

优先 PDF/SVG/EPS（以目标期刊接受格式为准）。

## 2. 位图

适合：
- photograph
- video frame
- microscopy / texture
- rendered full-field raster

在最终版面尺寸下检查清晰度。

## 3. 常见出版要求思路

不同出版商要求可能变化，投稿前以目标期刊最新 Guide for Authors 为准。通常应特别检查：
- line art 需要比照片更高分辨率；
- combination artwork 介于 line art 和 photo；
- 字体嵌入；
- 不使用极细线；
- figure 不应依赖屏幕放大才能读懂。

## 4. 单栏/双栏

设计时就按最终宽度预览：
- 单栏 figure 不要塞 8 个 panel；
- 双栏 figure 可承载复杂 pipeline 或 4–6 个 small multiples。

## 5. 轴和单位

必须检查：
- px vs mm
- frame vs s
- normalized amplitude 是否在 caption 说明
- Hz 上限与 sampling rate 是否一致

## 6. Caption 自包含

caption 应包含：
- 图在比较什么
- panel 对应什么
- 关键颜色/线型
- 缩写
- normalization / errorbar 定义（若必要）

不要在 caption 重新解释方法全部理论。

## 7. 最终 QA

导出后以 100% 和最终论文尺寸查看：
- 字是否糊
- marker 是否还能区分
- 黑白是否可读
- 主次是否明确
- transparent object 是否丢失
- raster 图片是否被过度压缩
