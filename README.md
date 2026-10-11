# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```
## PW1
### Lab A: Reproducible Foundations

What I built:
Implemented a radioactive decay simulation, set up the conda environment, and added automated unit tests.

Speed comparison (loop vs NumPy):

   - loop: 0.2500 s

   - numpy: 0.0002 s

   - speed-up: 1171.27x faster

Tests: all passing? yes

Conclusion:
In this lab, I built a reproducible environment and repository structure using Git and Conda. I learned that vectorization in NumPy provides a dramatic speedup over pure Python loops. Automated testing with pytest validated the accuracy and boundary cases of the simulation.

### Lab B: Data Visualization and Snakemake Automation

In this lab, we automated the data analysis workflow for radioactive decay observation:

1. **Data Processing & Plotting (`plot.py`)**:
   - Read observed decay counts from `decay_observed.csv` using `numpy.loadtxt`.
   - Calculated the theoretical decay curve $N(t) = N_0 e^{-\lambda t}$ with $\lambda = 0.3$.
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
   - Computed velocity components $v_x = \frac{dx}{dt}$, $v_y = \frac{dy}{dt}$ using `numpy.gradient` and overall speed  $|v| = \sqrt{v_x^2 + v_y^2}$.
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

#### Part 4: Chemical Equilibrium

We computed the equilibrium extent $x$ for the reaction $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$ starting from $1\text{ mol } \text{H}_2$ and $1\text{ mol } \text{I}_2$ with equilibrium constant $K = 15.6$:

- **Methods**: Solved the equilibrium equation $\frac{(2x)^2}{(1-x)^2} - K = 0$ using:
  1. `scipy.optimize.newton` (root-finding on the imbalance function directly).
  2. `scipy.optimize.minimize` with `SLSQP` (minimizing the squared imbalance $[k\_imbalance(x)]^2$).
- **Results**: Both methods yielded identical progress extent $x \approx 0.6638$.
- **Equilibrium Composition**:
  - $n(\text{H}_2) \approx 0.3362\text{ mol}$
  - $n(\text{I}_2) \approx 0.3362\text{ mol}$
  - $n(\text{HI}) \approx 1.3277\text{ mol}$
- **Visualization**: Generated `equilibrium.png` showing reagent decay and product accumulation over reaction progress, marking the equilibrium point $x \approx 0.6638$.

#### Part 5 (Bonus): Titration Equivalence Point

We identified the equivalence point in a titration curve from measured pH vs. added base volume data (`titration.csv`):

- **Method**: Computed the derivative $\frac{dpH}{dV}$ using `numpy.gradient` to identify the point of maximum slope (`np.argmax`).
- **Equivalence Point**: Obtained $V_{\text{eq}} \approx 50.00 \text{ mL}$.
- **Visualization**: Generated `titration.png` with side-by-side plots displaying the titration curve and its derivative peak at $V_{\text{eq}}$.

## PW3
### Dataset 1 - Heart Disease (Cleveland)

#### Session 1 - Characterise the data
##### 1.1 Summary Statistics of Continuous Variables

The continuous variables analyzed include `age`, `trestbps` (resting blood pressure), `chol` (serum cholesterol), and `thalach` (maximum heart rate achieved). All 303 observations are complete for these features.

Key numerical observations:
- **Age (`age`):** The average patient age is **54.4 years** ($\pm 9.0$), ranging from **29 to 77 years**. The median age is **56 years**, indicating that the study population primarily consists of middle-aged and older adults.
- **Resting Blood Pressure (`trestbps`):** The mean resting blood pressure is **131.7 mmHg** ($\pm 17.6$), with a range between **94 and 200 mmHg**. The median value is **130 mmHg**.
- **Serum Cholesterol (`chol`):** The average cholesterol level is **246.7 mg/dl** ($\pm 51.8$). While the 25th to 75th percentile range spans from **211 to 275 mg/dl**, there is a notable maximum value of **564 mg/dl**, suggesting potential extreme values.
- **Max Heart Rate (`thalach`):** The mean maximum heart rate reached during exercise is **149.6 bpm** ($\pm 22.9$), ranging from **71 to 202 bpm** with a median of **153 bpm**.

##### 1.2 The Shape of Continuous Variables

- **age & thalach:** Display roughly unimodal, symmetric distributions centered around middle-to-older age groups and peak heart rates.

- **trestbps & chol:** Exhibit right-skewed distributions with long tails extending toward higher values (including an extreme outlier of $564\text{ mg/dl}$ in cholesterol).

##### 1.3 Normality Testing and Verdicts

Evaluated using Q-Q plots grid (`qq_plots_grid.png`) and Shapiro-Wilk tests ($\alpha = 0.05$):
- **age:** $W = 0.98646$, $p = 0.00607$ $\Rightarrow$ Not normal (though visually close to the theoretical line).
- **chol:** $W = 0.94725$, $p = 0.00000$ $\Rightarrow$ Not normal (pronounced right-tail outliers).
- **trestbps:** $W = 0.96655$, $p = 0.00000$ $\Rightarrow$ Not normal (S-curve deviations).
- **thalach:** $W = 0.97645$, $p = 0.00007$ $\Rightarrow$ Not normal (mild lower-tail deviation).

#### Session 2 - Conclude and Compare
##### 1.4. Is the Effect Real? Group Comparison of `thalach`

We split the maximum heart rate (`thalach`) into two groups based on the binary heart disease `target` (0 = Healthy, 1 = Disease):
- **Healthy Group** ($n = 164$): Mean = $158.38\text{ bpm}$, SE = $1.50$, 95% CI $[155.44, 161.32]$
- **Disease Group** ($n = 139$): Mean = $139.26\text{ bpm}$, SE = $1.92$, 95% CI $[135.50, 143.02]$
- **Hypothesis Testing:** Both the Mann-Whitney U test ($p = 1.86 \times 10^{-13}$) and the two-sample t-test ($p = 3.46 \times 10^{-14}$) yielded extremely significant results ($p < 0.05$).
- **Conclusion:** We reject $H_0$. Healthy individuals achieve a significantly higher maximum heart rate during exercise compared to patients with heart disease. The non-overlapping 95% confidence interval error bars in `thalach_comparison.png` visually confirm this robust finding.

##### 1.5 Do Two Things Move Together? Correlation Analysis

We investigated the relationship between patient age and maximum heart rate (`thalach`):
- **Pearson Correlation Coefficient:** $r = -0.39381$ ($p = 1.11 \times 10^{-12}$).
- **Conclusion:** We reject $H_0$. There is a statistically significant, moderate negative correlation between age and maximum heart rate (`age_thalach_correlation.png`), indicating that peak exercise heart rate reliably decreases as age increases.