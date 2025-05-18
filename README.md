# Detailed Project Structure
The project “Involuntary Cognitive Influence on Quantum Systems: A Hypothesis Based on Human Radar-like Emission” is structured to ensure reproducibility, clarity, and compatibility with academic publishing standards (IEEE format) and open-access archiving platforms (Zenodo and GitHub). Below is the detailed structure of the project, including all files, their purposes, and their organization.

## Repository Overview
___
##### •  Repository URL: https://github.com/DonMask/QuantumCognitiveRadar
##### •  Zenodo DOI: 10.5281/zenodo.15458571
##### •  Author: Teodor Berger, Independent Researcher (bergerteodor@googlemail.com)
##### •  License: Creative Commons Attribution 4.0 International (CC BY 4.0)
___
The project consists of a LaTeX document, a bibliography file, a Python simulation script, and supporting files for documentation and version control. All figures are generated internally using tikz and pgfplots to ensure no external dependencies.

## The repository contains the following files, organized in a flat structure for simplicity:
```
QuantumCognitiveRadar/
├── .gitignore
├── LICENSE
├── README.md
├── main.tex
├── QuantumCognitiveRadar.pdf
├── references.bib
└── simulation.py
```
___
### Steps for Using This Project in Overleaf

### 1. Create the files in Overleaf:
- Create a new Overleaf project.
- Add the following three files:
  - `.gitignore` 
  - `main.tex` 
  - `references.bib` 

### 2. Compile `main.tex`:
- Set `main.tex` as the main document.
- Use the `pdfLaTeX` compiler (default).
- Click **Recompile** to generate the PDF (~4 pages).
- You may need to compile 2–3 times for all citations from `references.bib` to resolve.

### Troubleshooting

**Citation issues:**
- If you see `[?]` instead of proper references like [1], [2], [3], try compiling 2–3 times.
- Make sure `references.bib` is in the root directory of the project.
___
## Simulation Instructions
   To reproduce the interference pattern simulation:
1. Install Python 3 and required libraries:
```bash
    pip install numpy matplotlib
```
2. Run the simulation script:
```bash
    python simulation.py
```
3. The script generates a plot matching Fig. 2 in the paper.
___
