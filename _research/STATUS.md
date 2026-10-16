# Current checkpoint — RESUMED 2026-10-16

The owner lifted the pause on 2026-10-16 (Europe/London). Work restarted from a cloud checkout; the handoff files, pending JSON and updated queues were retrieved from the owner's Dropbox copy of the local workspace (they were not in the remote repository).

## Resumption log

- Fast-forwarded to `main` commit `7cbabe2` (documentation checkpoint). No other remote data changes.
- Pending `research-additions.json` validated: 10 datasets, 10 papers, unique IDs, no dangling paper DOIs, 3 new IDs, no existing entry modified. Line endings normalized to LF.
- Independent re-check of source files on 2026-10-16: both Hugging Face files and both OSF files answer HTTP 206 on range requests; the OSF CSV re-downloaded in full (12,939,994 bytes, SHA-256 matches the value below, 16,527 rows, 156 columns).
- Queue CSV status updates (4 rows) installed in both queues.
- Publication and live-feed confirmation: see "Publication outcome" below once recorded. Sharing-deployment check: still to do.

## Publication outcome — confirmed 2026-10-16

The three additions and both updated queues were merged by the separate continuation session in PR #2, merge commit `0d785aa`. The original machine independently compared its pending JSON and CSV contents to that remote version: they match semantically (CSV BOM/line-ending differences only). The local checkout adopted the published version; there is no remaining local-only research batch.

Cloud publisher [38894715168](https://github.com/konstantinosStouras/datasets/actions/runs/38894715168) completed successfully. An unauthenticated fetch of the live public feed confirmed **128 collections, 10 research entries**, all three new IDs, and no source URLs in the sanitized JSON. The research catalog contains 10 distinct cited papers.

Website sharing deployment [38893493361](https://github.com/konstantinosStouras/konstantinosStouras.github.io/actions/runs/38893493361) succeeded. Live requests using Facebook, LinkedIn and Twitter crawler user agents returned HTTP 200 with the new sharing title and icon markup. The preview JPEG, favicon, Apple touch icon and manifest also returned HTTP 200 with appropriate content types. These are HTTP checks, not actual in-app preview tests.

A separate offline check run [38893493750](https://github.com/konstantinosStouras/konstantinosStouras.github.io/actions/runs/38893493750) failed the Firebase deployment guard check: `datasets/_backend` lacks a `.firebaserc` naming its project. This did not prevent GitHub Pages deployment. Repair and verify the repository-required project guard before any future Firebase rules deployment; do not claim all site checks passed. No rules were changed during this synchronization.

The owner then requested that all relevant local work be saved on GitHub. Historical helpers and evidence have been added under `_research/archive/` and `_research/evidence/`, and the handoff documents now point to repository files. Abstract snippets were omitted from the discovery snapshot. Duplicate local exports are superseded; unrelated computer-recovery/session artifacts do not belong in this public research repository.

This synchronization pass does not restart new research in the original paused conversation. A separate continuation session had already recorded its own resumption above; preserve that history without interpreting it as authorization for unrelated work.

## State at the earlier pause (historical)

- Dataset fork checkout: `C:/Users/LENOVO/Dropbox/Others/GitHub/datasets`, branch `main`, last local committed checkpoint `2c9ee34` (review queues). Inspect current status/remotes before continuing; remote scheduled jobs can advance independently.
- Three newly verified dataset additions are saved in the local `research-additions.json` but **not committed or pushed**. The local file now contains 10 research entries and 10 distinct cited papers. The last confirmed live catalog had 125 total collections, 7 research entries and 8 cited papers. The expected merged count after the three additions is 128, but this batch's merge/publication still needs validation.
- After the pause, the owner explicitly authorized a documentation-only commit and push: root `AGENTS.md` plus `_research/HANDOFF.md`, `METHODS.md`, `STATUS.md`, and `README.md`. This documentation commit contains no dataset JSON or CSV queue changes. The three pending additions and both queue updates remain local and unpublished. A fresh remote clone therefore contains the handoff evidence but not the pending JSON records; obtain those local changes or reconstruct them from the documented evidence and revalidate after the owner resumes work.
- Website sharing changes were committed and pushed to site `master` as `40aa3b75e6f1cfb3da1ee3192fc23abb6e1f8b5b`. GitHub Pages run [38893493361](https://github.com/konstantinosStouras/konstantinosStouras.github.io/actions/runs/38893493361) was still in progress at the last check. Offline checks run 38893493750 was also in progress. **Live deployment has not yet been confirmed.** The already-started cloud deployment may finish during the pause.
- Site working checkout: `C:/Users/LENOVO/Dropbox/Others/GitHub/dataset-publish-work`, branch `codex/dataset-publish`. Sharing edits include complete static social tags, DataCatalog JSON-LD, favicon sizes 16/32/48, Apple touch icon, 192/512 icons and a web manifest. Existing 1200 × 630 branded JPEG retained. Nine catalog/membership tests passed; ad hoc checks confirmed image dimensions, 45,838-byte size, canonical agreement and icon paths. Icon visually inspected. No actual WhatsApp/Facebook/LinkedIn app preview tested; live crawler checks remain pending.

## Three additions now published (verification record)

All three have dateAdded and verifiedAt `2026-10-16` with tags, citations and caveats in the authoritative JSON.

| Dataset ID | Evidence and actual file check | Limits |
| --- | --- | --- |
| `british-historical-patent-texts` | [Author dataset](https://huggingface.co/datasets/matthewleechen/300YearsOfBritishPatents). Actual `all_patents.jsonl.gz` range request returned HTTP 206, read 131,072 bytes, gzip signature `1f8b`; first JSONL record successfully decoded (GB161700005A, 1617, six text pages). | About 1.77 GB; full archive not downloaded. Metadata says CC-BY-4.0 but README license section says CC BY-SA 4.0; conflicting terms explicitly disclosed. |
| `british-patent-breakthrough-scores` | [Separate score release](https://huggingface.co/datasets/matthewleechen/300YearsOfBritishPatents_KPST). Complete `breakthrough_scores_fh10_bh5_maxdf100.csv` returned HTTP 200; 9,628,241 bytes, 193,563 rows, five columns, observed years 1739–1889. | Other files use other horizons. Same conflicting license statements. Do not use 1617 as this checked file's start year. |
| `kickstarter-visual-features-crowdfunding` | [OSF project](https://osf.io/ujnzp/) linked by the publisher. Actual [CSV](https://osf.io/download/ky98j/) returned HTTP 200, 12,939,994 bytes, parsed 16,527 rows × 156 columns including row index. [R script](https://osf.io/download/ubw8m/) returned HTTP 200 and explicitly reads `fileforresearchbox.csv`. | Processed features, not a verified complete image archive. OSF metadata specifies no license. Coverage years and full geography not yet established; left unspecified. Results not replicated. |

Patent releases cite **300 years of British patents**, Enrico Berkes; Matthew Lee Chen; Matteo Tranchero, Research Policy 55(1), 105347 (2026), online 2025-10-24, DOI [10.1016/j.respol.2025.105347](https://doi.org/10.1016/j.respol.2025.105347). Author-hosted published PDF confirms the resources and explicitly links the score release in footnote 15; Crossref independently confirms bibliographic fields. The two releases represent different data products, not duplicate text collections.

Crowdfunding data cites **Extraction of visual information to predict crowdfunding success**, Simon J. Blanchard; Theodore J. Noseworthy; Ethan Pancer; Maxwell Poole, Production and Operations Management 32(12), 4172–4189 (2023), DOI [10.1111/poms.14083](https://doi.org/10.1111/poms.14083). Publisher and Crossref verified. CSV SHA-256: `fb1c9ea173851819bc8ef9cb098e7ff2f79b374eb0764e2c81244bf3573b106f`.

OSF discovery detail: native `osfstorage` is empty, but the public project has connected Dropbox folders. Query `/v2/nodes/ujnzp/files/` then its `dropbox` relationship. Analysis data is in `3-Analysis Codes (R)`; there is also literature-review data and image-extraction code. An empty native-storage response does not mean no public files exist. CSV parsing needs universal/newline-aware handling (`io.StringIO(text, newline='')`), because initial default parsing rejected its line endings.

## Prior confirmed live research entries

NBER Patent Data Project; PatentsView; USPTO Trademark Case Files; Business Dynamics Statistics (existing collection enriched, not a new duplicate); author-shared firm technology position/differentiation data; DISCERN historical patent–firm matches; Dell product life-cycle orders. Exact metadata, citations, access conditions and check descriptions are in JSON. Important caveats: BDS is only a public figure component of a restricted-data paper; Dell is a documented public reuse copy with no stated license; DISCERN's commercial underlying inputs remain restricted.

Last confirmed successful cloud catalog run before this pause: [38892242758](https://github.com/konstantinosStouras/datasets/actions/runs/38892242758). It published the prior seven research entries. The site bundled fallback has fewer research entries than the live feed; refresh it deliberately when needed, never use it to overwrite the newer fork.

## Review coverage and unresolved leads

Initial exploratory metadata scan: 102,778 unique DOI records in metadata years 2006–2026; 11,253 broad topic matches; 355 with availability cues. Title-focused subset: 125. Three manually verified missed papers were appended, yielding 358 broad and 128 priority queue rows. These counts describe a heuristic scan, not completed FT50 coverage. Neither boundary dates nor journal completeness has been fully audited.

Both queues now mark the British-patents and crowdfunding papers as having a verified public component. They also mark these Management Science leads as under review:

- **Artificial Intelligence, Lean Startup Method, and Product Innovations**, DOI `10.1287/mnsc.2022.03905`: publisher identity and availability statement checked; actual supplement files not verified. No dataset added from this lead.
- **The Uneven Impact of Generative Artificial Intelligence on Entrepreneurial Performance: Evidence from a Field Experiment in Kenya**, DOI `10.1287/mnsc.2024.06909`: publisher full text and availability statement checked; actual supplement files not verified. No dataset added from this lead.

Do not count these unresolved leads as unavailable or as published additions.

## Next steps for an authorized continuation

1. Clone or pull the current repository and read AGENTS, HANDOFF, METHODS and this checkpoint. No local pending catalog or queue files need to be retrieved from the original machine.
2. Inspect current workflow/feed state if making further changes; the ten research entries and the sharing deployment above are already confirmed. Do not duplicate the three additions.
3. Before any Firebase rules deployment, repair the missing project configuration and deployment guard reported above, following the website repository instructions. This remains unfinished and was not part of the file-publication request.
4. When the user authorizes further research in the relevant session, continue Management Science/M&SOM/POM priority leads, then other FT50 journals. The full twenty-year review remains outstanding.
5. Keep documentation current and preserve dated evidence, unresolved leads and actual deployment outcomes. Read the archive warning before reusing historical scripts.
