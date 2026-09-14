# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations

What I built:
Implemented a radioactive decay simulation, set up the conda environment, and added automated unit tests.

Speed comparison (loop vs NumPy):

    loop: 0.2500 s

    numpy: 0.0002 s

    speed-up: 1171.27x faster

Tests: all passing? yes

Conclusion:
In this lab, I built a reproducible environment and repository structure using Git and Conda. I learned that vectorization in NumPy provides a dramatic speedup over pure Python loops. Automated testing with pytest validated the accuracy and boundary cases of the simulation.

Lab B: Data Visualization and Snakemake Automation

In this lab, we automated the data analysis workflow for radioactive decay observation:

1. **Data Processing & Plotting (`plot.py`)**:
   - Read observed decay counts from `decay_observed.csv` using `numpy.loadtxt`.
   - Calculated the theoretical decay curve $N(t) = N_0 e^{-lambda t} with lambda = 0.3.
   - Generated a 1x2 comparative figure (`figure.png`) with shared axes comparing experimental scatter data against the theoretical curve.

2. **Workflow Automation (`Snakefile`)**:
   - Defined a Snakemake pipeline linking inputs (`plot.py`, `decay_observed.csv`) to the output (`figure.png`).
   - Automated rule execution to ensure reproducibility when raw data or scripts change.

### How to Run

To run the pipeline and generate the figure automatically:

```bash
cd "PW1/Lab B"
snakemake --cores 1