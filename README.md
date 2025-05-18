# QuantumCognitiveRadar

This repository contains the LaTeX source code and supplementary materials for the paper "Involuntary Cognitive Influence on Quantum Systems: A Hypothesis Based on Human Radar-like Emission" by Teodor Berger.

## Contents
- `main.tex`: The main LaTeX file for the paper.
- `references.bib`: Bibliography file in BibTeX format.
- `simulation.py`: Python script to simulate the interference patterns described in the paper.
- `.gitignore`: File to exclude temporary LaTeX and compilation files.

## Compilation Instructions
1. Ensure you have a LaTeX distribution (e.g., TeXlive or MikTeX) with `tikz` and `pgfplots` packages installed.
2. Compile `main.tex` using `pdflatex` or `xelatex`:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   ___
   1.  The output will be main.pdf.
Simulation Instructions
To reproduce the interference pattern simulation:
1.  Install Python 3 and required libraries:
```bash
pip install numpy matplotlib
```
2.  Run the simulation script:
```bash
python simulation.py
```
3.  The script generates a plot matching Fig. 2 in the paper.

## Contact
For questions, contact Teodor Berger at bergerteodor@googlemail.com.
## License
This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
