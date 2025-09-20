# 📘 GreenRemover

[English](README.en.md) | 中文

**GreenRemover** 是一个简洁高效的 **绿色背景抠像工具**，基于 Python 实现，支持将带绿幕的图像转换为带透明通道的 PNG，方便后续合成与二次创作。

<p align="center">
  <img src="assets/sample_input.png" alt="输入示例" width="40%">
  <img src="assets/sample_output.png" alt="输出示例" width="40%">
</p>

---

## ✨ 功能特性

* 🎯 **精准抠绿**：自动识别纯绿及偏绿色区域并去除
* 🖼️ **透明输出**：输出为带透明通道的 PNG 格式
* ⚡ **轻量快速**：依赖少，安装简单，可直接命令行使用
* 🔧 **可扩展**：核心算法封装为函数，支持二次开发

---

## 📦 安装方法

### 方式一：通过 `uv`

```bash
git clone https://github.com/avatarreal/greenremover.git
cd greenremover
uv sync
```

### 方式二：通过 `pip`

```bash
pip install greenremover
```

---

## 🚀 使用方法

### 1. 命令行使用

安装完成后，你可以直接运行命令：

```bash
greenremover input.png output.png
```

* `input.png`：输入的带绿幕图像
* `output.png`：输出的抠像结果（带透明背景）

### 2. 作为库调用

你也可以在 Python 中直接调用：

```python
from PIL import Image
from greenremover.core import remove_green

img = Image.open("input.png")
out = remove_green(img)
out.save("output.png")
```

---

## 🧪 开发与测试

### 安装开发依赖

```bash
uv sync --group dev
```

### 运行单元测试

```bash
uv run pytest
```

### 代码检查与格式化

```bash
uv run ruff check greenremover tests   # 代码规范检查
uv run black greenremover tests        # 自动格式化
uv run mypy                            # 静态类型检查
```

---

## 📂 项目结构

```
greenremover/
├── greenremover/
│   ├── __init__.py      # 包入口
│   ├── core.py          # 核心抠像算法
│   └── cli.py           # 命令行接口
├── tests/               # 单元测试
│   └── test_core.py
├── assets/              # 示例图片
├── README.md
├── pyproject.toml       # 项目配置
└── LICENSE
```

---

## 📜 许可证

本项目使用 [MIT License](LICENSE) 开源。  
你可以自由地使用、修改和分发本项目，但请保留原始许可证声明。  

> 注：以上为简要说明，若与英文原文有冲突，以 [LICENSE](LICENSE) 文件中的英文条款为准。

---

## 🌟 致谢

* [Pillow](https://python-pillow.org/) — 图像处理库
* [NumPy](https://numpy.org/) — 数值计算库
* 社区灵感与支持 ❤️

---


⚡ **GreenRemover：让抠像更简单、更纯粹。**


