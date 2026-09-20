# 中间过程与机制验证图

## 1. 为什么需要中间过程图

只有“最终误差更低”无法证明新模块按宣称机制工作。

中间图的任务是建立：

```text
failure observable
→ module response
→ corrected representation
→ final benefit
```

## 2. 推荐四联图

### Phase wrapping
(a) raw displacement / wrapped phase
(b) coarse estimate
(c) compensated residual phase
(d) final reconstructed displacement

### Reliability
(a) raw phase/flow
(b) edge/amplitude cue
(c) confidence / abnormal probability
(d) refined flow

### Disturbance repair
(a) contaminated waveform
(b) anomaly score + threshold
(c) abnormal interval mask
(d) repaired waveform + spectrum

### Tracking
(a) global localization
(b) local crop / search region
(c) detected geometry
(d) corrected center trajectory

## 3. “before/after”必须给机制变量

仅有：
`raw → final`
容易被 reviewer 质疑是黑盒。

至少增加：
- confidence
- mask
- residual
- kernel response
- phase nonlinearity indicator
中的一个。

## 4. 局部放大

适合：
- waveform jump
- sub-pixel deviation
- tracking loss
- edge center difference

放大图要有：
- source rectangle
- connector
- 同一坐标单位
- 不改变 y-scale 去夸大差异

## 5. Ablation 图

推荐：
```text
baseline
+ module A
+ A+B
+ A+B+C
```

如果 module B 本身很关键，再加 B-only。

颜色可以固定：
- baseline 灰
- incremental stages 同一主色由浅到深
- full proposed 最深

## 6. 参数机制图

当参数有明确物理作用时，优先用：
- kernel + frequency response 双面板
- parameter ↑ 时 3 条代表曲线
- 标出 passband/threshold/linear range

不要只给一张 sensitivity bar，而不解释参数如何改变机制。

## 7. Failure case 也可以是主图

若方法具有 failure detection：
- valid
- degraded
- invalid
三种状态非常值得画。

“知道自己什么时候不可信”本身就是测量方法的重要能力。
