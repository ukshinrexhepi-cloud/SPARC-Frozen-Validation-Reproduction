# SPARC frozen validation reproduction

## Result

The included Colab re-executes the frozen SPARC kernel-variant
nested-validation design from archived derived inputs, fixed folds,
model specifications, and Ridge parameters.

The validated run reproduces all field-response and reconstructed
observed-acceleration metrics to floating-point precision.

## Run

1. Extract this release into Google Drive.
2. Open `code/SPARC_Frozen_Validation_Reproduction.ipynb` in Colab.
3. In Cell 1, set `RELEASE_ROOT` to the extracted release folder.
4. Run all cells from top to bottom.
5. The final cell must report `Overall status: PASS`.

## Scope

This release is limited to the empirical SPARC frozen-validation path.
It excludes Bullet Cluster, Core-Cusp, H-I, WISE, spectral analyses,
and wider UQSH theory materials.

## Data boundary

Original SPARC raw files are not redistributed. Their SHA-256 source
locks are recorded in `release_manifest.json`.

## Integrity

Run `python verify_release.py` after extraction.
Expected result: `STATUS: PASS`.
