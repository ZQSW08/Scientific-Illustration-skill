# Method Overview Wireframe

```text
┌─────────────┐
│   INPUT     │
│ video/data  │
└──────┬──────┘
       │
       v
┌────────────────────┐
│ Challenge / failure│
│ e.g. large motion  │
└────────┬───────────┘
         │
         v
┌────────────────────┐
│ STAGE A            │
│ coarse / normalize │
│ output: z_A        │
└────────┬───────────┘
         │
         v
┌────────────────────┐
│ STAGE B            │
│ fine / phase       │
│ output: z_B        │
└────────┬───────────┘
         │
    ┌────┴─────┐
    │confidence│ - - - - -┐
    └────┬─────┘          │
         v                │
┌────────────────────┐    │
│ STAGE C            │< - ┘
│ repair / fusion    │
└────────┬───────────┘
         │
         v
┌────────────────────┐
│ OUTPUT             │
│ displacement/freq │
└────────────────────┘
```

## 设计提示

- Stage A/B/C 使用统一圆角矩形。
- Challenge 使用与算法不同的视觉语言。
- confidence 是辅助信息，使用虚线。
- 所有箭头尽量不交叉。
