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
├── README.md
├── main.tex
├── QuantumCognitiveRadar.pdf
├── references.bib
└── simulation.py
```
___
```
1. main.tex
   Purpose: The main LaTeX source file for the paper, containing the complete manuscript in IEEE Dependencies: Requires LaTeX      packages: geometry, amsmath, cite, hyperref, float, caption, tikz,

2. references.bib
   Purpose: BibTeX file containing the bibliography entries cited in the paper.
   Description: This file includes three references formatted according to IEEE standards, covering foundational works             in quantum mechanics and consciousness. The entries are used in main.tex to generate the References section.

3. simulation.py
   Purpose: Python script to simulate the interference patterns described in the paper.
   Description: This script generates simulated data for the interference patterns (with and without a human observer)             using a cosine-squared model with a perturbation to represent cognitive influence. It is referenced in the “Numerical           Simulation” section of main.tex but not embedded in the LaTeX document to keep the PDF clean.

4. README.md
   Purpose: Documentation file providing an overview of the project, compilation instructions, simulation instructions, and        Zenodo metadata.
   Description: This Markdown file serves as the entry point for users accessing the repository. It describes the                  project, lists the files, and provides detailed instructions for compiling the LaTeX document and running the simulation.       It also includes Zenodo metadata for archiving.

5. .gitignore
   Purpose: Git configuration file to exclude temporary and generated files from version control.
   Description: This file ensures that only essential files are tracked in the GitHub repository, excluding LaTeX                  compilation artifacts and Python cache files.

6. QuantumCognitiveRadar.pdf
   Description: output/ final version.
```
___
### Steps for Using This Project in Overleaf

### 1. Create the files in Overleaf:
- Create a new Overleaf project.
- Add the following three files:
  - `.gitignore` (copy the content provided above).
  - `main.tex` (copy the updated LaTeX source).
  - `references.bib` (copy the BibTeX entries).

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
