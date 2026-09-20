# Editable-first 本地科研制图工作流

## 1. 总原则

默认交付不是“图片文件”，而是一个可维护的 figure package：

```text
figure_x/
├── data/
│   ├── raw.csv
│   └── processed.csv
├── source/
│   ├── figure.opju      # 数据图时
│   ├── figure.vsdx      # 结构/组合图时
│   └── generate_*.py
├── assets/
│   ├── frame_001.png
│   ├── phase_map.png
│   └── ...
├── export/
│   ├── figure.svg
│   ├── figure.pdf
│   └── figure.png
└── README.md
```

原始数据与变换代码是证据源；可编辑图文件是呈现源；PNG通常是预览。以下Origin/Visio流程仅在用户选择该工具时采用，不替代已有MATLAB/Python工程。

## 2. 图型 → 工具选择矩阵

| 图型 | 首选工具 | 可编辑主文件 | 备注 |
|---|---|---|---|
| 已有MATLAB数据图 | MATLAB | .m + .fig | 保留MAT/CSV，FIG保存Visible=on，PNG预览；按需矢量导出 |
| 已有Python数据图 | 现有绘图库 | 脚本 + 数据 + SVG/PDF | 不为“可编辑”额外引入商业软件 |
| 时域/频域/误差曲线 | Origin | .opju | 数据和样式同时保留 |
| 3D waterfall / surface | Origin | .opju | 适合论文中的分层曲线/阈值面 |
| 柱状/箱线/heatmap | Origin | .opju | 可在本地直接调轴、字体、legend |
| 方法总览图 | Visio | .vsdx | 原生 shape/connectors |
| 算法流程图 | Visio | .vsdx | connector 与 stage 容器可编辑 |
| 实验装置示意 | Visio | .vsdx | 照片 + 原生标注 |
| “真实图像+曲线+流程箭头”混合图 | Origin + Visio | .opju + .vsdx | Visio 负责最后拼版 |
| 无 Origin/Visio | SVG + CSV + Python | .svg + .py | 明确为 fallback |

## 3. 选择Origin后的数据图流程

1. 保留MATLAB/Python原始与处理数据，导出带单位说明的CSV；不为呈现另行平滑、筛选或修改数值。
2. 使用 Origin Python API 将数据写入 workbook。
3. 建 graph/layer/plot。
4. 完成 axis、legend、panel、inset。
5. 保存 `.opju`。
6. 导出 SVG/PDF/PNG。
7. README 记录数据列、单位、绘图脚本和 Origin 版本。

## 4. 选择Visio后的方法图流程

1. 先定义 page grid、stage bounding boxes。
2. 将 stage、文本、箭头、ROI 框做成原生 Visio shape。
3. 真实视频帧/phase map 等作为独立 asset 嵌入。
4. Origin 图以矢量导出后嵌入。
5. 所有 panel label 独立为文本 shape。
6. 保存 `.vsdx`，导出 PDF/SVG/PNG。
7. 禁止把整个页面先渲染成 PNG，再放进 Visio。

## 5. 混合图的“所有权”

若一张图包含：
- 曲线；
- 图像；
- 箭头；
- 公式；
- stage 容器；

则按实际工具记录：
- 曲线的可编辑呈现源属于选定绘图工具（如MATLAB、Python或Origin）；
- 版式呈现源属于选定布局工具（如SVG、draw.io或Visio）；
- 原始 frame/mask/map 属于 assets；
- 公式建议保留 MathType/Office equation 或 SVG；
- 最终 `.vsdx` 仅作为拼版，不应成为数据图的唯一源。

## 6. 修改回路

### 改数值/曲线
回原数据/生成脚本核对变换 → 在选定绘图工具重新导出 → 更新布局中的对象。不得在图形编辑器中手改实验数值以取得吻合。

### 改箭头/布局/文字
直接在 Visio 修改。

### 改算法中间图
从 MATLAB/Python 重新导出同名 asset；尽量保持同尺寸，减少版式重排。

## 7. 可重复性

每张关键 figure 的 README 至少记录：
- source data；
- processing script；
- normalization；
- units；
- software；
- main editable file；
- export size；
- font；
- color roles；
- figure claim。

## 8. 不可接受的交付

- 只有 PNG；
- “可编辑 PPT”但所有内容其实是一张背景图；
- `.vsdx` 内只有一张全页截图；
- Origin 图没有 worksheet 数据；
- 图中数字来自手工输入却无来源；
- 修改脚本后无法重现原图。

