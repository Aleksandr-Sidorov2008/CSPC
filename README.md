# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```
## PW1
###Lab A: Reproducible Foundations

What I built:
Implemented a radioactive decay simulation, set up the conda environment, and added automated unit tests.

Speed comparison (loop vs NumPy):

    loop: 0.2500 s

    numpy: 0.0002 s

    speed-up: 1171.27x faster

Tests: all passing? yes

Conclusion:
In this lab, I built a reproducible environment and repository structure using Git and Conda. I learned that vectorization in NumPy provides a dramatic speedup over pure Python loops. Automated testing with pytest validated the accuracy and boundary cases of the simulation.

###Lab B: Data Visualization and Snakemake Automation

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
```
## PW2
### Lab A: Motion from Tracking Data

In this lab, we analyzed noisy position data of a falling object to explore numerical differentiation and integration:

1. **Numerical Differentiation & Noise Amplification**:
   - Calculated velocity $v = \frac{dy}{dt}$ and acceleration $a = \frac{dv}{dt}$ using `numpy.gradient`.
   - **Mean acceleration**: $-8.58\text{ m/s}^2$ (close to theoretical $g \approx -9.81\text{ m/s}^2$).
   - **Standard deviation**: $28.72\text{ m/s}^2$. 
   - **Noise Observation**: Numerical differentiation amplifies high-frequency measurement noise because comparing small, noisy differences between nearby points creates extreme slope fluctuations.

2. **Numerical Integration & Noise Suppression**:
   - Reconstructed velocity and position using `scipy.integrate.cumulative_trapezoid`.
   - **Max position error**: $0.78\text{ m}$.
   - **Conclusion**: Integration accumulates values and causes random measurement noise to cancel out, effectively smoothing the data and accurately recovering the original position despite highly noisy acceleration.

3. **Bonus: 2D Trajectory Analysis**:
   - Analyzed 2D motion data from `trajectory.csv` ($x$ and $y$ over time $t$).
   - Computed velocity components $v_x = \frac{dx}{dt}$, $v_y = \frac{dy}{dt}$ using `numpy.gradient` and overall speed $\vert{}v\vert{} = \sqrt{v_x^2 + v_y^2}$.
   - Visualized the resulting figure-eight trajectory (Lissajous curve) alongside total speed over time in `trajectory.png`.

#### Visualization
- 3-panel comparative motion plot saved as `motion.png`.
- 2D trajectory and magnitude of velocity plot saved as `trajectory.png`.

### Lab B: Optimization in Chemistry

#### Part 2: Three Routes to a Minimum

We compared three optimization algorithms on two different mathematical landscapes:

1. **Simple Convex Function ($f(x) = (x-3)^2 + 1$)**:
   - **Methods tested from $x_0 = 0$**: Gradient Descent, Newton's Method (on $f'(x) = 0$), and SLSQP (`scipy.optimize.minimize`).
   - **Results**: All three methods converged seamlessly to the global minimum at $x = 3.0000$ ($f(x) = 1.0000$).
   - **Observation**: On a simple convex landscape, the initial starting guess and algorithm choice do not alter the final result.

2. **Harder Landscape ($g(x) = x^4 - 3x^2 + x + 5$)**:
   - **Gradient Descent**:
     - From $x_0 = 0$: Converged to local/global minimum at $x \approx -1.3008$ ($g(x) \approx 1.4861$).
     - From $x_0 = 2$: Converged to local minimum at $x \approx 1.1309$ ($g(x) \approx 3.9298$).
   - **Newton's Method**:
     - From $x_0 = 0$: Solved $g'(x) = 0$ and landed on $x \approx 0.1699$ ($g(x) \approx 5.0841$). Evaluating $g''(0.1699) = -5.65 < 0$ confirmed this stationary point is a **local maximum**, not a minimum.
     - From $x_0 = 2$: Solved $g'(x) = 0$ and landed on $x \approx 1.1309$ ($g(x) \approx 3.9298$). Evaluating $g''(1.1309) = 9.35 > 0$ confirmed a **local minimum**.
   - **SLSQP (`minimize`)**:
     - From $x_0 = 0$: Found global minimum at $x \approx -1.3009$ ($g(x) \approx 1.4861$).
     - From $x_0 = 2$: Found global minimum at $x \approx -1.3006$ ($g(x) \approx 1.4861$).

**Key Takeaways**:
- On complex landscapes with multiple stationary points, Newton's method can converge to local maxima because it only seeks root locations where the first derivative equals zero ($g'(x) = 0$). Checking the second derivative ($g'' > 0$) is essential.

#### Part 3: Reaction Kinetics Fitting

We fitted a first-order rate law $C(t) = C_0 e^{-kt}$ to experimental concentration measurements (`kinetics.csv`) using non-linear least squares optimization:

- **Objective Function**: Minimized the sum of squared errors between experimental data and theoretical exponential decay.
- **Optimization Method**: Used `scipy.optimize.minimize` with the `SLSQP` algorithm bounded within $k \in [0, 5]$.
- **Fitted Parameter**: Obtained a rate constant of $k \approx 0.2618 \text{ s}^{-1}$.
- **Visualization**: Generated `kinetics.png` demonstrating an excellent exponential fit over the noisy experimental measurements.