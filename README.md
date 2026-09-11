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