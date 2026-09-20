# Visio 科研方法图与组合图工作流

## 1. 适用图型

优先用于：
- 方法总览图；
- multi-stage pipeline；
- tracking feedback loop；
- 实验装置示意；
- stage + real frame + intermediate map；
- Origin 图和图片的最终组合版式。

## 2. 为什么不用“一张生成图片”

高水平方法图经常需要后期反复修改：
- stage 名；
- 公式；
- 箭头方向；
- panel 次序；
- ROI；
- 中间图；
- 颜色语义。

因此每个结构元素都必须可独立编辑。

## 3. Visio 自动化

Windows + Visio 环境下优先 COM automation。

典型检查：
```python
try:
    import win32com.client
    app = win32com.client.Dispatch("Visio.Application")
    VISIO_AVAILABLE = True
except Exception:
    VISIO_AVAILABLE = False
```

若不可用：
- 不自动安装 Office/Visio；
- 输出 editable SVG / draw.io / PPTX fallback；
- 明确说明没有生成原生 `.vsdx`。

## 4. 原生元素规则

以下必须尽量使用 Visio 原生 shape：
- stage container；
- rectangle；
- text；
- arrows/connectors；
- ROI box；
- callout；
- panel label。

以下可以作为独立图像 asset：
- raw frame；
- phase map；
- amplitude map；
- response map；
- confidence surface screenshot；
- 复杂 Origin chart。

## 5. 方法图的分层

参考 DA-ViReS 类大总览图：

### Level 0: Page
整张 Fig.1。

### Level 1: Stage
`Step 1 / Step 2 / Step 3`

### Level 2: Module
`Direction awareness`
`Phase amplification`
`Anomaly detection`
`Signal repair`

### Level 3: Evidence object
真实视频、waveform、mask、spectrum。

Visio 中每一级都应该可以 group/ungroup。

## 6. Feedback loop

参考 hybrid KCF/L-D-C 类图：
- training arrow；
- tracking arrow；
- proposed correction arrow；
- threshold gate；
- feedback to template update。

不同逻辑角色允许使用不同箭头色，但全篇固定，不要每张图重新定义。

## 7. Page grid

建议：
- 双栏宽度优先；
- 先划 12-column 或 4-column grid；
- stage 之间至少保留统一 gap；
- 所有模块边缘对齐；
- connector 尽量水平/垂直；
- 避免斜箭头大面积交叉。

## 8. Figure 内嵌真实图

嵌入前先裁掉无关空白。

如果是 video frame：
- 保持 aspect ratio；
- ROI 框用 Visio shape，不要烙进图片；
- target label 用 Visio text。

如果是 plot：
- 优先 SVG/EMF；
- 保留独立 Origin source；
- 不从 Word 截屏。

## 9. 公式

优先顺序：
1. Office equation / MathType；
2. SVG equation；
3. 高分辨率透明 PNG（最后选择）。

不要让公式字体与全文严重不一致。

## 10. 导出

交付：
- `.vsdx`
- PDF
- SVG（若导出链稳定）
- PNG preview
- assets 文件夹。

## 11. 禁止

- 把整个 Fig.1 先用 image generator 生成，再放 Visio；
- 文本烙死在 bitmap；
- 箭头烙死在 bitmap；
- 不同 stage 的边框、线宽、字体完全不统一；
- 为了“科技感”使用大量发光、渐变和 3D 卡片。
