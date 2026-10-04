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

**What the data showed:** The observed counts decrease over time, [məsələn: quickly at the beginning and more slowly later, with small random scatter].

**Match with the analytical law:** [Öz qərarın. Məsələn: Yes, the observed points follow the same exponential shape as N0*exp(-0.3 t), with only small deviations, so the data agree with the law.]

**Snakemake pipeline:** The Snakefile has one rule that builds figure.png from decay_observed.csv by running plot.py, and Snakemake only reruns it when its input has changed.