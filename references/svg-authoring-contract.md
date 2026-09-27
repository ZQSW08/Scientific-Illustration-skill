# Editable SVG Authoring Contract

## 1. 目标

本 Skill 生成的 SVG 必须同时满足两件事：

1. **跨软件可打开**：Inkscape、Figma、Illustrator、浏览器、Microsoft 365 等常见工具可以正常显示；
2. **人类可继续编辑**：文字仍是文字，模块仍是模块，箭头仍是箭头，图层/分组有语义，而不是一个巨大 path 或一张嵌入式 PNG。

因此，默认生成的 SVG 不是“渲染终点”，而是**可维护源文件**。

---

## 2. 两种 SVG 交付档位

### Portable Editable SVG

默认首选。

文件名：
`figure_editable.svg`

特点：
- 纯标准 SVG；
- 尽量使用 `<rect>`、`<line>`、`<polyline>`、`<path>`、`<text>`、`<g>`；
- 无 `foreignObject`；
- 不依赖某一软件私有标签；
- 文本不转路径；
- 结构化 group/id；
- 箭头使用 `<marker>`；
- 重复对象使用 `<defs>` / `<symbol>` / `<use>`；
- 可被 Inkscape、Figma、Illustrator 等继续编辑。

### Tool-native Editable Source

当用户明确使用某软件时，同时保留：
- Inkscape: `.svg`（可含 layer metadata）；
- Illustrator: `.ai` + clean SVG；
- Visio: `.vsdx` + SVG export；
- Origin: `.opju` + SVG export。

不要让“带软件私有信息的 SVG”成为唯一副本。

---

## 3. 强制结构规则

### 3.1 必须有 viewBox

例如：

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     width="180mm"
     height="100mm"
     viewBox="0 0 1800 1000">
```

`viewBox` 负责内部坐标；width/height 表达目标版面。

### 3.2 必须语义分组

示例：

```xml
<g id="background" data-name="Background">...</g>
<g id="stage_1" data-name="Stage 1 - Acquisition">...</g>
<g id="stage_2" data-name="Stage 2 - Tracking">...</g>
<g id="stage_3" data-name="Stage 3 - Measurement">...</g>
<g id="connectors" data-name="Connectors">...</g>
<g id="annotations" data-name="Annotations">...</g>
```

不要：

```xml
<path d="M ... 8000 个节点 ..." />
```

把整张图 flatten 成单一路径。

### 3.3 文本必须保持为文本

优先：

```xml
<text id="title_stage_1"
      x="100" y="80"
      font-family="Times New Roman, Times, serif"
      font-size="34">
  Video acquisition
</text>
```

不要把标题、坐标轴、legend、panel label 默认转成 path。

原因：
- 人工无法直接改字；
- 文件显著膨胀；
- 搜索/替换失效；
- Figma/Illustrator/Inkscape 中文字修改困难。

如果因投稿/字体嵌入最终必须 outline，应额外导出 `figure_submission.svg/pdf`，而不是覆盖 editable source。

### 3.4 每个重要对象有 id

推荐：
- `panel_a`
- `axis_time`
- `curve_proposed`
- `curve_reference`
- `roi_zoom_1`
- `arrow_stage1_stage2`
- `label_confidence`

不要使用：
- `path123456`
- `g987`
作为主要人工维护标识。

### 3.5 箭头使用 marker

推荐：

```xml
<defs>
  <marker id="arrow_main"
          viewBox="0 0 10 10"
          refX="9" refY="5"
          markerWidth="7" markerHeight="7"
          orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke"/>
  </marker>
</defs>

<path d="M 100 200 H 350"
      fill="none"
      stroke="#333"
      stroke-width="3"
      marker-end="url(#arrow_main)"/>
```

这样箭头与连线仍是独立对象。

### 3.6 重复元件放入 defs/symbol

如：
- camera icon；
- tracking point；
- stage badge；
- repeated marker。

避免复制一堆不可维护路径。

---

## 4. 样式规则

### 4.1 跨编辑器优先使用简单 presentation attributes

例如：

```xml
<rect fill="#F5F5F5" stroke="#4A4A4A" stroke-width="2"/>
```

复杂 CSS 可用，但如果目标是跨 Inkscape / Figma / Illustrator 手工编辑，不要把所有视觉属性隐藏在多层 CSS cascade 中。

### 4.2 颜色角色要命名

在生成代码中至少维护：
- `COLOR_PROPOSED`
- `COLOR_REFERENCE`
- `COLOR_BASELINE_1`
- `COLOR_WARNING`
- `COLOR_GUIDANCE`

而不是在几十个元素上散落 hex。

### 4.3 避免过度 SVG filter

drop-shadow、blur、复杂 filter 容易在不同编辑器中表现不同，且 Illustrator 某些效果导出时可能 rasterize。

科研图默认：
- 少阴影；
- 少 blur；
- 少 blend mode；
- 不使用不必要的 filter chain。

---

## 5. 图片资源

### 5.1 可替换版

当 SVG 属于一个 figure package 时，优先让图片作为独立 asset：

```xml
<image id="frame_input"
       href="../assets/frame_input.png"
       x="..." y="..." width="..." height="..."/>
```

这样用户可直接替换 asset。

### 5.2 单文件便携版

另生成：
`figure_portable.svg`

其中可把 raster image 嵌入 data URI。

### 5.3 不要把整张图做成 image

允许 raster 的对象只有：
- 原始照片；
- 视频帧；
- 本来就是 raster 的 field/map。

文字、框、箭头、曲线、坐标轴必须优先保留矢量。

---

## 6. 软件兼容性注意事项

### Inkscape
- 标准 SVG 编辑器；
- `<g>` 可映射为 group；
- Inkscape layer 本质上是带 layer metadata 的 group；
- SVG text 应保留为 text。

### Figma
- 导入 SVG 后会转换为可编辑 vector layer；
- 但某些 SVG 特性并非完全保留；
- Figma 文档明确指出 marker/pattern 在跨工具 SVG copy/paste 时可能不被带入；
- 如果要从 Figma 再导出可编辑文字，需要关闭 Outline text，否则文字默认可能变成 glyph/vector。

### Illustrator
- 可以保存/打开 SVG；
- 如果最终长期在 Illustrator 修改，建议同时保存 `.ai`；
- clean SVG 不应依赖 “Preserve Illustrator Editing Capabilities” 作为跨软件 source of truth，因为该选项会嵌入 Illustrator 数据，且手工修改 SVG XML 后 Illustrator 重新打开时可能读取嵌入的 AI 部分。

### Microsoft 365
- Word/PowerPoint/Excel 可插入 SVG；
- Windows Office 可将 SVG “Convert to Shape” 后拆成 Office shape 做局部修改；
- 更适合快速排版/小改，不是复杂 SVG 的主编辑器。

---

## 7. 禁止项

默认禁止：
- 文本全部 outline；
- 整页 flatten；
- `foreignObject` 用来放 HTML 文本；
- base64 嵌入整张最终图；
- 数百层匿名 group；
- 没有 viewBox；
- 隐藏 clip/mask 链造成对象无法选择；
- 重度 filter / blend mode；
- 一条 path 同时承担文字、框、箭头等多个逻辑角色。

---

## 8. Editable SVG 完成标准

一张 SVG 只有同时满足以下条件才叫“可编辑”：

- [ ] Inkscape 可逐对象选择；
- [ ] 文字可直接双击修改；
- [ ] Stage / panel 可整体移动；
- [ ] 箭头/框可单独改颜色和位置；
- [ ] 曲线/axis/legend 未合并成 bitmap；
- [ ] 有语义 group / id；
- [ ] 无重复 id；
- [ ] 有 viewBox；
- [ ] 打开浏览器显示正常；
- [ ] 通过 `scripts/check_editable_svg.py` 基本检查。
