# SPARC frozen validation reproduction

## Purpose

This repository contains the frozen empirical SPARC validation path. The
included Colab notebook re-executes the archived kernel-variant
nested-validation design from derived inputs, fixed galaxy-separated folds,
frozen model specifications, and frozen Ridge parameters.

The notebook verifies the numerical result against the locked reference
metrics rather than training or tuning a new model.

## One-cell master notebook

Open `code/SPARC_Frozen_Validation_Reproduction.ipynb` in Google Colab and
run its single code cell. It performs the complete reproducibility workflow:

- verifies the integrity of the archived inputs;
- re-executes all 60 frozen outer-fold fits;
- reconstructs 30,240 out-of-fold prediction records;
- compares field-response and reconstructed observed-acceleration metrics
  against the locked reference, using an absolute tolerance of 1e-10;
- prepares the certified Q12 figure source tables;
- generates the two publication figures with English labels and captions;
- writes `VALIDATION_CERTIFICATE.md`, `validation_summary.json`, and
  `SHA256SUMS.txt`;
- creates a portable ZIP archive of the certified run, including the figures.

The Colab cell writes a new, timestamped run below
`public_colab_runs/frozen_validation_<UTC timestamp>/`; it does not modify
the frozen inputs or locked reference files.

## Figures produced by the master notebook

- `figures/figure_candidate_h_representative_galaxy_rotation_curves_compact_labels.png`  
  Four deterministic Q12 representative galaxy rotation curves. Black points
  are observations, gold is the baryonic rotation curve, blue is the median
  frozen OOF reconstruction, and the pale-blue band is the actual spread
  across the four frozen variants.

- `figures/figure_2_oof_residual_phase_map.png`  
  Q12 out-of-fold residual structure across the baryonic-versus-observed
  acceleration plane. Each coloured hexagon reports the median residual of
  at least five prediction records.

Each figure is accompanied by its exact source table, English caption, and
JSON integrity manifest.

## Running the release

1. Extract this release in Google Drive.
2. Open `code/SPARC_Frozen_Validation_Reproduction.ipynb` in Colab.
3. In the configuration block at the top of the cell, set `RELEASE_ROOT`
   to the extracted release directory.
4. Run the single cell.
5. Confirm that the final output reports:

   ```
   === FROZEN VALIDATION CERTIFIED ===
   Overall status: PASS
   Field metrics exact: True
   g_obs metrics exact: True
   ```

6. Retain the timestamped run directory and its
   `_with_figures.zip` archive as the reproducibility record.

## Independent release verification

Before running Colab, verify the archived release contents:

```bash
python verify_release.py
```

Expected result: `STATUS: PASS`.

## Scope and data boundary

This release is limited to the empirical SPARC frozen-validation path. It
does not contain Bullet Cluster, core-cusp, H I, WISE, spectral, or wider
UQSH-theory analyses.

Original SPARC raw files are not redistributed. Their SHA-256 source locks
are recorded in `release_manifest.json`.
