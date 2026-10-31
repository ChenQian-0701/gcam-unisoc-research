# 紫光展锐机型的 GCam 兼容性研究

[English](README.md) · [天翼一号 2022 专用适配](https://github.com/ChenQian-0701/gcam-tyh212u)

本仓库面向研究者，整理展锐 / Spreadtrum 设备上的 GCam 排障方法、能力调查、实验设计和分析工具。首个案例为天翼一号 2022（TYH212U / ARES、UMS9620、Android 11）。

**这里不提供通用安装包，不承诺展锐全机型兼容。** 模块源码、机型参数、安装构建和实机回归放在独立的 [gcam-tyh212u](https://github.com/ChenQian-0701/gcam-tyh212u) 仓库。

## 阅读顺序

1. [移植流程](docs/porting-guide.md)：先调查实际接口，再分层定位。
2. [处理链](docs/architecture.md)：输入、ISP、合成格式、元数据与融合。
3. [故障分类](docs/failure-modes.md)：黑图、基准帧失败、资源恢复与 AE 冻结。
4. [证据与结论边界](docs/evidence.md)：请求成功、接收成功、保存成功不能互相替代。
5. [画质量化](docs/quality.md)：重复拍摄测波动，同时检查纹理和曝光。
6. [TYH212U 案例](docs/case-studies/tyh212u.md)：已验证事实、有限结论和未解决问题。

## 可以复用什么

- 相机能力采集和日志脱敏工具。
- 对输入像素、电平、曝光/增益、时间戳和生命周期逐层核对的方法。
- 重复 JPEG 平坦区域波动分析工具（仅处理固定构图的 SDR 输出）。
- 设备报告模板和能力记录格式。

**不能直接照搬**：黑电平 0、白电平 1023、6 帧、关闭 Google AWB、混淆类名、单相机可用性改判。这些都有特定版本和设备前提。

工具命令见 [English README](README.md)。原始照片、完整日志和设备序列号留在本地；脱敏工具不能替代人工检查。研究失败记录也欢迎贡献，但应区分观察、推断和未验证方案。

原创代码及文档采用 Apache-2.0，第三方软件保持各自权利，见 [声明](THIRD_PARTY_NOTICES.md)。
