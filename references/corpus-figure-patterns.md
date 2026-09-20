# 高水平视觉测振论文中的图形模式蒸馏

以下仅提炼图形与论证模式，不复制原图。

## 1. M-PME

强图形模式：
- 先用简单 Gaussian surface + 多振幅曲线展示 phase wrap failure；
- 再给 pyramid / coarse-to-fine schematic；
- 后续实验将 trajectory、error 与真实旋转/非旋转场景对应。

可迁移：
> “失败现象图”应早于“复杂方法图”。

## 2. APM-IPOF

方法图强调：
- integer-pixel coarse stage
- compensated/reconstructed sequence
- sub-pixel phase stage
- additive fusion

它把 coarse 和 fine 用“残差工作区间”连接，而非视觉上并列。

后续图中：
- ASR flowchart
- IPOF flowchart
分别细化两个主要贡献。

可迁移：
> 一个总览图 + 每个真正创新模块各一张局部流程图，是很稳妥的层级。

## 3. SPOF

典型图序：
- Fig.1 proposed method
- Fig.2 spatial constraints
- 后续显示 confidence / outlier correction / 位移结果

这类图适合：
```text
physical prior
→ confidence
→ probabilistic outlier
→ repair
```

## 4. BPAF

非常值得学习：
- temporal kernel 与 amplitude spectrum 同图出现；
- nonlinear suppression 用真实 waveform before/after 展示；
- ablation 同时给 time waveform + spectrum；
- prior-frequency sweep 用结果曲线说明参数宽容度。

可迁移：
> 若创新是滤波器，不只画最终 FFT；必须画 kernel、frequency response 和 signal effect。

## 5. DA-ViReS

Fig.1 把真实 gust 输入、方向归一化、微振动增强、signal repair 分区。

后续过程图不是只给误差：
- direction-aware normalization
- enhanced vibration slice
- abnormal detection/repair
- 最后才是多 cable error / interference-intensity robustness

可迁移：
> 现场算法应先“展示处理过程”，再“展示汇总指标”。

## 6. UAV L-D-C

复杂系统通过多图层级化：
- overall measurement framework
- improved KCF feedback
- dynamic search region
- edge/detection details
- ego-motion compensation
- time histories
- NRMSE/PCC
- mode shapes

可迁移：
> 大系统不要试图一张图讲完。总览图负责职责，子图负责算法，结果图负责证据。

## 7. Camera-disturbance reliability

优秀做法是让 reliability 成为可视化对象：
- spatial map
- temporal reliability
- reconstructed spectrum

这让“可靠性”不是一句形容词，而是可观察量。

## 8. PNL stereo

适合学习：
- geometry / PNL mechanism schematic
- filter configuration comparison
- algorithm comparison
- illumination/sensitivity robustness

可迁移：
> 对抽象新指标，要同时展示“定义示意 + 它与误差的相关关系”。

## 9. Crossline phase center

标记目标研究常见有效组合：
- marker geometry
- phase response/zero crossing
- pose/large-motion scene
- tracking trajectory/error

可迁移：
> 如果创新是 measurement-oriented feature design，图一定要让几何特征和定位原理在视觉上对应。

## 10. LoG-Gabor many-task optimization

滤波器优化类图要同时包含：
- filter family / response
- task relation/transfer
- optimization result
- full-field result

否则容易看起来像“只是在调参”。
