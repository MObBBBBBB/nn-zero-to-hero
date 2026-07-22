# nn-zero-to-hero

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[中文版本](README_CN.md)

> 📝 **Attribution Notice**: If you find these notes helpful and share or
> repost them elsewhere, please link back to this repository. Thanks!

My learning notes and hands-on experiments for Andrej Karpathy's
[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
course — a bottom-up journey from scalar autograd to GPT-2.

## Progress

| # | Lecture | Status | Notebook |
|---|---------|--------|----------|
| 1 | micrograd | ✅ Done | [lec01_micrograd.ipynb](experiments/01_micrograd/lec01_micrograd.ipynb) |
| 2 | makemore Part 1 (Bigram) | ✅ Done | [lec02_makemore_bigram.ipynb](experiments/02_makemore_bigram/lec02_makemore_bigram.ipynb) |
| 3 | makemore Part 2 (MLP) | 🔄 In Progress | |
| 4 | makemore Part 3 (BatchNorm) | ⬜ Not started | |
| 5 | makemore Part 4 (Backprop Ninja) | ⬜ Not started | |
| 6 | makemore Part 5 (WaveNet) | ⬜ Not started | |
| 7 | Build GPT | ⬜ Not started | |
| 8 | GPT Tokenizer (BPE) | ⬜ Not started | |
| 9 | Reproduce GPT-2 (124M) | ⬜ Not started | |

## Environment

- **Python** 3.12.13
- **PyTorch** 2.11.0+cu128
- **CUDA** 12.8
- **GPU** NVIDIA GeForce RTX 3060 Laptop (6 GB VRAM)
- **venv** `~/.local/venvs/global/`

## Structure

```
nn-zero-to-hero/
├── LICENSE
├── README.md
├── README_CN.md
├── CLAUDE.md                     # Project guide for Claude Code
└── experiments/                  # My practice notebooks
    ├── 01_micrograd/
    ├── 02_makemore_bigram/
    ├── 03_makemore_mlp/
    └── ...
```

## Resources

- [Course homepage](https://karpathy.ai/zero-to-hero.html)
- [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Bilibili playlist](https://www.bilibili.com/video/BV1mqrTBvEaf)
- [Main course repo](https://github.com/karpathy/nn-zero-to-hero)
- [micrograd](https://github.com/karpathy/micrograd)
- [makemore](https://github.com/karpathy/makemore)
- [ng-video-lecture (GPT)](https://github.com/karpathy/ng-video-lecture)
- [minbpe (Tokenizer)](https://github.com/karpathy/minbpe)
- [build-nanogpt (GPT-2 124M)](https://github.com/karpathy/build-nanogpt)
- [nanoGPT](https://github.com/karpathy/nanoGPT)

## License

MIT — see [LICENSE](LICENSE) for details.
