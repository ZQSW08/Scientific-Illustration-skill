# 视觉语言规范

## 1. 全文固定角色色

建议先定义角色，而不是具体颜色名：

- proposed
- reference
- primary baseline
- secondary baselines
- disturbance/outlier
- confidence

只要角色一致，具体期刊配色可后调。

## 2. 色盲与黑白

关键类别不要只靠色相区分，同时使用：
- solid / dashed
- marker shape
- line width
- hatch（少量）

尤其避免“红 vs 绿”作为唯一编码。

## 3. 饱和度层级

主方法：
- 高饱和、较深

baseline：
- 低饱和

背景区域：
- 很浅

outlier：
- 警示但不要整张图都是红色

## 4. 连续 colormap

优先 perceptually uniform：
- viridis
- cividis
- magma 等

正负位移/相位：
- diverging colormap
- 0 对齐中心

禁止使用 rainbow/jet 表达连续误差，除非领域有强制习惯且解释充分。

## 5. 字体

- 全文统一字体族
- panel label (a)(b) 更醒目
- axis label > tick label
- 缩放到最终版面仍可读

不要在同一图混用中英文字体、衬线/无衬线多套风格。

## 6. 线宽

建立层级：
- reference/proposed：较粗
- baseline：正常
- grid：极细且低对比
- ROI / annotation：不应比数据曲线更抢眼

## 7. 留白

好的方法图大量留白。

不要因为“还有空白”就填元素。

## 8. 面板编号

统一放在左上角，避免每张子图位置不同。

## 9. Legend

- 避免挡数据
- 方法多时可用 figure-level legend
- 顺序与正文/表格保持一致

## 10. Annotation

只标：
- 关键 peak
- failure point
- threshold
- transition
- ROI

不要标每个点。
