# 方法总览图设计

## 1. 先画“信息流”，再画“算法框”

高质量总览图首先回答：
- 输入是什么；
- 干扰/挑战是什么；
- 方法在哪一步改变问题条件；
- 中间表示是什么；
- 最终输出是什么。

建议先写：

```text
Input
→ Failure / challenge
→ Stage A
→ Intermediate
→ Stage B
→ Reliability / correction
→ Output
```

再将其视觉化。

## 2. 每个 Stage 只包含三种元素

1. 标题
2. 代表性视觉对象
3. 1–2 个关键动作

不要将：
- 所有函数名
- 所有参数
- 所有公式
塞进总览图。

## 3. 推荐总览图构图

### A. Coarse-to-fine

```text
Video
  ↓
[Coarse motion]
  ↓ compensation
[Residual image]
  ↓
[Fine phase]
  ↓
[Total displacement]
```

强调第一阶段如何把残差压回第二阶段的有效工作区间。

### B. Detect–repair

```text
Raw signal
→ feature/statistic
→ abnormal mask
→ repair
→ clean signal
```

### C. Reliability-guided

```text
Raw estimate
→ confidence cues
→ confidence map
→ reject/down-weight
→ refined estimate
```

### D. Hybrid tracking

```text
Global localization
→ local detection
→ bias correction
↘ confidence feedback / update
```

如果有反馈，必须画成回路，不要只在正文说。

## 4. “挑战”应该被视觉化

例如：
- phase wrap：画出 wrapped phase / jump
- target leaving ROI：画出固定框失效
- weak texture：画低 amplitude / singular flow
- gust disturbance：画 contaminated waveform
- UAV motion：画 camera ego-motion 与 structure motion 混合

方法图若没有显式显示 challenge，读者很难理解“为什么需要这些模块”。

## 5. 箭头语义

统一：
- 实线：data flow
- 虚线：guidance / confidence / prior
- 回环箭头：update / feedback
- 双向箭头：真正的双向交互，不要滥用

## 6. 输入输出变量

方法图可保留少量变量：
- integer displacement
- residual
- confidence
- repaired signal

不要放推导细节。

## 7. 方法图与正文的映射

图中的 Stage A/B/C 必须和方法章节的小节标题高度一致。

这样审稿人可从：
`Fig.1 → Section 2.1 → 2.2 → 2.3`
顺着读。

## 8. 常见失败

- 颜色太多，没有主次；
- 视觉对象过大、文字过小；
- pipeline 和实验装置混在同一图；
- 一张图既想讲算法、又想讲结果、又想讲实验；
- 图中缩写正文没有定义；
- 箭头交叉过多。
