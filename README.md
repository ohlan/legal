# App policies

GitHub Pages site with the privacy policies and terms of service for TranscenD apps.
Each app has its own folder:

| App | Privacy policy | Terms of service |
|---|---|---|
| Pista | [pista/privacy/](./pista/privacy/) | [pista/terms/](./pista/terms/) |

## Layout

- `_data/apps.yml` — one entry per app: name, icon, contact, hero colours.
- `_layouts/policy.html`, `assets/site.css`, `assets/site.js` — shared design (light/dark,
  contents sidebar, section cards). Pages pick their app with `app: <key>` in front matter.
- `index.md` — site root listing every app (add a card per app).
- `<app>/index.md` — the app's hub; `<app>/privacy/` and `<app>/terms/` — the documents.

## Updating Pista's texts

The app repo is the source of truth (`PennyTrail/docs/PRIVACY_POLICY.md`,
`docs/TERMS_OF_SERVICE.md`):

```bash
python3 tools/sync_from_app.py ../PennyTrail/docs
```

## Adding an app

1. Add its entry to `_data/apps.yml` and its icon to `assets/apps/`.
2. Create `<app>/index.md`, `<app>/privacy/index.md`, `<app>/terms/index.md` with
   `app: <key>`, `nav: privacy|terms` and `root: "../../"` (hub: `root: "../"`).
3. Add a card to `index.md`.
