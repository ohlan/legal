# Pista policies

Source for the GitHub Pages site with Pista's legal pages.

- [Pista Privacy Policy](./pista/)
- [Pista Terms of Service](./pista/terms/)

The texts are copied from the app repo (`PennyTrail/docs/PRIVACY_POLICY.md` and
`docs/TERMS_OF_SERVICE.md`), which is the source of truth:

```bash
python3 tools/sync_from_app.py ../PennyTrail/docs
```

Design: `_layouts/policy.html`, `assets/pista.css`, `assets/pista.js`. `penny-trail/` only
redirects old links (used by app version 1.0.1 and earlier) to `pista/`.
