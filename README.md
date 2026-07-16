# nn-zero-to-hero

My learning notes and experiments for Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) course.

## Environment

- Python 3.12.13
- PyTorch 2.11.0+cu128
- CUDA 12.8
- GPU: NVIDIA GeForce RTX 3060 Laptop (6GB VRAM)

## Progress

| # | Lecture | Status | Notes |
|---|---------|--------|-------|
| 1 | micrograd | ✅ Done | [Notebook](experiments/01_micrograd/lec01_micrograd.ipynb) |
| 2 | makemore Part 1 (Bigram) | 🔄 In Progress | — |
| 3 | makemore Part 2 (MLP) | ⬜ Not started | |
| 4 | makemore Part 3 (BatchNorm) | ⬜ Not started | |
| 5 | makemore Part 4 (Backprop Ninja) | ⬜ Not started | |
| 6 | makemore Part 5 (WaveNet) | ⬜ Not started | |
| 7 | Build GPT | ⬜ Not started | |
| 8 | GPT Tokenizer (BPE) | ⬜ Not started | |
| 9 | Reproduce GPT-2 (124M) | ⬜ Not started | |

## Structure

```
nn-zero-to-hero/
├── CLAUDE.md          # Project guide for Claude Code
├── README.md
├── experiments/       # My own practice code
│   ├── 01_micrograd/
│   ├── 02_makemore_bigram/
│   └── ...
└── memory/
    ├── progress.json  # Lecture progress tracker
    └── questions.md   # Running question log
```

## Resources

- [Course homepage](https://karpathy.ai/zero-to-hero.html)
- [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Main course repo](https://github.com/karpathy/nn-zero-to-hero)
