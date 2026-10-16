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

## Batch 2 (2026-10-16): three patent-research datasets, published

Status: **published and confirmed 2026-10-16.** Merged in PR 3 (merge commit `c341793`). Cloud publisher run [38896605298](https://github.com/konstantinosStouras/datasets/actions/runs/38896605298) completed successfully. The live public feed (`catalog-public.json`) then showed **131 collections, 13 research entries**, all three IDs below with their paper titles and date added 2026-10-16, and no Zenodo, Dataverse, DOI, GitHub or OSF URLs in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `us-patent-text-keywords-novelty-measures` | Arts, Hou, Gomez, Research Policy 50(2), 104144 (2021), DOI 10.1016/j.respol.2020.104144 | [Zenodo 3515985](https://zenodo.org/records/3515985) is open, 20 files. Description and documentation PDF cite the paper and the code repository (exists). `patent_text_measures.zip` downloaded in full: MD5 matches Zenodo, 5,645,845 rows. Three more archives returned HTTP 206 with the ZIP signature. | Several files are many GB (up to about 46 GB), mostly not downloaded. Zenodo license label is cc-by-nc-1.0. PATSTAT-derived text may carry its own terms. Paper full text not read. |
| `in-text-patent-citation-database` | Bryan, Ozcan, Sampat, Research Policy 49(4), 103946 (2020), DOI 10.1016/j.respol.2020.103946 | [Harvard Dataverse ZEZWBX](https://doi.org/10.7910/DVN/ZEZWBX), CC0, one public 850 MB TSV. Whole file streamed: 2,408,583 rows, 26 columns, article years 1984 to 2016. Record names the authors and the user's guide. | Labelled beta 0.9 (Dataverse version 2.0, 2019). No patent grant-year column was seen in the header. Paper full text not read. |
| `us-patent-inventor-disambiguation` | Li et al., Research Policy 43(6), 941-955 (2014), DOI 10.1016/j.respol.2014.01.012 | [Harvard Dataverse 5F1RRI](https://doi.org/10.7910/DVN/5F1RRI), CC0, 64 public files. One 73 MB inventor table parsed: 337,483 rows, 31 columns, grant years 1975 to 2010. Documentation PDF read; it points to Dataverse and the code repository (exists). | Only one table sampled; other files listed, not downloaded. Statistical disambiguation, superseded for recent years by PatentsView (already listed). Paper full text not read. |

Queue rows for these three papers were set to the verified status in both CSVs. The catalog JSON has 13 datasets and 13 papers; the live total of 131 matched that expectation.

## Management Science leads checked 2026-10-16 (neither added)

- `10.1287/mnsc.2022.03905` (Wang and Wu, Management Science 72(1), 756-782, 2026): Crossref confirms identity. The INFORMS page and supplement returned HTTP 403 to automated requests, so the supplement could not be inspected. The arXiv version (2506.16334) says the startup data are matched to the Chinese Enterprise Database, which uses proprietary government sources. No public data found. Status: unresolved, likely restricted.
- `10.1287/mnsc.2024.06909` (Otis et al., Management Science, online 2026-07-10): Crossref confirms identity. The NBER working paper says the study was pre-registered on OSF but gives no data link; a public OSF title search found no matching project. The INFORMS supplement returned 403. Status: unresolved, no public study data found.

Neither 403 was bypassed. A person with a browser could open the supplements and report what they contain.

## Batch 3 (2026-10-16): three patent-research datasets published, one lead left unresolved

Status: **published and confirmed 2026-10-16.** Merged in PR 4 (merge commit `fe1235d`). Cloud publisher run [38897774771](https://github.com/konstantinosStouras/datasets/actions/runs/38897774771) completed successfully. The live public feed then showed **134 collections, 16 research entries**, all three IDs below with their paper titles and date added 2026-10-16, and no Zenodo, Dataverse, DOI, GitHub, OSF, Hugging Face or ScholarBank URLs in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `us-patent-text-similarity-pairs` | Arts, Cassiman, Gomez, Strategic Management Journal 39(1), 62-84 (online 2017-10-24), DOI 10.1002/smj.2699 | [Dataverse JO2DQZ](https://doi.org/10.7910/DVN/JO2DQZ), CC0, 13 public files, publication field names the paper. Range requests on three data files returned tab-separated patent pairs with scores; the description PDF was read. | Files are 0.1 to 2.5 GB, not downloaded. The PDF describes Java code but no code file is listed. Coverage 1976 to 2013 is the record's statement. Paper full text not read. This paper was missing from both queues; appended. |
| `patcit-patent-citations` | Verluise, Cristelli, Higham, de Rassenfosse, Strategic Management Journal 47(3), 678-698 (online 2025-10-22), DOI 10.1002/smj.70027 | Paper (accepted manuscript read from the LSE repository) says the in-text patent citation data are at Zenodo DOI 10.5281/zenodo.3710993. Zenodo is open, CC-BY-4.0, 9 files in the latest version 0.3.1. A 3 MB range of the in-text patent archive decoded to the schema and real data rows. | Which PatCit version matches the paper's 49.5 million citations is not verified (online appendix not read). Archives are gzip-wrapped. Underlying DOCDB/PATSTAT/Google Patents terms may apply. The Wiley page was blocked (403), so only the repository copy was read. |
| `us-inventor-ages-gender-death-dates` | Kaltenberg, Jaffe, Lachman, Research Policy 52(1), 104629 (2023), DOI 10.1016/j.respol.2022.104629 | Abstract states the data are public on Harvard Dataverse; [record YRLSKU](https://doi.org/10.7910/DVN/YRLSKU) is by the same authors, CC0, 23 public files. Age/gender table (2,408,326 rows, 1,858,516 inventors) and crosswalk (8,080,135 rows, grant years 1976-2018) streamed and parsed; README read. | Contains named individuals, residence city/state, estimated birth years and some death dates scraped from people-search sites: flagged prominently in the entry. Birth years run 1800 to 2013 in the file; heuristics, not verified facts. Paper full text not read. |

Queue rows: Arts et al. 2018 appended to both queues; the other two set to verified status.

### Unresolved lead from this pass

- `10.1002/smj.3001`, Png, "U.S. R&D, 1975-1998: A new dataset", Strategic Management Journal 40(5), 715-735 (2019). The abstract's data statement gives `five.dartmouth.edu/datasets` and DOI 10.25540/3wd8-dffw (the OSF link in the abstract is only the Open Practices badge page). The DOI resolves to NUS ScholarBank, a public record titled "U.S. R&D data (Cattell directories)", CC BY-NC 4.0, whose citation field names the paper and which lists .dta, .do, .docx and .zip file types. But anonymous API requests show no downloadable files in the original-files bundle, and the Dartmouth host returned HTTP 503. **Not added** because no actual file could be inspected. A person with a browser could check whether the files download. Dataset concerns noted by the author: facility-level R&D directories digitized from copyrighted print records.

### How this batch was found

Searched all abstracts in the cloned site database (269,424 unique DOIs across `lit/data` and `lit/data-ft50`) for repository words (Zenodo, Dataverse, OSF, GitHub, figshare, Dryad, DOI prefixes 10.5281, 10.7910, 10.17605) combined with innovation topic words: 77 hits, most from INFORMS Journal on Computing optimization code (off-topic, not reviewed). Hits that were relevant were checked by hand. Also checked repository search APIs by title; results are noisy. Abstract cues cover only part of the field: many papers state data locations only in the full text.

## Batch 4 (2026-10-16): three new datasets and one enriched collection

Status: committed through a pull request. **Publication is not confirmed until the workflow run and live feed are recorded here.**

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `open-source-write-access-novelty-survival` | Medappa, Srivastava, Favaron, Research Policy 54(8), 105284 (2025), DOI 10.1016/j.respol.2025.105284 | [DataverseNL VQC4OD](https://doi.org/10.34894/VQC4OD), 13 public files, record titled as replication data for the paper. Eight files downloaded and parsed: panel 45,418 rows (6,277 repositories), survival 6,563 rows, training 759 and test 190 rows, Stata code. | Semicolon-delimited. Code that built the data from GitHub is not in the deposit. License field says GNU GPL v3.0. Repository owner handles appear. Paper full text not read. |
| `wwii-us-patent-secrecy-orders` | Gross, Management Science 69(4), 2318-2338 (2023), DOI 10.1287/mnsc.2022.4457 | [Harvard Dataverse 6ZAJGK](https://doi.org/10.7910/DVN/6ZAJGK), CC BY-NC 4.0, two files, both downloaded: 8,475 records, 5 columns, filings 1932-1945, 6,353 with patent numbers. README read, names the paper. | Non-commercial license. Only 6,353 records link to granted patents. Paper full text not read. Found through DataCite; paper was missing from both queues. |
| `inventor-firm-innovation-replication-archive` | Bhaskarabhatla, Cabral, Hegde, Peeters, Management Science 67(6), 3899-3920 (2021), DOI 10.1287/mnsc.2020.3646 | [DataverseNL NLQTNC](https://doi.org/10.34894/NLQTNC) (the Erasmus DOI forwards here), CC-BY-4.0, 25 public files, 2.9 GB. README read in full. Small files parsed; largest Stata files returned 206 with the Stata signature. | README says some source files (full Compustat) cannot be shared. Contains inventor names with LinkedIn employment spells: personal-data note in the entry. Compustat-derived terms. Large files not downloaded. Also missing from the queues. |
| `national-health-and-nutrition-examination-survey-nhanes` (existing upstream entry, enriched) | Nicolaou, Patel, Wolfe, Management Science 64(4), 1825-1841 (2018), DOI 10.1287/mnsc.2016.2664 | Abstract names NHANES 2011-2012. Three CDC SAS transport files (TST_G, OCQ_G, DEMO_G) downloaded and parsed. | Only the 2011-2012 cycle files were checked. The paper's other data (Understanding Society Innovation Panel) are not covered. The CDC `Nchs/Nhanes/2011-2012/*.XPT` links return HTML 'not found' with status 200; the working path is `Nchs/Data/Nhanes/Public/2011/DataFiles/`. Date added is today because the original had none. |

The dry run of the publisher's own merge code (`mergeResearch`) before pushing gave 137 collections, 20 research entries, no duplicate IDs, NHANES enriched in place.

### Leads found in this pass and not added

- `10.1177/10422587221084249` (Block et al., Entrepreneurship Theory and Practice, family-firm innovation replication): DataCite lists SAGE-hosted supplement files (CSV, XLSX, R, DOCX), but the host answers automated requests with a Cloudflare challenge. Not verified, not bypassed.
- `10.1177/10422587251322409` (Replicating Davidsson and Honig, ETP 2025) and `10.1016/j.respol.2017.07.008` (CrowdBerkeley, Research Policy 2017): ICPSR records (PSED II, Kickstarter Data) list these papers, but this only shows a bibliography link, not use; ICPSR needs registration. The CrowdBerkeley paper presents three public databases whose download location was not found yet.
- Off-priority replication records found for Management Science: servitization bullwhip effect (DataverseNL `10.34894/oveyga`), return-insurance JD.com data (DataverseNL `10.34894/uxtgk8`), corporate environmental engagement (SMU RDR `10.25440/smu.17869031`), "Cancel the deal?" experiment (Dataverse `10.7910/DVN/TOYM2W`). Not reviewed because outside the priority topics; available for a later pass.

### Systematic discovery by DataCite

DataCite indexes Zenodo, Dataverse, Dryad, figshare, ICPSR and many institutional repositories. A quoted-DOI query finds deposits whose metadata mention a paper. Run over the 359 DOIs in the two queues: 20 had hits. A second sweep over 20,247 topic-matched FT50 papers (2006 onward; order: Management Science, M&SOM, POM, SMJ, Organization Science, Research Policy, others) runs in chunks; the first 1,000 (all Management Science) gave the Gross and Bhaskarabhatla et al. records. The sweep output is kept outside the repository; rerun with `_research/archive/datacite-sweep.py` after adding it if needed.

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
