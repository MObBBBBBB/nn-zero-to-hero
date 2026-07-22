# nn-zero-to-hero

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[English](README.md)

> 📝 **转载声明**：若转载或引用本仓库内容，请附上原文链接。

[Andrej Karpathy](https://karpathy.ai/) 的
[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
系列课程学习笔记与实验代码 — 从标量自动求导到 GPT-2，自底向上理解现代深度学习。

## 课程进度

| # | 课题 | 状态 | Notebook |
|---|------|------|----------|
| 1 | micrograd — 标量级自动求导引擎 | ✅ 已完成 | [lec01_micrograd.ipynb](experiments/01_micrograd/lec01_micrograd.ipynb) |
| 2 | makemore Part 1 — bigram 语言模型 | ✅ 已完成 | [lec02_makemore_bigram.ipynb](experiments/02_makemore_bigram/lec02_makemore_bigram.ipynb) |
| 3 | makemore Part 2 — MLP 语言模型 | 🔄 进行中 | |
| 4 | makemore Part 3 — 激活函数与 BatchNorm | ⬜ 未开始 | |
| 5 | makemore Part 4 — Backprop Ninja | ⬜ 未开始 | |
| 6 | makemore Part 5 — WaveNet 架构 | ⬜ 未开始 | |
| 7 | Build GPT — decoder-only Transformer | ⬜ 未开始 | |
| 8 | GPT Tokenizer — BPE 分词器 | ⬜ 未开始 | |
| 9 | Reproduce GPT-2 (124M) | ⬜ 未开始 | |

## 运行环境

- **Python** 3.12.13
- **PyTorch** 2.11.0+cu128
- **CUDA** 12.8
- **GPU** NVIDIA GeForce RTX 3060 Laptop (6 GB VRAM)
- **虚拟环境** `~/.local/venvs/global/`

## 目录结构

```
nn-zero-to-hero/
├── LICENSE
├── README.md
├── README_CN.md
├── CLAUDE.md                     # Claude Code 项目指南
└── experiments/                  # 实验 Notebook
    ├── 01_micrograd/
    ├── 02_makemore_bigram/
    ├── 03_makemore_mlp/
    └── ...
```

## 参考资源

- [课程主页](https://karpathy.ai/zero-to-hero.html)
- [YouTube 播放列表](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Bilibili 播放列表](https://www.bilibili.com/video/BV1mqrTBvEaf)
- [主课程仓库](https://github.com/karpathy/nn-zero-to-hero)
- [micrograd](https://github.com/karpathy/micrograd)
- [makemore](https://github.com/karpathy/makemore)
- [ng-video-lecture (GPT)](https://github.com/karpathy/ng-video-lecture)
- [minbpe (分词器)](https://github.com/karpathy/minbpe)
- [build-nanogpt (GPT-2 124M)](https://github.com/karpathy/build-nanogpt)
- [nanoGPT](https://github.com/karpathy/nanoGPT)

## 许可

MIT — 详见 [LICENSE](LICENSE)。
