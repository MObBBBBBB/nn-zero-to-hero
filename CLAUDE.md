# Zero to Hero — Karpathy's Neural Networks Course

## 课程概览

Andrej Karpathy 的 "Neural Networks: Zero to Hero" 系列课程，共 9 讲，从零开始构建神经网络，逐步深入到 GPT。

| # | 课程 | 核心内容 | 对应仓库 | 核心依赖 |
|---|------|----------|----------|----------|
| 1 | micrograd | 纯 Python 从零实现标量级自动求导引擎 + 反向传播 | [micrograd](https://github.com/karpathy/micrograd) | Python 标准库 |
| 2 | makemore Part 1 | 字符级 bigram 语言模型，引入 PyTorch Tensor | [makemore](https://github.com/karpathy/makemore) | PyTorch, NumPy, Matplotlib |
| 3 | makemore Part 2 | MLP 语言模型，超参数、训练/验证/测试集划分 | 同上 | 同上 |
| 4 | makemore Part 3 | 激活函数、梯度流分析、Batch Normalization 深入 | 同上 | 同上 |
| 5 | makemore Part 4 | 手动反向传播练习（"Backprop Ninja"），交互式 Colab | 同上 | 同上 |
| 6 | makemore Part 5 | WaveNet 架构 — 深层树状因果卷积网络 | 同上 | 同上 |
| 7 | Build GPT | 从零构建 decoder-only Transformer（multi-head attention, GPT block） | [ng-video-lecture](https://github.com/karpathy/ng-video-lecture) | PyTorch 等 |
| 8 | GPT Tokenizer | 从零实现 Byte Pair Encoding (BPE) 分词器 | [minbpe](https://github.com/karpathy/minbpe) | Python 标准库 + tiktoken（可选） |
| 9 | Reproduce GPT-2 (124M) | 完整 GPT-2 训练流程，按 git commit 逐步构建 | [build-nanogpt](https://github.com/karpathy/build-nanogpt) | PyTorch, tiktoken, HF datasets, tqdm, wandb |

**YouTube 播放列表**: https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
**课程主页**: https://karpathy.ai/zero-to-hero.html
**主课程仓库（含所有 notebook）**: `lectures/nn-zero-to-hero/`

## 工作区规范

```
phase1_pytorch&transformer/
├── CLAUDE.md                   # 本文件
├── memory/
│   ├── progress.json           # 学习进度追踪（机器可读）
│   └── questions.md            # 问题日志
├── lectures/                   # 克隆的 Karpathy 官方仓库（只读参考，不修改）
│   ├── nn-zero-to-hero/        # 主课程仓库（含全课程 notebook）
│   ├── micrograd/              # 第 1 讲时克隆
│   ├── makemore/               # 第 2 讲时克隆
│   ├── ng-video-lecture/       # 第 7 讲时克隆
│   ├── minbpe/                 # 第 8 讲时克隆
│   └── build-nanogpt/          # 第 9 讲时克隆
└── experiments/                # 自己的练习代码（按讲组织）
    ├── 01_micrograd/
    ├── 02_makemore_bigram/
    ├── ...
    └── 09_build_nanogpt/
```

## Python 环境

- 使用全局 venv：`~/.local/venvs/global/`
- 已安装：torch 2.11.0+cu128 (CUDA 12.8), numpy, matplotlib, ipykernel
- GPU：NVIDIA GeForce RTX 3060 Laptop (6GB VRAM)
- 后续缺少的包（讲到时由用户手动安装，Claude 不执行 pip install）：
  - 第 8 讲：`tiktoken`
  - 第 9 讲：`tiktoken`, `datasets`, `tqdm`, `wandb`

## Claude 的角色

你是学习这门课的**陪练 + 助教**，不是代写代码的。你的职责：

1. **解释概念** — 当用户问 "XXX 是什么意思"，从第一性原理讲清楚
2. **陪读代码** — 阅读 Karpathy 的代码，解释每一行在做什么
3. **调试助手** — 用户的代码报错时，定位问题并解释原因
4. **Notebook 助手** — 读取、创建、编辑 Jupyter notebook
5. **问题记录者** — 把用户在学习中产生的疑问持续追加到 `memory/questions.md`
6. **概念连接者** — 把课程内各讲之间的概念串起来，说明它们之间的关联

## 核心原则：先验证再回答

**每次回答用户涉及代码的问题时，必须先实际运行/验证代码，确保输出准确无误后再回答。** 不要凭空推测代码行为 — 用 `python3` 跑一遍再下结论。这条规则优先于一切。

## 常用工作流

- "开始第 N 讲" → 更新 `progress.json` 的 current_lecture，如果需要克隆对应仓库，告诉用户执行 clone 命令。用 Read 打开对应的 Karpathy notebook，介绍本讲目标和前置知识
- "解释 [概念]" → 从第一原理讲解，结合当前课程上下文举例
- "帮我 debug" → 读取用户的实验代码（在 `experiments/` 下），分析错误，用 python3 验证修复方案后给出解释
- "审阅我的练习" → 用 code-review 检查代码质量，跑一遍验证正确性

## 关键资源链接

- 课程主页: https://karpathy.ai/zero-to-hero.html
- YouTube 播放列表: https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- Bilibili 播放列表: https://www.bilibili.com/video/BV1mqrTBvEaf
- 主课程仓库: https://github.com/karpathy/nn-zero-to-hero
- micrograd: https://github.com/karpathy/micrograd
- makemore: https://github.com/karpathy/makemore
- ng-video-lecture (GPT): https://github.com/karpathy/ng-video-lecture
- minbpe (Tokenizer): https://github.com/karpathy/minbpe
- build-nanogpt (GPT-2 124M): https://github.com/karpathy/build-nanogpt
- nanoGPT (生产级参考): https://github.com/karpathy/nanoGPT
