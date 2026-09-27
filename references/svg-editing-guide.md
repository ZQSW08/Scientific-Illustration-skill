# 如何编辑本 Skill 生成的 SVG

## 最推荐：Inkscape

适合用户本地直接修改科研 SVG。

### 基本步骤

1. 安装并打开 Inkscape。
2. File → Open → 选择 `figure_editable.svg`。
3. 打开 Objects/Layers 面板。
4. 展开：
   - Background
   - Stage 1
   - Stage 2
   - Connectors
   - Annotations
5. 修改：
   - 文本：Text tool；
   - 框/箭头：Select tool；
   - 节点：Node tool；
   - 颜色：Fill and Stroke；
   - 图层：Objects/Layers。

### 推荐操作

- 改文字：优先直接修改 `<text>`，不要转 path。
- 移动一个 stage：选中其 group，一次整体移动。
- 改箭头：选 path，再改 stroke/marker。
- 更换视频帧：替换 package 中 assets 文件，或重新 link/embed。
- 导出投稿前 PDF：保留一份原始 editable SVG。

### 不要轻易做

- Path → Object to Path（尤其是文字）；
- Flatten；
- 大量 Boolean 后不保留源；
- 把所有 group 解散。

这些操作往往降低后续可编辑性。

---

## Figma

Figma 官方说明：SVG 导入后会转成 editable vector layer。

使用：
1. 打开 Figma Design；
2. 将 SVG 直接拖入 canvas；
3. 图层面板中选择 group/vector；
4. Enter 进入 vector edit mode；
5. 可编辑节点、fill、stroke、group。

注意：
- Figma 某些 SVG 特性在跨工具时可能丢失；
- marker/pattern 是已知兼容性风险；
- 若从 Figma 再导出 SVG，并希望文字保持可编辑，应关闭 “Outline text”。

因此 Figma 很适合：
- 改布局；
- 改矢量 shape；
- 协同编辑；
- 快速改色。

但若图大量依赖 scientific text / marker / native layer 语义，Inkscape 更适合作为 clean SVG 主编辑器。

---

## Adobe Illustrator

适合已有 Adobe 工作流的用户。

建议：
- 打开 `figure_editable.svg`；
- 另存 `.ai` 作为 Illustrator 主源；
- 导出 clean SVG 作为交换文件。

如果勾选 “Preserve Illustrator Editing Capabilities”，SVG 会带额外 Illustrator 数据，文件会更大；而且 Illustrator 重开时可能优先读取嵌入的 Illustrator 部分，所以不应让这个版本成为跨软件唯一源。

---

## PowerPoint / Excel

Microsoft 365 Windows 可以：
1. Insert → Pictures → SVG；
2. 右键 SVG；
3. Convert to Shape；
4. 拆开后逐部分编辑；
5. 修改后重新 Group。

适合：
- 改颜色；
- 简单移动；
- 图标/小流程图。

不适合：
- 大量路径；
- 科研复杂总览图；
- 需要长期维护的主源。

---

## Boxy SVG

Boxy SVG 是专门面向 SVG 的编辑器，官方强调：
- geometry / transform / paint 可在画布编辑；
- 支持 group/arrange/path operations；
- 保留 IDs、classes、metadata；
- 可直接查看/编辑 SVG/CSS。

适合：
- 想直接编辑标准 SVG；
- 不想安装大型桌面软件；
- 希望同时看图与 SVG 代码。

---

## 直接编辑 XML

SVG 本质是 XML。

如果本 Skill 生成语义化 id，可以直接在 VS Code 搜索：

```text
id="title_stage_2"
id="curve_proposed"
id="roi_zoom_1"
```

修改文字：

```xml
<text id="title_stage_2">New title</text>
```

修改颜色：

```xml
stroke="#B2182B"
```

这种方式特别适合：
- 批量替换字体；
- 批量改颜色；
- 改标签；
- 调整少量数值。

---

## 推荐的软件优先级

如果目标是“科研 SVG 本地可编辑”：

### 免费本地优先
**Inkscape**

### 已有 Adobe
**Illustrator**

### 在线/协作
**Figma**

### 专注 SVG
**Boxy SVG**

### 只想小改并插进论文/PPT
**PowerPoint/Excel Convert to Shape**

---

## Skill 输出时必须告诉用户

每次生成 SVG 后，回复应至少说明：

1. 哪个文件是 editable source；
2. 推荐用什么软件打开；
3. 文本是否保留为 text；
4. raster asset 是否外链/嵌入；
5. 是否还有 Origin/Visio 原生源；
6. 哪个文件是投稿/预览版。
