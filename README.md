# Detailed Project Structure
The project “Involuntary Cognitive Influence on Quantum Systems: A Hypothesis Based on Human Radar-like Emission” is structured to ensure reproducibility, clarity, and compatibility with academic publishing standards (IEEE format) and open-access archiving platforms (Zenodo and GitHub). Below is the detailed structure of the project, including all files, their purposes, and their organization.
```
Repository Overview
•  Repository URL: https://github.com/DonMask/QuantumCognitiveRadar
•  Zenodo DOI: 10.5281/zenodo.15458571
•  Author: Teodor Berger, Independent Researcher (bergerteodor@googlemail.com)
•  License: Creative Commons Attribution 4.0 International (CC BY 4.0)
```
The project consists of a LaTeX document, a bibliography file, a Python simulation script, and supporting files for documentation and version control. All figures are generated internally using tikz and pgfplots to ensure no external dependencies.
File Structure
The repository contains the following files, organized in a flat structure for simplicity:
```
QuantumCognitiveRadar/
├── main.tex
├── references.bib
├── simulation.py
├── README.md
└── .gitignore
```
## Compilation Instructions
1. Ensure you have a LaTeX distribution (e.g., TeXlive or MikTeX) with `tikz` and `pgfplots` packages installed.
2. Compile `main.tex` using `pdflatex` or `xelatex`:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   The output will be main.pdf.
___
## Simulation Instructions
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
___
