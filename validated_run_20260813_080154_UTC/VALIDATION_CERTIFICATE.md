# SPARC frozen validation reproduction certificate

## Result

Overall validation status: PASS
Field-response metrics reproduced exactly: True
Reconstructed observed-acceleration metrics reproduced exactly: True

## Scope

This notebook re-executes the frozen SPARC kernel-variant nested-validation
design from archived derived inputs, archived kernel features, frozen outer
fold assignments, frozen model specifications, and frozen Ridge parameters.

The official SPARC raw archive is not redistributed by this release.

## Numerical criterion

A metric is treated as exact when the absolute difference from the locked
reference is below 1e-10. Observed residual differences of order 1e-16 are
standard floating-point rounding effects.

## Field-response comparison

| sample   | kernel_variant           |   n_rows_reconstructed |   n_galaxies_reconstructed |   reconstructed_field_rmse |   reconstructed_field_r2 |   n_rows_locked |   n_galaxies_locked |   field_rmse |   field_r2 |   rmse_difference |   r2_difference | field_metrics_exact   |
|:---------|:-------------------------|-----------------------:|---------------------------:|---------------------------:|-------------------------:|----------------:|--------------------:|-------------:|-----------:|------------------:|----------------:|:----------------------|
| Q1       | abs_leave_one_out        |                   1859 |                         99 |                   0.316181 |                 0.383767 |            1859 |                  99 |     0.316181 |   0.383767 |       0           |     0           | True                  |
| Q1       | abs_self_dlnr            |                   1859 |                         99 |                   0.314117 |                 0.391784 |            1859 |                  99 |     0.314117 |   0.391784 |       5.55112e-17 |     5.55112e-17 | True                  |
| Q1       | current_abs_self_uniform |                   1859 |                         99 |                   0.313284 |                 0.395006 |            1859 |                  99 |     0.313284 |   0.395006 |       0           |     0           | True                  |
| Q1       | signed_self_uniform      |                   1859 |                         99 |                   0.313228 |                 0.395225 |            1859 |                  99 |     0.313228 |   0.395225 |       5.55112e-17 |     5.55112e-17 | True                  |
| Q12      | abs_leave_one_out        |                   2805 |                        163 |                   0.336814 |                 0.421937 |            2805 |                 163 |     0.336814 |   0.421937 |       5.55112e-17 |     0           | True                  |
| Q12      | abs_self_dlnr            |                   2805 |                        163 |                   0.335313 |                 0.427077 |            2805 |                 163 |     0.335313 |   0.427077 |       5.55112e-17 |     0           | True                  |
| Q12      | current_abs_self_uniform |                   2805 |                        163 |                   0.335103 |                 0.427794 |            2805 |                 163 |     0.335103 |   0.427794 |       5.55112e-17 |     5.55112e-17 | True                  |
| Q12      | signed_self_uniform      |                   2805 |                        163 |                   0.335055 |                 0.427956 |            2805 |                 163 |     0.335055 |   0.427956 |       5.55112e-17 |     0           | True                  |
| Q123     | abs_leave_one_out        |                   2896 |                        175 |                   0.359918 |                 0.407846 |            2896 |                 175 |     0.359918 |   0.407846 |       5.55112e-17 |     0           | True                  |
| Q123     | abs_self_dlnr            |                   2896 |                        175 |                   0.358593 |                 0.412197 |            2896 |                 175 |     0.358593 |   0.412197 |       0           |     0           | True                  |
| Q123     | current_abs_self_uniform |                   2896 |                        175 |                   0.358758 |                 0.411656 |            2896 |                 175 |     0.358758 |   0.411656 |       0           |     0           | True                  |
| Q123     | signed_self_uniform      |                   2896 |                        175 |                   0.35863  |                 0.412074 |            2896 |                 175 |     0.35863  |   0.412074 |       5.55112e-17 |     5.55112e-17 | True                  |

## Reconstructed observed-acceleration comparison

| sample   | kernel_variant           |   n_rows |   reconstructed_gobs_rmse |   reconstructed_gobs_r2 |   gobs_rmse |   gobs_r2 |   gobs_rmse_difference |   gobs_r2_difference | gobs_metrics_exact   |
|:---------|:-------------------------|---------:|--------------------------:|------------------------:|------------:|----------:|-----------------------:|---------------------:|:---------------------|
| Q1       | abs_leave_one_out        |     1859 |                  0.147835 |                0.904134 |    0.147835 |  0.904134 |            2.77556e-17 |          0           | True                 |
| Q1       | abs_self_dlnr            |     1859 |                  0.145679 |                0.906911 |    0.145679 |  0.906911 |            8.32667e-17 |          0           | True                 |
| Q1       | current_abs_self_uniform |     1859 |                  0.145441 |                0.907215 |    0.145441 |  0.907215 |            5.55112e-17 |         -2.22045e-16 | True                 |
| Q1       | signed_self_uniform      |     1859 |                  0.145289 |                0.907407 |    0.145289 |  0.907407 |            5.55112e-17 |          0           | True                 |
| Q12      | abs_leave_one_out        |     2805 |                  0.163695 |                0.903169 |    0.163695 |  0.903169 |            5.55112e-17 |         -2.22045e-16 | True                 |
| Q12      | abs_self_dlnr            |     2805 |                  0.161697 |                0.905518 |    0.161697 |  0.905518 |            0           |          0           | True                 |
| Q12      | current_abs_self_uniform |     2805 |                  0.161875 |                0.90531  |    0.161875 |  0.90531  |            5.55112e-17 |          0           | True                 |
| Q12      | signed_self_uniform      |     2805 |                  0.161863 |                0.905325 |    0.161863 |  0.905325 |            0           |          0           | True                 |
| Q123     | abs_leave_one_out        |     2896 |                  0.174639 |                0.893003 |    0.174639 |  0.893003 |            5.55112e-17 |          0           | True                 |
| Q123     | abs_self_dlnr            |     2896 |                  0.172467 |                0.895648 |    0.172467 |  0.895648 |            5.55112e-17 |          0           | True                 |
| Q123     | current_abs_self_uniform |     2896 |                  0.173075 |                0.894911 |    0.173075 |  0.894911 |            8.32667e-17 |          0           | True                 |
| Q123     | signed_self_uniform      |     2896 |                  0.172918 |                0.895102 |    0.172918 |  0.895102 |            1.11022e-16 |          0           | True                 |

## Execution environment

- Python: 3.12.13
- numpy: 2.0.2
- pandas: 2.2.2
- scikit-learn: 1.6.1
