# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- - I created the CSPC repository with a conda environment, Git branches, pytest tests and a speed comparison script.

**Speed comparison (loop vs NumPy):**
- loop : 1.766 s
- numpy : 0.012 s
- speed-up: 147.2 x faster

**Tests:** all passing? yes

**Conclusion:**
- I built a reproducible setup: a conda environment from environment.yml, a Git repository with a branch and merge, and three passing pytest tests. NumPy was about 147.2 times faster than the pure-Python loop, because it handles all atoms at once instead of one by one in a Python loop.
- Some things went wrong at first: environment.yml was saved empty so the environment had no Python, and the GitHub repository name had a typo, which caused "Repository not found" when pushing. I fixed both by checking the file with cat and renaming the repository.
- I learned that a small mistake in a file or a name can break the whole workflow, and that checking each step (git status, pytest -v) saves time.

## PW1 --- Lab B

**What the data showed:** The observed counts start at about 5000 and decrease over time, quickly at first and then more slowly, until they are close to zero after about t = 12. The points show only very small scatter.

**Match with the analytical law:** Yes, the observed points follow the same exponential decay shape as the analytical curve N0*exp(-0.3 t), where N0 is the first observed count. On the shared axes the two panels look the same, so the data agree with the law.

**Snakemake pipeline:** The Snakefile has one rule that builds figure.png from decay_observed.csv by running plot.py, and Snakemake only reruns it when its input has changed.

## PW2 --- Lab A

- **Mean acceleration:** -8.58 m/s² (std = 28.7 m/s²), roughly consistent with -g = -9.81 m/s², so the object is in free fall. The mean deviates from -9.81 because of the large noise in the acceleration.
- **Why the acceleration is noisy:** A derivative compares nearby measurements, so it amplifies noise. The acceleration is a second derivative, so the noise is amplified twice, while the position is not differentiated at all.
- **Integrating back:** Integrating the noisy acceleration twice recovered the position with a maximum difference of 0.78 m from the original, showing that integration suppresses noise.

## PW2 --- Lab B

### Part 2: three optimisation methods
- On the convex function f(x) = (x-3)^2 + 1, gradient descent, Newton's method and SLSQP all reached x = 3.
- On g(x) = x^4 - 3x^2 + x + 5, the methods did not always agree. From x0 = 0, Newton's method converged to x = 0.17, where g'' < 0, so it is a maximum, not a minimum, while gradient descent and SLSQP reached the minimum at x = -1.30. From x0 = 2, gradient descent and Newton reached the local minimum at x = 1.13.
- The starting point and the algorithm both matter on a complicated landscape: g has two minima (x = -1.30 and x = 1.13) and a maximum, and the result depends on which one is closest to the start. Newton finds any stationary point, so g'' must be checked.

### Part 3: reaction rate
- Fitted rate constant: k = X (close to 0.25), and the fitted curve passes through the data (kinetics.png).

### Part 4: equilibrium
- Newton and SLSQP agree: x = X. Equilibrium amounts: H2 = X mol, I2 = X mol, HI = X mol (equilibrium.png).

### Part 5: titration (bonus)
- The equivalence point is at X mL, where the slope of the pH curve is largest (titration.png).

## PW3 --- Data, Distributions, Testing, Causation

Data: Heart Disease (Cleveland), UCI Machine Learning Repository, Janosi, Steinbrunn, Pfisterer, Detrano (1989), https://doi.org/10.24432/C52P4X. The original 0--4 target was converted to 0/1 (0 = no disease, 1--4 = disease). The chemicals dataset is synthetic (Moodle).

### Session 1: distributions and normality

- age is roughly bell-shaped with a slight left skew. chol and trestbps are right-skewed (chol has one extreme value near 560). thalach is left-skewed (distributions.png).
- Normality verdicts (Q-Q plots in qqplots.png and Shapiro-Wilk test):
  - age: approximately normal. The Q-Q plot is almost a straight line and the skew is small (-0.21). The Shapiro test formally rejects normality (p = 0.006), but with n = 303 this test detects even tiny deviations, so I judged by the plot and the skew together.
  - chol: not normal (Shapiro p = 5.9e-09, skew = 1.13). The upper tail bends strongly away from the line in the Q-Q plot.
  - trestbps: not normal (Shapiro p = 1.8e-06, skew = 0.70). The right tail bends away from the line.
  - thalach: not normal (Shapiro p = 7.0e-05, skew = -0.53). The lower tail bends away from the line.

### Session 2: heart rate and age

- Do heart-disease patients reach a different maximum heart rate? thalach is not normal (Session 1), so I compared the two groups with the Mann-Whitney U test (rank-based, no normality assumption). I also ran a Welch t-test as a check.
  - Disease (n = 139): mean thalach = 139.26 bpm, SEM = 1.92 (95% CI half-width 3.76).
  - Healthy (n = 164): mean thalach = 158.38 bpm, SEM = 1.50 (95% CI half-width 2.94).
  - Mann-Whitney U = 5806.5, p = 1.9e-13. Welch t = -7.86, p = 9.1e-14.
  - Conclusion: patients with heart disease reach a significantly lower maximum heart rate (about 19 bpm lower). The 95% confidence intervals of the two means do not overlap (thalach_means.png), so the plot agrees with the test.
- age vs thalach: Spearman rho = -0.392 (p = 1.5e-12) and Pearson r = -0.394 (p = 1.1e-12). Maximum heart rate decreases as age increases; the relationship is negative and moderate (age_vs_thalach.png). I rely mainly on Spearman because thalach is not normal.
- Bonus: the target proportions are 0.541 (no disease) and 0.459 (disease). Entropy = 0.995 bits (maximum 1 for two categories) and Gini = 0.497 (maximum 0.5), so the column is almost perfectly balanced, i.e. hard to guess.

### Chemical mystery

- Naive analysis: cadmium has r = 0.88 with malignancy and benzene only r = 0.385, so at face value cadmium appears to be the cause (chem_naive.png).
- Third variable: pollution_index is strongly correlated with both cadmium and malignancy (r = 0.90 with malignancy). I restricted the data to patients with pollution within +-5 of the median (49.5, n = 99) and recomputed the associations: cadmium drops to r = 0.00 (p = 0.997), while benzene stays strong at r = 0.652 (p = 2.6e-13) (chem_restricted.png). A partial correlation controlling for pollution gives the same result: cadmium 0.013 (p = 0.69), benzene 0.755 (p = 7e-185).
- Conclusion: benzene is the real cause of malignancy. Cadmium only looked guilty because pollution raises both cadmium and malignancy (confounding). Benzene's association became stronger after the control because the pollution-driven variation in malignancy was hiding it. Correlation alone did not identify the cause; comparing patients with similar pollution levels did.