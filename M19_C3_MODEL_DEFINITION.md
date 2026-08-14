# M19/C3 model-comparison supplement

This document accompanies `M19_C3_Model_Comparison_Reproduction.ipynb`. It is
separate from the certified frozen-validation master notebook and does not
change that release's inputs, out-of-fold outputs, figures, or certificate.

## Scope

The M19/C3 results are an internal, galaxy-separated out-of-fold comparison on
previously analysed SPARC data. The C3 choice was post-selection motivated.
Accordingly, the comparison is explanatory and does not constitute an external
prospective validation, a global model search, or a fundamental field equation.

## Code-defined M19 reference model

The audited reference model is named
`M19_full_free_q_saturated_gradient` in Stage 6T45. For baryonic acceleration
\(g_{\mathrm{bar}}(r)\), its nonlocal source and response are

\[
g_{\mathrm{cum}}(r)=\frac{2}{r^2}\int_0^r r' g_{\mathrm{bar}}(r')\,dr',
\qquad
\omega(r)=g_{\mathrm{bar}}(r)^{1-\eta}g_{\mathrm{cum}}(r)^\eta,
\]

\[
s_q(r)=g_{\mathrm{ref}}\left(\frac{\omega(r)}{g_{\mathrm{ref}}}\right)^q,
\qquad
\Delta g_{\mathrm{M19}}(r)=A g_{\max}
\tanh\!\left(\frac{s_q(r)}{g_{\max}}\right),
\]

\[
g_{\mathrm{pred}}^{\mathrm{M19}}(r)=g_{\mathrm{bar}}(r)+
\Delta g_{\mathrm{M19}}(r)+\lambda\frac{d}{dr}
\left[r\Delta g_{\mathrm{M19}}(r)\right].
\]

The six fitted parameters are \(A\), \(g_{\mathrm{ref}}\),
\(g_{\max}\), \(\eta\), \(q\), and \(\lambda\).

## C3 specialization and exact mapping

The audited compact comparison is called
`C3_joint_q05_linear_gradient`. It retains the nonlocal source and gradient,
fixes \(q=0.5\), and removes the saturation. Thus

\[
\Delta g_{\mathrm{C3}}(r)=K\sqrt{\omega(r)},
\qquad
g_{\mathrm{pred}}^{\mathrm{C3}}(r)=g_{\mathrm{bar}}(r)+
\Delta g_{\mathrm{C3}}(r)+\lambda\frac{d}{dr}
\left[r\Delta g_{\mathrm{C3}}(r)\right].
\]

The earlier linear C3 notation \(A g_{\mathrm{ref}}
\sqrt{\omega/g_{\mathrm{ref}}}\) is algebraically identical when
\(K=A\sqrt{g_{\mathrm{ref}}}\). This exact identity applies only to the
linear, fixed-\(q=0.5\) C3 parameterizations. It does not make C3 equivalent to
the full M19 reference model, which retains free \(q\) and saturation.

## Repository relation

Keep the existing frozen-validation notebook unchanged. Add this notebook and
document as a separate model-comparison supplement, then publish a new version
of the existing Zenodo record if the repository release is updated.
