# nn-zero-to-hero

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[中文版本](README_CN.md)

> 📝 **Attribution Notice**: If you find these notes helpful and share or
> repost them elsewhere, please link back to this repository. Thanks!

My learning notes and hands-on experiments for Andrej Karpathy's
[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
course, with GPT-2 reproduction as a follow-up goal. This is a personal learning
repository, not the official course repository or a complete reimplementation of
Karpathy's makemore/nanoGPT libraries. Completed and ongoing work is listed below.

## Progress

| # | Lecture | Status | Notebook |
|---|---------|--------|----------|
| 1 | micrograd | ✅ Done | [lec01_micrograd.ipynb](experiments/01_micrograd/lec01_micrograd.ipynb) |
| 2 | makemore Part 1 (Bigram) | ✅ Done | [lec02_makemore_bigram.ipynb](experiments/02_makemore_bigram/lec02_makemore_bigram.ipynb) |
| 3 | makemore Part 2 (MLP) | ✅ Done | [lec03_makemore_mlp.ipynb](experiments/03_makemore_mlp/lec03_makemore_mlp.ipynb) |
| 4 | makemore Part 3 (BatchNorm) | ✅ Done | [lec04_makemore_batchnorm.ipynb](experiments/04_makemore_batchnorm/lec04_makemore_batchnorm.ipynb) |
| 5 | makemore Part 4 (Backprop Ninja) | ⏳ Deferred until after the 2027 entrance exam | [lec05_makemore_backprop.ipynb](experiments/05_makemore_backprop/lec05_makemore_backprop.ipynb) |
| 6 | makemore Part 5 (WaveNet) | ✅ Done | [lec06_makemore_wavenet.ipynb](experiments/06_makemore_wavenet/lec06_makemore_wavenet.ipynb) |
| 7 | Build GPT | 🔄 In progress | [lec07_build_gpt.ipynb](experiments/07_build_gpt/lec07_build_gpt.ipynb) |
| 8 | GPT Tokenizer (BPE) | ⬜ Not started | |
| 9 | Reproduce GPT-2 (124M) | ⬜ Not started | |

## Environment

Recorded development environment (not a requirement for every lecture):

- **Python** 3.12.13
- **PyTorch** 2.11.0+cu128
- **CUDA** 12.8
- **GPU** NVIDIA GeForce RTX 3060 Laptop (6 GB VRAM)

The current notebooks use PyTorch, NumPy and Matplotlib. The micrograd notebook
also uses the Python `graphviz` package and the Graphviz `dot` executable for
computation graphs. Use a Jupyter-compatible editor with a Python kernel.

## Running the notebooks

Select a kernel with the required packages and run cells in order from each
notebook's own directory. The makemore notebooks read `../names.txt`, and the
Build GPT notebook reads `../input.txt`; both datasets are included in
`experiments/`. Training settings may need adjustment for your hardware.

## Structure

```
nn-zero-to-hero/
├── LICENSE
├── README.md
├── README_CN.md
└── experiments/                  # My practice notebooks
    ├── names.txt                 # Shared makemore dataset
    ├── input.txt                 # Shakespeare text for Build GPT
    ├── 01_micrograd/
    ├── 02_makemore_bigram/
    ├── 03_makemore_mlp/
    ├── 04_makemore_batchnorm/
    ├── 05_makemore_backprop/
    ├── 06_makemore_wavenet/
    └── 07_build_gpt/
```

This tree shows the published files. Local reference clones (`lectures/`),
progress records (`memory/`) and AI assistant instructions (`AGENTS.md`) are
Git-ignored and are not included when cloning this repository.

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
