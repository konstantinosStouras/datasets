# Current checkpoint — RESUMED 2026-10-16

The owner lifted the pause on 2026-10-16 (Europe/London). Work restarted from a cloud checkout; the handoff files, pending JSON and updated queues were retrieved from the owner's Dropbox copy of the local workspace (they were not in the remote repository).

## Live progress log (newest first; updated as work proceeds)

Times are UTC on 2026-10-16, taken from GitHub workflow run timestamps or the container clock. (An earlier version of this log used estimated times; they have been replaced with these observed ones.)

- 17:48 Batch 16 live (run 38939877345, 17:28:21; 186 entries).
- 17:40 Batch 15 live (run 38939563044, 17:25:37; 185 entries). Batch 16 (Brazilian hospital panel) submitted. Metadata fetch for the remaining Dataverse and Zenodo sweep leads running.
- 17:30 FT50-wide sweep finished (113,511 papers; 750 clean leads). Batch 15 submitted: AIOE, Twin-2K-500, scientific complexity, OM-OR conference survey, EHR event logs, MLB managers, IRI category survey. Session worker restarted once during this stretch; files and results survived.
- 15:12 Batch 14 live (run 38920471271, 15:01:20; 178 entries). REStud Zenodo community (544 records) matched and scored; ten mid-sized packages downloaded and listed, four large ones listed by reading the zip directory with range requests.
- 15:05 Batch 14 submitted: six QJE and JPE deposits (patent applications 1998-2003, French industrialization panels, inventor migration database, federal R&D funding tables, Chinese AI firms, automation patent panels). Sweep at about 18,000 of 113,511 with 458 hits.
- 14:40 FT50-wide DataCite batch sweep started (113,511 papers from 1996 on); QJE, JPE, REStud and Econometric Society replication archives listed. Owner: no experiments category, focus on 1996 on, prefer reusable datasets.
- 14:12 Batch 13 live (run 38913236095, 14:07:51; 172 entries).
- 14:10 Batch 13 submitted: three Management Science deposits (Guzman and Li founding strategy; Gong and Png automation; Roach and Sauermann startup hiring) found by matching the site's Management Science paper list against Dataverse search results. Six other Management Science leads logged and not added.
- 13:35 DataCite sweep complete (21 of 21). Bloom and Van Reenen management practices data added (found in chunk 19) and live (run 38906891938, 13:19:05; 169 entries). `research-additions.json` now holds 52 datasets and 79 papers.
- 13:25 Batch 12 KPSS entry live (run 38905816430, 13:10:38). Two more QJE deposits (Bell et al., Kline et al.) live too (run 38906120243, 13:13:08; 168 entries). Sweep chunks 18 and 19 of 21 reviewed or in progress. Batch 11 confirmed live (run 38905315190, 13:06:36). DataCite sweep: 18 of 21 chunks done.
- 12:15 Batch 5 live (CrowdBerkeley Kickstarter database; run 38899203737 succeeded at 12:15:15). `main`'s `catalog-public.json` then showed 138 collections, 21 research entries, no URLs. The raw.githubusercontent.com copy lagged for a few minutes behind `main`, so I checked the file in git.
- 12:12 Batch 4 live: open source write-access data, WWII patent secrecy orders, inventor-firm replication archive, NHANES enrichment (run 38898838401).
- 12:02 Batch 3 live: patent text similarity, PatCit, inventor ages (run 38897774771). Png R&D directory data left unresolved (no downloadable file visible).
- 11:52 Batch 2 live: patent text and novelty measures, in-text patent citations, inventor disambiguation (run 38896605298).
- 11:35 Batch 1 live: the three pending items from the pause (run 38894715168). Website sharing update confirmed live earlier in the session (HTML, image, icons; crawler user agents return 200).
- 12:22 Batch 6 submitted: ride-hail deskilling experiments (SMJ) and three named public datasets found through the abstract scan (PSED, Kauffman Firm Survey, World Bank Enterprise Surveys). SBIR.gov blocked.
- 12:30 Batch 6 confirmed live (run 38900143266 at 12:23:29: 142 collections, 25 research entries). Batch 7 submitted: five patent and entrepreneurship replication deposits found in sweep chunks 4 to 6 (Marx and Fuegi, SBIR/DoD, disruptive patents, topology of technology space, AngelList social vision).
- 12:35 Batch 7 confirmed live (run 38901007519 at 12:30:56: 147 collections, 30 research entries). Batch 8 submitted: Mannheim Innovation Panel (application-gated) and six open Research Policy deposits from sweep chunks 6 and 7.
- 12:42 Batch 8 confirmed live (run 38901669227 at 12:36:30: 154 collections, 37 research entries; raw feed caught up). Batch 9 submitted: Community Innovation Survey (Eurostat tables) and Global Entrepreneurship Monitor.
- 12:51 Batch 9 confirmed live (run 38902467271 at 12:43:11: 156 collections, 39 research entries). Batch 10 submitted: NBER Orange Book, ClinicalTrials.gov, World Bank FAT survey (found through the abstract scan and sweep chunks 9 to 12).
- 12:56 Batch 10 confirmed live (run 38903631072 at 12:52:56: 159 collections, 42 research entries). Added a 'Known blockers' section. AER deposits on openICPSR are blocked like ICPSR; QJE deposits on Dataverse are often README-only or code-only.
- 13:05 Batch 10 confirmed live earlier; batch 11 submitted: six replication deposits (RFS, QJE x2, JPE, JFE, JIBS) from sweep chunks 13 and 14.
- Running: DataCite sweep of 20,247 topic-matched FT50 papers in 21 chunks of 1,000, started 12:06, about 3 minutes per chunk (17 of 21 done at 13:05; chunks now reach AER, QJE, JPE, marketing and finance journals). Two failed requests so far (proxy drops); failed DOIs are rerun at the end. Next: vet hits from each finished chunk by hand, add verified ones, publish, record each batch here.
- Unresolved and blocked by publisher bot challenges (not bypassed): INFORMS supplements (two Management Science leads), Wiley, SAGE.

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

## Known blockers: hosts that cannot be checked by script

These hosts answer scripted requests with a bot challenge, a 403 or an empty file list. Nothing was bypassed. Papers whose data sit only on these hosts stay 'unresolved', not 'no public data'. A person with a browser could open them and report what they hold.

| Host | Effect on coverage |
| --- | --- |
| INFORMS (pubsonline.informs.org) | Management Science, M&SOM, Organization Science, ISR and Information Systems Research supplements. This is the main reason priority journals Management Science, M&SOM and POM yield few additions: most of their shared data sit in INFORMS-hosted supplements. |
| Wiley, SAGE (journal sites and SAGE figshare) | Supplements of SMJ, POM, ETP, JOM and similar journals. |
| ICPSR and openICPSR | Study pages and downloads; AER, PSED, GEM (ICPSR copy), MIDUS and other deposits cannot be opened. DataCite metadata still confirms they exist. |
| SBIR.gov | Official SBIR/STTR award data and API. |
| Bielefeld University repository | Data publications behind an anti-bot page. |
| NUS ScholarBank | Records show no files to anonymous requests. |
| SharePoint and Dropbox links | Used by some QJE deposits; not stable repositories and not verified. |

Hosts that work well: Zenodo, Harvard Dataverse and DataverseNL, Mendeley Data, OSF, Hugging Face, GitHub (git), Dryad, institutional DSpace APIs, Eurostat, the World Bank Microdata Library catalog API, NBER, Kauffman, GEM and ClinicalTrials.gov.

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

## Batch 4 (2026-10-16): three new datasets and one enriched collection, published

Status: **published and confirmed 2026-10-16.** Merged in PR 5 (merge commit `27585c2`). Cloud publisher run [38898838401](https://github.com/konstantinosStouras/datasets/actions/runs/38898838401) completed successfully. The live public feed then showed **137 collections, 20 research entries**, all four IDs below with their paper titles and date added 2026-10-16 (NHANES enriched in place, only one NHANES entry), and no URLs of any kind in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `open-source-write-access-novelty-survival` | Medappa, Srivastava, Favaron, Research Policy 54(8), 105284 (2025), DOI 10.1016/j.respol.2025.105284 | [DataverseNL VQC4OD](https://doi.org/10.34894/VQC4OD), 13 public files, record titled as replication data for the paper. Eight files downloaded and parsed: panel 45,418 rows (6,277 repositories), survival 6,563 rows, training 759 and test 190 rows, Stata code. | Semicolon-delimited. Code that built the data from GitHub is not in the deposit. License field says GNU GPL v3.0. Repository owner handles appear. Paper full text not read. |
| `wwii-us-patent-secrecy-orders` | Gross, Management Science 69(4), 2318-2338 (2023), DOI 10.1287/mnsc.2022.4457 | [Harvard Dataverse 6ZAJGK](https://doi.org/10.7910/DVN/6ZAJGK), CC BY-NC 4.0, two files, both downloaded: 8,475 records, 5 columns, filings 1932-1945, 6,353 with patent numbers. README read, names the paper. | Non-commercial license. Only 6,353 records link to granted patents. Paper full text not read. Found through DataCite; paper was missing from both queues. |
| `inventor-firm-innovation-replication-archive` | Bhaskarabhatla, Cabral, Hegde, Peeters, Management Science 67(6), 3899-3920 (2021), DOI 10.1287/mnsc.2020.3646 | [DataverseNL NLQTNC](https://doi.org/10.34894/NLQTNC) (the Erasmus DOI forwards here), CC-BY-4.0, 25 public files, 2.9 GB. README read in full. Small files parsed; largest Stata files returned 206 with the Stata signature. | README says some source files (full Compustat) cannot be shared. Contains inventor names with LinkedIn employment spells: personal-data note in the entry. Compustat-derived terms. Large files not downloaded. Also missing from the queues. |
| `national-health-and-nutrition-examination-survey-nhanes` (existing upstream entry, enriched) | Nicolaou, Patel, Wolfe, Management Science 64(4), 1825-1841 (2018), DOI 10.1287/mnsc.2016.2664 | Abstract names NHANES 2011-2012. Three CDC SAS transport files (TST_G, OCQ_G, DEMO_G) downloaded and parsed. | Only the 2011-2012 cycle files were checked. The paper's other data (Understanding Society Innovation Panel) are not covered. The CDC `Nchs/Nhanes/2011-2012/*.XPT` links return HTML 'not found' with status 200; the working path is `Nchs/Data/Nhanes/Public/2011/DataFiles/`. Date added is today because the original had none. |

The dry run of the publisher's own merge code (`mergeResearch`) before pushing gave 137 collections, 20 research entries, no duplicate IDs, NHANES enriched in place.

### Leads found in this pass and not added

- `10.1177/10422587221084249` (Block et al., Entrepreneurship Theory and Practice, family-firm innovation replication): DataCite lists SAGE-hosted supplement files (CSV, XLSX, R, DOCX), but the host answers automated requests with a Cloudflare challenge. Not verified, not bypassed.
- `10.1177/10422587251322409` (Replicating Davidsson and Honig, ETP 2025): an ICPSR record (PSED II) lists the paper, but this only shows a bibliography link, not use; ICPSR needs registration. Unresolved. (The CrowdBerkeley paper, Research Policy 2017, was resolved afterwards: see Batch 5.)
- Off-priority replication records found for Management Science: servitization bullwhip effect (DataverseNL `10.34894/oveyga`), return-insurance JD.com data (DataverseNL `10.34894/uxtgk8`), corporate environmental engagement (SMU RDR `10.25440/smu.17869031`), "Cancel the deal?" experiment (Dataverse `10.7910/DVN/TOYM2W`). Not reviewed because outside the priority topics; available for a later pass.

### Systematic discovery by DataCite

DataCite indexes Zenodo, Dataverse, Dryad, figshare, ICPSR and many institutional repositories. A quoted-DOI query finds deposits whose metadata mention a paper. Run over the 359 DOIs in the two queues: 20 had hits. A second sweep over 20,247 topic-matched FT50 papers (2006 onward; order: Management Science, M&SOM, POM, SMJ, Organization Science, Research Policy, others) runs in chunks; the first 1,000 (all Management Science) gave the Gross and Bhaskarabhatla et al. records. The sweep output is kept outside the repository; rerun with `_research/archive/datacite-sweep.py` after adding it if needed.

## Batch 5 (2026-10-16): CrowdBerkeley Kickstarter database, published

Status: **published and confirmed 2026-10-16.** Merged in PR 7 (merge commit `8598959`). Cloud publisher run [38899203737](https://github.com/konstantinosStouras/datasets/actions/runs/38899203737) completed successfully. `catalog-public.json` on `main` then showed **138 collections, 21 research entries**, the new ID with its paper title and date added 2026-10-16, and no URLs in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `kickstarter-relational-database` | Yu, Johnson, Lai, Cricelli, Fleming, Research Policy 46(10), 1723-1737 (2017), DOI 10.1016/j.respol.2017.07.008 | [Harvard Dataverse EOYBXM](https://doi.org/10.7910/DVN/EOYBXM), CC0, two public files (split ZIP, about 3.5 GB). The record cites the paper. Range requests: first part has the split-archive signature and its start inflates to a SQLite 3 header with tables project, creator, comments, reward, funding_trend, location; the second part's central directory lists one file, `hdd/kickstarter.db`. | Full database not downloaded. Creator profiles and comments: personal-data note. Scraped from Kickstarter (platform terms). Coverage years not stated. The paper's Kiva and CrowdRise databases were not found. Paper full text not read. |

Found by following a lead (the paper presents public databases) with Dataverse and DataCite title searches after a web search found no download page.

## Batch 6 (2026-10-16): deskilling-technology experiments and three named public datasets, published

Status: **published and confirmed 2026-10-16.** Merged in PR 9 (merge commit `efa0324`). Cloud publisher run [38900143266](https://github.com/konstantinosStouras/datasets/actions/runs/38900143266) completed successfully (12:23:29 UTC). `catalog-public.json` on `main` then showed **142 collections, 25 research entries**, all four IDs below with the right access classes, and no URLs in the sanitized JSON.

| Dataset ID | Papers | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `deskilling-technology-ride-hail-experiments` | Ong and Png, Strategic Management Journal 47(2), 364-389 (2025), DOI 10.1002/smj.70017 | [Harvard Dataverse IGBHPE](https://doi.org/10.7910/DVN/IGBHPE), CC0, registered as a supplement to the paper (DataCite hit). Nine public files; README, bootstrap table, field table (200 rows) and vignette table (26,499 rows, 803 participants) parsed. | Participant-level data with age and sex (de-identified IDs). Country not stated in the files read. Paper full text not read. |
| `kauffman-firm-survey` | Three Journal of Business Venturing papers (2014, 2020, 2022) | Kauffman Foundation page links public-use files. Stata file downloaded and read: 4,928 firms, 4,492 variables. Imputed-data ZIP listed. | Abstracts do not say whether public-use or restricted data were used. Confidential data need the paid NORC enclave. A Management Science paper (2022) and a Review of Financial Studies paper (2012) used restricted data and are deliberately not cited. |
| `panel-study-of-entrepreneurial-dynamics-psed` | Five papers in Entrepreneurship Theory and Practice and Journal of Business Venturing (2012-2024), including a replication study | PSED project site opened: data through ICPSR. DataCite records exist for ICPSR studies 37203, 37202, 38153, 38154. | **ICPSR blocks scripted access: no data file was opened.** Needs a free ICPSR account. Use shown in each paper's abstract only. |
| `world-bank-enterprise-surveys` | Research Policy 2018 and 2019, Entrepreneurship Theory and Practice 2017 | Program page states survey information is publicly available. Microdata Library API: 794 studies, a study record, and the public sampling note PDF downloaded. One paper checked in its author working paper. | **Microdata sit behind a free login: no data file was opened.** Evidence of use is the abstract (and one working paper). |

Dry run of the publisher's merge code before pushing: 142 collections, 25 research entries, no duplicate IDs. The queues gained 22 appended rows and updated rows for the cited papers.

### Leads found in this pass and not added

- SBIR.gov (small business awards): the site and its API answer scripted requests with HTTP 403, so nothing could be verified. 17 FT50 abstracts mention SBIR/STTR (Research Policy, Organization Science, Strategic Management Journal, Management Science, AER). Not added; a person with a browser could check the bulk award files.
- Global Entrepreneurship Monitor: ICPSR lists the Adult Population Survey 1998-2017 (study 20320), but ICPSR access is blocked here; GEM's own site not yet checked. 16 abstracts mention it.
- Community Innovation Survey (Eurostat), FDA Orange Book/Drugs@FDA, Crunchbase, Kauffman restricted data: not yet reviewed.

### New method: named public datasets in abstracts

Scanned 2006-2026 FT50 abstracts that match the innovation/entrepreneurship words for names of public data sources (count of matching papers in brackets): Kickstarter (78), PatentsView/USPTO (51), PATSTAT/EPO (48), Community Innovation Survey (36), Compustat (32, licensed), FDA data (21), Crunchbase (17), SBIR/STTR (17), Global Entrepreneurship Monitor (16), PSED (12), Kauffman Firm Survey (6), World Bank Enterprise Surveys (5). Reading the abstract wording shows genuine use versus false matches. This finds datasets used by many papers, a good complement to the per-paper repository search.

## Batch 7 (2026-10-16): five patent and entrepreneurship replication deposits, published

Status: **published and confirmed 2026-10-16.** Merged in PR 10 (merge commit `5a00e92`). Cloud publisher run [38901007519](https://github.com/konstantinosStouras/datasets/actions/runs/38901007519) completed successfully (12:30:56 UTC). `catalog-public.json` on `main` then showed **147 collections, 30 research entries**, all five IDs below, and no URLs in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `reliance-on-science-patent-paper-citations` | Marx and Fuegi, Strategic Management Journal 41(9), 1572-1594 (2020), DOI 10.1002/smj.3145 | [Zenodo 3236339](https://doi.org/10.5281/zenodo.3236339), open, CC BY-NC 4.0; the record names the SMJ article. Pairs table downloaded and parsed (59,202 rows); first rows of the 1.4 GB citation table read by range request. | **Latest release is U.S.-only; the SMJ paper is about worldwide citations, so its data are in older versions (64 versions exist), not inspected.** Non-commercial license. |
| `dod-sbir-sttr-awards-patents-commercialization` | Bottai, de Rassenfosse, Raiteri, Research Policy 54(9), 105302 (2025), DOI 10.1016/j.respol.2025.105302 | [Zenodo 17018422](https://doi.org/10.5281/zenodo.17018422), open, CC BY 4.0, 12 files. README and five tables downloaded and parsed (2,213 awards, 42,342 patents, 3,623 links, 2,027 web pages). | Department of Defense SBIR/STTR only, 1984-2018; a derived database, not the official SBIR.gov files. Paper full text not read. |
| `disruptive-patents-cd-index-uspto` | Macher, Rutzer, Weder, Research Policy 53(5), 104992 (2024), DOI 10.1016/j.respol.2024.104992 | [Zenodo 8020003](https://doi.org/10.5281/zenodo.8020003) (latest 10839471), CC BY 4.0, 29 files. Small table read; first rows of the 438 MB patent-level CSV read by range request. | Large files not downloaded; R script not run. Paper full text not read. |
| `firm-technology-space-topological-replication` | Escolar, Hiraoka, Igami, Ozcan, Research Policy 52(8), 104821 (2023), DOI 10.1016/j.respol.2023.104821 | [Zenodo 7957847](https://doi.org/10.5281/zenodo.7957847) (v1.1 record 7957848), CC BY 4.0, 5 files. README read; code archive downloaded and listed (322 entries). | Regression data include Compustat-derived variables (licensed source; authors state permission for derived outputs). Nothing run. Paper full text not read. |
| `startup-social-vision-angellist-study` | van Balen and Tarakci, Organization Science 35(1), 326-345 (2024), DOI 10.1287/orsc.2023.1671 | [DataverseNL ILDZ9Q](https://doi.org/10.34894/ILDZ9Q), registered as a supplement to the paper. Study 1 workbook downloaded and parsed (1,191 rows, 66 columns); R scripts public. | **Partial: the Study 2 field-experiment file is restricted and was not accessed.** CC BY-NC-ND 4.0. Company names appear. Paper full text not read. |

Dry run of the publisher's merge code before pushing: 147 collections, 30 research entries, no duplicate IDs.

### Unresolved leads from this pass (not added)

- `10.1002/smj.3464` (Hou, Png, Xiong, SMJ 2022): a replication package record at NUS ScholarBank (`10.25540/amvf-6ty0`) exists, but, like the Png R&D directory record, anonymous requests show no downloadable files.
- `10.1016/j.respol.2023.104740` (Hotte, Research Policy 2023): a Bielefeld data publication (`10.4119/unibi/2967659`, CC BY 4.0, about 7.4 GB) exists, but the host answers scripted requests with an anti-bot challenge. Not bypassed.
- Also seen in chunks 4 to 6 and not reviewed: a Federal Court Cases Integrated Data Base record linked to a patent enforcement paper (Organization Science 2012), and an SMJ 2023 paper whose link to the PSED II record needs checking against its abstract.

## Batch 8 (2026-10-16): the Mannheim Innovation Panel and six open Research Policy deposits, published

Status: **published and confirmed 2026-10-16.** Merged in PR 11 (merge commit `c4bbb77`). Cloud publisher run [38901669227](https://github.com/konstantinosStouras/datasets/actions/runs/38901669227) completed successfully (12:36:30 UTC). `catalog-public.json` on `main` (and the raw copy the website reads) then showed **154 collections, 37 research entries**, all seven IDs below with correct access classes, and no URLs in the sanitized JSON.

| Dataset ID | Paper(s) | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `mannheim-innovation-panel-mip` | Eight Research Policy papers (2008-2016) listed by the data provider's own DOI records as documenting publications | ZEW pages read (annual survey since 1993; scientific use files; on-site and remote access). DataCite records give the rights wording and the publication list. | **Access class 'Agreement or mixed'. No data file was opened.** Researchers at publicly funded institutions only; non-commercial. Which data version each paper used is not stated. |
| `democracy-innovation-country-panel` | Zang, Research Policy 46(7), 1272-1283 (2017), DOI 10.1016/j.respol.2017.05.014 | [Dataverse KPOT20](https://doi.org/10.7910/DVN/KPOT20), CC0, six files; all downloaded, four Stata tables parsed (10,914 country-years, 214 countries, 1960-2010). | Variable sources not checked. Paper full text not read. |
| `us-cleantech-startup-alliances-panel` | Doblinger, Surana, Anadon, Research Policy 48(6), 1458-1475 (2019), DOI 10.1016/j.respol.2019.02.006 | Mendeley Data `t8rrxnb6p2`, CC BY-NC 3.0, supplement to the paper. Panel table 2,408 rows x 24 numeric columns, 657 startups, 2008-2012; do-file read. | Non-commercial. No codebook. |
| `lithium-ion-battery-core-patents` | Malhotra, Zhang, Beuse, Schmidt, Research Policy 50(9), 104318 (2021), DOI 10.1016/j.respol.2021.104318 | Mendeley Data `c5nydpmxt2`, CC BY-NC 3.0. 419 patent-family rows x 50 columns. | Only the core trajectory, not the full 101,620 families. |
| `government-ideology-innovation-country-panel` | Wang, Feng, Chen, Wen, Chang, Research Policy 48(5), 1232-1247 (2019), DOI 10.1016/j.respol.2018.12.009 | Mendeley Data `jgcg2y64sw`, CC BY 4.0. 1,573 rows x 73 columns, 102 countries, 1995-2015. | Paper says 110 countries. Chinese column headings. No codebook. |
| `expert-surveys-research-spending-replication` | Urbatsch, Research Policy 49(8), 104058 (2020), DOI 10.1016/j.respol.2020.104058 | Mendeley Data `2587f727rh`, CC BY 4.0, six files downloaded; research-spending table 1,078 rows, 138 countries, 2006-2017. | Source of the official figures not named in the abstract. |
| `emerging-market-categories-innovation-data` | Lo, Nag, Xu, Agung, Research Policy 49(3), 103911 (2020), DOI 10.1016/j.respol.2019.103911 | Mendeley Data `ws8gbhtntj`, CC BY 4.0. One Stata table of 72,778 rows x 73 columns. | **No codebook or code; the unit and years are not stated.** Read the paper first. |

Dry run of the publisher's merge code before pushing: 154 collections, 37 research entries, no duplicate IDs. The queues gained 28 appended rows.

### Unresolved lead from this pass

- DataverseNL `10.34894/0vlsgb` (a Research Policy 2019 paper on repeated ties in university-industry consortia): the record lists no files, so nothing could be verified. Not added.

## Batch 9 (2026-10-16): Community Innovation Survey tables and Global Entrepreneurship Monitor, published

Status: **published and confirmed 2026-10-16.** Merged in PR 12 (merge commit `b6e8d62`). Cloud publisher run [38902467271](https://github.com/konstantinosStouras/datasets/actions/runs/38902467271) completed successfully (12:43:11 UTC). `catalog-public.json` on `main` then showed **156 collections, 39 research entries**, both IDs below, and no URLs in the sanitized JSON.

| Dataset ID | Papers | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `community-innovation-survey-eurostat` | Five Research Policy papers (2010-2025) whose abstracts state use of the Community Innovation Survey | Eurostat catalogue lists ten waves (CIS2006 to CIS2024; 263 tables). Table `inn_cis13_bas` (CIS2022) downloaded in full via the API: 60,076 values, 31 geographies, 103 industry codes. Methodology and microdata-access pages read. | **Public component is the aggregate tables only.** The papers use firm-level microdata (national or Eurostat), which need accreditation (scientific-use or Safe Centre). Entry says so. Full texts not read. |
| `global-entrepreneurship-monitor-gem` | Nine papers in Research Policy, Journal of Business Venturing, Entrepreneurship Theory and Practice and Journal of Political Economy whose abstracts state use of GEM | GEM data page lists 68 Adult Population Survey and 61 National Expert Survey files, downloadable without login through the page's own download action. 2019 APS individual file downloaded and parsed (163,006 respondents, 419 variables, 50 countries); 2019 national file parsed (50 x 218); a 2021 NES file downloaded (zip listing only). | No license or terms text found (the terms page returned 'not found'). Files have no stable direct links. Most files only listed. Full texts not read. |

Dry run of the publisher's merge code before pushing: 156 collections, 39 research entries, no duplicate IDs.

### Leads from this pass not added

- Zenodo `10.5281/zenodo.10960975` (ESG scores for equity crowdfunding platforms, JBV 2024): the public record is documentation of how scores were built; the dataset version (`10960976`) is **restricted**. Not added.
- ICPSR links without a stated use: PSED II is listed on ICPSR for an SMJ 2023 paper (racial gap in entrepreneurship), an ETP 2022 paper (growth mindset) and an ETP 2025 paper; the abstracts do not say PSED/MIDUS was used (the SMJ abstract says only 'a representative sample of American new business founders in 2005', consistent with PSED II). Not added to the PSED entry.
- openICPSR `e100177` (Tangail survey, Bangladesh, JBV 2019): not verified (ICPSR access blocked).

## Batch 10 (2026-10-16): Orange Book, ClinicalTrials.gov and the World Bank FAT survey, published

Status: **published and confirmed 2026-10-16.** Merged in PR 13 (merge commit `5c3d5aa`). Cloud publisher run [38903631072](https://github.com/konstantinosStouras/datasets/actions/runs/38903631072) completed successfully (12:52:56 UTC). `catalog-public.json` on `main` then showed **159 collections, 42 research entries**, all three IDs below with correct access classes, and no URLs in the sanitized JSON.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `nber-fda-orange-book-patent-exclusivity` | Durvasula, Hemphill, Ouellette, Sampat, Williams, Research Policy 52(7), 104791 (2023), DOI 10.1016/j.respol.2023.104791 | [NBER data page](https://www.nber.org/research/data/orange-book-patent-and-exclusivity-data-1985-2016) names the article as the user's guide. README read; four clean Stata tables downloaded and parsed (130,259 drug-patent rows, 31 editions 1985-2016; 32,427 exclusivity rows). | Scanned PDFs and Excel folders not opened. No license statement on the pages. Historical extract only. |
| `clinicaltrials-gov-registry` | Rathee, Malik, Salandra, Research Policy 54(1), 105112 (2025), DOI 10.1016/j.respol.2024.105112 | Public API v2 returned 607,349 studies (80,551 with results) and a full study record on 16 Oct 2026. Bulk zip starts with a ZIP signature. | The paper's abstract describes its focus on the registry but does not say 'data from', so use is inferred. Bulk archive (several GB) not inspected. |
| `world-bank-firm-adoption-of-technology-fat` | Cirera, Comin, Cruz, Quarterly Journal of Economics 141(3), 2025-2085 (2026), DOI 10.1093/qje/qjag018 | Dataverse record for the paper points to the World Bank microdata; the Microdata Library's open API lists a 16-study FAT collection (2019-2023) and a study record whose citation requirement names the paper. | **Microdata behind a free login: no data file opened.** Full text not read. |

Dry run of the publisher's merge code before pushing: 159 collections, 42 research entries, no duplicate IDs.

### Leads from this pass logged and not added

- JFQA 2025 innovation screening (Zheng): package holds code, intermediate outputs and **pseudo (synthetic) data**; the public USPTO inputs are on an external Dropbox link. Marked 'Code only — not a dataset addition'.
- QJE papers: Juhasz et al. (2026) and Kalyani et al. (2025) have Dataverse records with README only (data on SharePoint links, not verifiable); Bergeaud et al. (2025) can only be run in the French secure data environment; Nguyen (2026) has logs and code, no data.
- JMR 2025 crowdfunding by gender (Gao et al.): every file in the Dataverse record is access-restricted. JM 2026 product portfolio paper: licensing restrictions.
- JPE 2026 (Bhalotra et al., medical innovation) uses IPUMS census extracts (5 GB; public) but its topic is health outcomes of an innovation, outside the priority topics. Not reviewed further.

### Large downloads

One request for the ClinicalTrials.gov bulk zip used a range header that the server ignored and pulled about 3 GB before I stopped it. The partial file was deleted. Use `curl --max-filesize` or request only headers for large bulk files.

## Batch 11 (2026-10-16): six replication deposits in finance, economics and international business journals

Status: published and confirmed. Workflow run 38905315190 succeeded at 13:06:36 UTC; the live feed then showed 165 collections and 48 research entries with all six IDs present.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `startup-patent-scope-timing-data` | Hegde, Ljungqvist, Raj, Review of Financial Studies 35(6), 2705-2742 (2021), DOI 10.1093/rfs/hhab097 | [Dataverse I6PMAE](https://doi.org/10.7910/DVN/I6PMAE), CC0, seven files. Four tables and the do-file downloaded and parsed (29,933 x 131; 12,180 x 47; 8,281 x 30). | Identifiers not examined; do-file not rerun. |
| `taxation-innovation-state-inventor-panels` | Akcigit, Grigsby, Nicholas, Stantcheva, Quarterly Journal of Economics 137(1), 329-385 (2021), DOI 10.1093/qje/qjab022 | [Dataverse SR410I](https://doi.org/10.7910/DVN/SR410I), CC0. 344 MB packet downloaded in full; inner archive opened: state panel 3,848 rows, inventor panel 6,465,562 rows, location choice 4,659,712 rows. | Only top corporate tax rate and a few tax-base variables included. |
| `directed-innovation-climate-agriculture-data` | Moscona, Sastry, QJE 138(2), 637-701 (2022), DOI 10.1093/qje/qjac039 | [Dataverse 5ELEPA](https://doi.org/10.7910/DVN/5ELEPA), CC0, 82 files (3.6 GB). README read; crop (632 x 43) and county (21,027 x 16) tables parsed. | Large climate inputs listed only. Nothing rerun. |
| `compustat-uspto-patent-assignment-link` | Arque-Castells, Spulber, Journal of Political Economy 130(7), 1860-1918 (2022), DOI 10.1086/719908 | [Zenodo 6352357](https://doi.org/10.5281/zenodo.6352357) (files in 6352358), CC BY 4.0. README read in full; smallest archive downloaded and listed. | Large archives (up to 1.6 GB) not downloaded. Compustat identifiers: licensed source. Coverage 1981-2012 per README. |
| `employment-protection-process-innovation-data` | Bena, Ortiz-Molina, Simintzi, Journal of Financial Economics 146(2), 637-664 (2022), DOI 10.1016/j.jfineco.2021.10.005 | Mendeley Data `jpg9bjzjwk`, CC BY 4.0, supplement to the paper. Firm-year panel 45,263 x 78 (fiscal years 1975-1997, 4,447 firms). | 'Public version' of the data; what was left out is not stated. |
| `populism-entrepreneurship-individual-data` | Bennett, Boudreaux, Nikolaev, Journal of International Business Studies 54(1), 151-181 (2023), DOI 10.1057/s41267-022-00515-9 | Mendeley Data `c8vz84fzfz`, CC BY-NC-SA 4.0. 407 MB Stata table: 2,467,779 rows x 43 columns. | Underlying surveys not described; may carry their own terms. Years variable 1960-2020. |

Dry run of the publisher's merge code before pushing: 165 collections, 48 research entries, no duplicate IDs.

## Batch 12 (2026-10-16): KPSS patent values extended to 2025, and three QJE deposits

Status: KPSS published and confirmed (run 38905816430 succeeded at 13:10:38 UTC; the live feed then showed 166 entries including `kpss-patent-values-extended-2025`). The two QJE deposits below are also published and confirmed: run 38906120243 succeeded at 13:13:08 UTC, and `catalog-public.json` on `main` (read through git, since the raw.githubusercontent.com copy lagged) then held 168 entries including both IDs. The management practices entry is also published and confirmed: run 38906891938 succeeded at 13:19:05 UTC, and `catalog-public.json` on `main` then held 169 entries including its ID.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `kpss-patent-values-extended-2025` | Kogan, Papanikolaou, Seru, Stoffman, Quarterly Journal of Economics 132(2), 665-712 (2017), DOI 10.1093/qje/qjw040 | [GitHub repository](https://github.com/KPSS2017/Technological-Innovation-Resource-Allocation-and-Growth-Extended-Data), head 78ecbc8 (2026-09-09). Three zips cloned and read in full: 3,831,908 rows each; issue years 1926-2025; 10,599 distinct permnos. | No license stated. CRSP codes come from a licensed source. Values differ slightly from the paper. Paper full text not read. |
| `who-becomes-an-inventor-public-tables` | Bell, Chetty, Jaravel, Petkova, Van Reenen, QJE 134(2), 647-713 (2019), DOI 10.1093/qje/qjy028 | [Dataverse UITDYS](https://doi.org/10.7910/DVN/UITDYS), CC0, 26.7 MB zip downloaded in full. README read; seven aggregate CSV tables opened (741 to 574,741 rows). | Aggregates only; microdata not public. Codebook PDF not read. |
| `who-profits-from-patents-application-data` | Kline, Petkova, Williams, Zidar, QJE 134(3), 1343-1404 (2019), DOI 10.1093/qje/qjz011 | [Dataverse HMFYON](https://doi.org/10.7910/DVN/HMFYON), CC0, 32.6 MB zip downloaded in full. Application file opened: 3,737,351 rows, years 2000-2013. | Partial: tax and wage data are confidential. Mostly code. |
| `management-practices-survey-bloom-van-reenen` | Bloom, Van Reenen, QJE 122(4), 1351-1408 (2007), DOI 10.1162/qjec.2007.122.4.1351 | [Dataverse NUOTSQ](https://doi.org/10.7910/DVN/NUOTSQ), CC0, found in sweep chunk 19. Both data tables downloaded and parsed: 6,267 rows x 189 columns each, 732 firm codes, 1994-2004, four countries. Instruction note read. | Anonymized (company names removed), so results may differ from the paper. The two tables are not labelled and differ in 94 columns; not investigated. Do-file not rerun. |

Considered and not added: Emerick, de Janvry, Sadoulet, Dar, AER 106(6) (2016), Dataverse W97NZB (CC0, 5.8 MB). It is a field experiment on flood-tolerant rice in India, an agricultural development topic outside the innovation-management focus. Revisit if the owner wants technology adoption in development.

An earlier sweep hit pointed to Zenodo 15545361 for this paper; that record is a different dataset (Green AI patents), so it was not used.

Sweep review, chunk 18 (EJOR, Review of Economic Studies, JOM, JMIS, AER 2009-2010 and others): almost all hits were unrelated figshare supplements from other journals' articles. The real leads are about 25 AER 2009-2010 replication deposits on openICPSR (for example Do Traditional Institutions Constrain Female Entrepreneurship? e112341; Risk Taking by Entrepreneurs e113334; Estate Taxation, Entrepreneurship, and Wealth e113293; Burden of the Nondiversifiable Risk of Entrepreneurship e112349; Learning about a New Technology: Pineapple in Ghana e112329; Technological Revolutions and Stock Prices e113321). openICPSR cannot be checked by script, so none were added. A person with a browser could verify them. The eight DOIs that failed during the sweep were rerun: none has a deposit.

Sweep finished (all 21 chunks, 20,247 topic-matched FT50 papers). Chunks 19 and 20 added one verified dataset (Bloom and Van Reenen above). The rest of their hits were unrelated figshare or Zenodo records and another set of AER 2006-2008 openICPSR deposits that cannot be checked by script (for example Does Innovation Cause Stock Market Runups? e113255; Restructuring Research e113260; On the Cyclicality of Research and Development e116283; Estimating the Effects of Global Patent Protection in Pharmaceuticals e116242). The sweep only covers papers that DataCite links by DOI, so it is a floor and not a census.

Dry run of the publisher's merge code before pushing the management practices entry: 169 collections, 52 research entries, no duplicate IDs.

## Batch 13 (2026-10-16): Management Science deposits found through the owner's literature database

Status: published and confirmed. Workflow run 38913236095 succeeded at 14:07:51 UTC; `catalog-public.json` on `main` then held 172 entries including all three IDs.

Method: the 12,485 Management Science records in the site's `papers-ms.json` were filtered to innovation, new product, entrepreneurship, patent and technology topics (2,766 not yet in the review queues; 690 of them from 2010 on with a narrow topic match). Abstract cues were checked, and the Harvard Dataverse and DataverseNL search APIs were queried for records mentioning "Management Science" (68 records) and matched to paper titles. Most Management Science abstracts point only to the INFORMS supplement, which scripts cannot read.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `founding-strategy-startup-website-text` | Guzman, Li, Management Science 69(1), 101-118 (2023), DOI 10.1287/mnsc.2022.4369 | [Dataverse NRYTAA](https://doi.org/10.7910/DVN/NRYTAA), CC0, 102 files, about 11 GB. README read; 2003 website-text table downloaded and parsed (4,674 rows: 493 startups, 4,181 public firms); Stata similarity file header read by range request. | Beta release; analysis file needs Crunchbase academic data. Model files are Python pickles, not opened. GitHub code page unreachable from here. Third-party website text. |
| `automation-specialization-cashier-taxi-data` | Gong, Png, Management Science 70(3), 1580-1595 (2024), DOI 10.1287/mnsc.2023.4760 | [Dataverse JKYRPS](https://doi.org/10.7910/DVN/JKYRPS), CC0. README and disguise note read; cashier table 152,246 x 350 (4 stores) and taxi survey 402 x 39 downloaded in full and parsed. | Cashier data disguised under an NDA; one appendix table not reproducible. Country and years not stated in the deposit. |
| `startup-hiring-phd-job-choice-replication` | Roach, Sauermann, Management Science 70(6), 3619-3644 (2024), DOI 10.1287/mnsc.2023.4868 | [Dataverse IGFCET](https://doi.org/10.7910/DVN/IGFCET), CC0. Table 2,415 x 22 and do-file downloaded and read. | Depositors allow replication use only, despite the CC0 label. Survey years not in the deposit. |

Management Science leads checked and not added: Younkin and Kuppuswamy 2018 crowdfunding (the DataCite link is the UNC copy of the article text, no data); Zhang, Yu and Chen 2022 return insurance (DataverseNL JD.com files all restricted); Niu et al. 2024 bullwhip (data-report PDF only); Gillingham and Bollinger 2021 solar adoption (openICPSR, blocked); Becker et al. 2022 crowd classification (CC0 experiment files, outside the core topic, not inspected); Cappelen et al. 2025 consumer exploitation experiment (CC0, outside topic). A Zenodo search for Management Science deposits was started and had not returned when this batch was committed.

Also in this batch: the batch 12 entries now use the catalog's standard vocabulary (Administrative records, Firms & institutions, Panel / longitudinal, Places & geographic areas).

Dry run of the publisher's merge code before pushing: 172 collections, 55 research entries, no duplicate IDs.

## FT50-wide discovery pass (started 2026-10-16, in progress)

Owner's instructions this session: check all FT50 papers in the Lit for public datasets, focus on papers from the last 30 years (1996 on), prefer datasets that are useful for follow-up studies, and do not build a separate experiments category.

Methods and outcomes so far:

- Management Science title search: the 690 Management Science papers from 2010 on with innovation, entrepreneurship, patent or technology topics (not already in the queues) were searched by title on Harvard Dataverse and Zenodo. Dataverse returned no deposits beyond batch 13 (the only matches were the editorial column "Management Insights" against an unrelated rental-market dataset, and the two deposits already handled). Zenodo returned nothing usable in the part completed (about 560 of 690; the remainder hit connection resets and was not rerun).
- Dataverse journal-name searches ("Management Science", "10.1287/mnsc") on Harvard Dataverse and DataverseNL: 68 and 132 records, mostly ICPSR archive links for old papers or deposits for finance and behavioural papers; the on-topic ones are in batch 13. A lead not added: Kelley, Management Science 40(11), 1406-1425 (1994), survey of metalworking plants on programmable automation, held at ICPSR 1087 (blocked for scripts).
- DataCite batch sweep: the DataCite API accepts up to about 40 DOIs joined with OR in one `relatedIdentifiers.relatedIdentifier` query, so the whole list can be swept in roughly 3,000 requests. The Lit holds 248,793 FT50 DOIs; 20,247 were swept earlier; 113,511 of the rest are from 1996 on and are being swept now in priority order (MS, M&SOM, POM, Research Policy, SMJ, Organization Science, JBV, SEJ, ETP, AMJ, MISQ, ISR, JOM, Operations Research, IJOC, Marketing Science, JMR, JM, then the others). Script: scratchpad `sweep2/dc2.py` (to be archived under `_research/archive/`). Results go to `sweep2/res.json`.
- Journal replication archives listed directly: Harvard Dataverse QJE (431 datasets) and JPE (284) collections; Zenodo communities `restud-replication` (544 records) and `es-replication-repository` (290, Econometric Society journals). American Economic Review deposits sit on openICPSR, which blocks scripts.

Next: triage the sweep hits by host and journal, drop figshare "Additional file" noise and ICPSR archive links, verify candidates with actual file reads, and publish in batches with the usual STATUS records.

## Batch 14 (2026-10-16): six deposits from the QJE and JPE replication archives

Status: published and confirmed. Workflow run 38920471271 succeeded at 15:01:20 UTC; `catalog-public.json` on `main` then held 178 entries including all six IDs. The Chinese AI-firm entry was then enriched with the REStud 2023 paper and its Zenodo package (next pull request).

Found by listing the Harvard Dataverse QJE and JPE collections, matching deposit titles and citations to the Lit, scoring the 826 matched papers from 1996 on by management relevance, and inspecting the top of that list.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `uspto-patent-applications-1998-2003-aipa` | Hegde, Herkenhoff, Zhu, JPE 131(7), 1845-1903 (2023), DOI 10.1086/723636 | [Dataverse PFSRVT](https://doi.org/10.7910/DVN/PFSRVT), CC0. README read; 159.5 MB Stata file read end to end: 1,107,710 rows, 36 columns. | Public version drops 428,690 pending or abandoned applications; twin-patent and firm files not deposited. |
| `french-industrialization-firm-panels-1794-1840` | Juhász, Squicciarini, Voigtländer, JPE 132(10), 3215-3259 (2024), DOI 10.1086/730205 | [Dataverse EGWOPG](https://doi.org/10.7910/DVN/EGWOPG), CC0. README read; six tables parsed (cotton 868, metallurgy 1,366, paper 867 rows). | Two-period panels; study-specific firm ids. |
| `inventor-migration-patents-database-prato` | Prato, QJE 140(1), 165-238 (2025), DOI 10.1093/qje/qjae040 | [Dataverse IX6AW9](https://doi.org/10.7910/DVN/IX6AW9), CC0. 687 MB zip downloaded; ReadMe read; Stata headers read: inventors_database 8,981,831 x 62, inventors_year 6,099,891 x 22, inventors_unique 4,009,660 x 13, coauthors 35,659,955 x 4. | Raw PATENTS-ICRIOS and WIPO inputs not included; tables not loaded in full; inventor names present. |
| `federal-rd-funding-university-tables-babina` | Babina, He, Howell, Perlman, Staudt, QJE 138(2), 895-954 (2023), DOI 10.1093/qje/qjac046 | [Dataverse EZZBCR](https://doi.org/10.7910/DVN/EZZBCR), CC0. All public tables parsed (Single Audit 97,766 rows; IPEDS 92,397 rows; CFDA 5,884). | Partial: IRIS and Census outcomes restricted, code only. |
| `china-ai-firms-surveillance-contracts-data` | Beraja, Kao, Yang, Yuchtman, QJE 138(3), 1349-1402 (2023), DOI 10.1093/qje/qjad012 | [Dataverse GCOVGX](https://doi.org/10.7910/DVN/GCOVGX), CC0. 610 MB zip downloaded; README read; headers of four Stata tables read (firm panel 1,040,621 x 120). | Commercial source data released deidentified; reuse terms uncertain. |
| `induced-automation-innovation-patent-panels` | Hémous, Olsen, Zanella, Dechezleprêtre, JPE 133(6), 1975-2028 (2025), DOI 10.1086/734778 | [Dataverse IMCSW1](https://doi.org/10.7910/DVN/IMCSW1), CC0, 1,045 files, 56 GB. READMEs and Sources.md read; folder sizes listed; two tables parsed (133 x 104; 58,731 x 8). | PATSTAT, EPO text and Orbis inputs excluded; most files not downloaded. |

Leads inspected and not added (recorded in the broader queue): JPE military innovation (simulated table only); QJE trust and innovation, generative AI at work, workplace knowledge flows, unequal gains from product innovations, discretion in hiring, capitalists (code only); New Frontiers (README only, NBER-restricted inputs); worker evaluations in auto manufacturing (field experiment, set aside per the owner); codification and technology absorption (README only); Econometrica female entrepreneurship (code only), managerial autonomy (simulated Prowess data), screening property rights (17 GB, not inspected). Technology Sophistication Across Establishments (QJE 2026) is already cited on the FAT entry.

Dry run of the publisher's merge code before pushing: 178 collections, 61 research entries, no duplicate IDs.

## Batch 15 (2026-10-16): seven deposits from the FT50-wide sweep and companion searches

Status: published and confirmed. Workflow run 38939563044 succeeded at 17:25:37 UTC; `catalog-public.json` on `main` then held 185 entries including all seven IDs.

Sweep outcome: all 113,511 papers from 1996 on were swept (40 DOIs failed with transient errors and were not rerun). 7,673 raw hits; 750 clean leads after removing figshare "Additional file" supplements, SAGE and publisher figshare collections, arXiv, ICPSR archive links and other noise, and papers already in the queues. By journal: QJE 358, EJOR 64, JPE 48, AER 45, JMR 37, RFS 29, JM 25, Psychological Science 21, JFE 21, MS 10, ASR 10, Research Policy 9. By host: Harvard Dataverse 550, Zenodo 111, Mendeley 36, SMU 20, Dryad 20, Erasmus 19, DataverseNL 17. The lead list is in the scratchpad `sweep2/triage2.json` and should be copied to the archive if the session ends.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `ai-occupational-exposure-aioe` | Felten, Raj, Seamans, SMJ 42(12), 2195-2217 (2021), DOI 10.1002/smj.3286 | [GitHub AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE) cloned (head adca5fc, 2024-06-03). All workbook sheets and Stata inputs parsed (774 occupations, 250 industries, 3,271 counties). | No licence file. |
| `twin-2k-500-digital-twin-personas` | Toubia et al., Marketing Science 44(6), 1446-1455 (2025), DOI 10.1287/mksc.2025.0262 | [Hugging Face](https://huggingface.co/datasets/LLM-Digital-Twin/Twin-2K-500), CC BY 4.0. Human-response tables parsed (2,058 x 761; 2,058 x 127); one persona Parquet chunk parsed (294 rows). | Card links the preprint, not the journal DOI. Includes behavioural experiments. |
| `scientific-complexity-pubmed-openalex` | Melluso, Research Policy 55(8), 105570 (2026), DOI 10.1016/j.respol.2026.105570 | [Zenodo 20813591](https://doi.org/10.5281/zenodo.20813591). Data description read; CSV header and first rows read by range (9,627,624 rows per the description). | Licence conflict: CC BY 4.0 on Zenodo versus O-UDA-1.0 (non-commercial) in the description. File not downloaded in full. |
| `om-or-conference-value-survey` | Cavallin Toscani, Atasu, Van Wassenhove, Vinelli, M&SOM 26(1), 66-79 (2024), DOI 10.1287/msom.2022.0591 | [Zenodo 8256528](https://doi.org/10.5281/zenodo.8256528), CC BY 4.0. CSV parsed: 555 x 58. | Small, academic-community survey. |
| `ehr-audit-trail-event-logs` | Pentland, Vaast, Ryan Wolf, MISQ 45(2), 967-984 (2021), DOI 10.25300/misq/2021/15360; Kim, Pentland, Frank, Ryan Wolf, Organization Science 36(2), 862-880 (2025), DOI 10.1287/orsc.2022.16749 | [Dataverse 5FSJ1G](https://doi.org/10.7910/DVN/5FSJ1G), CC0. README read; 42.5 MB R file downloaded (size matches). | Not parsed (no R here); counts from the README. |
| `mlb-managers-team-performance-peeters` | Peeters, Salaga, Juravich, Management Science 66(6), 2735-2751 (2020), DOI 10.1287/mnsc.2019.3323 | [DataverseNL EKHDNA](https://doi.org/10.34894/EKHDNA), CC BY 4.0, 58 files. README read; four tables parsed (723 team-seasons; 158 managers; 116 GMs; 20,369 salaries). | Large lineup and game files listed only. |
| `iri-marketing-dataset-category-characteristics` | Bronnenberg, Kruger, Mela, Marketing Science 27(4), 745-748 (2008), DOI 10.1287/mksc.1080.0450; Datta, Ailawadi, van Heerde, JM 81(3), 1-20 (2017), DOI 10.1509/jm.15.0340 | [DataverseNL ELVF0J](https://doi.org/10.34894/ELVF0J), custom terms. Survey CSV parsed (752 x 412); codebook read. | IRI data under agreement (Circana); not accessed. Access class: Agreement or mixed. |

Also: the Mannheim Innovation Panel entry now cites Becker and Dietz, Research Policy 33(2) (2004), found through the ZEW scientific-use-file record.

Leads inspected and not added: two Research Policy deposits on Dryad (synthesis centres; citation inflation and the disruption index), whose downloads sit behind the Anubis anti-bot check (same blocker as Bielefeld; metadata and file lists are readable through the Dryad API); AMJ framing study (newspaper PDFs only); a 2026 third-party replication of Flammer (2013) on Dataverse; a Zenodo escrow record for a digital-twin benchmark (restricted). Of the Management Science sweep hits, the climate-concern stock study, copy trading, bank-run contagion, leadership and incentives, group-size tournaments and country-image trade deposits are outside the owner's topics and were not inspected.

Dry run of the publisher's merge code before pushing: 185 collections, 68 research entries, no duplicate IDs.

## Batch 16 (2026-10-16): Brazilian public-hospital panel

Status: published and confirmed. Workflow run 38939877345 succeeded at 17:28:21 UTC; `catalog-public.json` on `main` then held 186 entries including the new ID.

| Dataset ID | Paper | Evidence and file check | Limits |
| --- | --- | --- | --- |
| `brazil-public-hospitals-private-management-panel` | Coube, Fontes, Rocha, QJE 141(3), 2597-2673 (2026), DOI 10.1093/qje/qjag028 | [Dataverse D7IMCO](https://doi.org/10.7910/DVN/D7IMCO), CC0. 74.5 MB zip downloaded; README data section read; all 16 Stata headers read (hospital panel 37,584 x 45; OSS register 43,607 x 30; staff panels up to 4.1 million rows). | Some variables from identified records are aggregated or masked. Portuguese variable names. |

Leads inspected and not added: Boehm and Oberfield (ASI data not redistributable); Biswas et al. JM channel adoption (5% noisy sample under NDA); Minni managers (proprietary personnel data); Weidmann et al. good manager (experiment); Autor et al. superstar firms (public aggregates plus Census code); Gopinath et al. South Europe (Orbis); Gumpert et al. multiple establishments (do-files only).

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

## Review coverage and unresolved leads (current)

Catalog state: 42 research entries citing 69 distinct papers (see the live progress log for the total number of collections).

Queues: the priority queue has 186 rows (unverified lead 110, under review 9, verified 63, code only/restricted 4) and the broader queue has 415 rows (unverified lead 337, under review 9, verified 65, code only/restricted 4). Rows come from three heuristic sources, none a complete census: the abstract-availability scan (102,778 DOIs, 2006 to 2026), an abstract scan for named public data sources, and a DataCite sweep of 20,247 topic-matched papers in FT50 journals (14 of 21 chunks reviewed so far). 'Unverified lead' rows from the first scan are mostly publisher supplements on blocked hosts (see Known blockers), so they are unresolved, not 'no public data'.

What these searches do and do not establish: the DataCite sweep finds deposits (Zenodo, Dataverse, Mendeley Data, Dryad, figshare, OSF, institutional repositories) whose metadata mention a topic-matched paper's DOI, so it misses deposits that do not cite the DOI. The abstract scans find datasets that abstracts name. Sources such as NBER, Eurostat, GEM, the World Bank and Kauffman were reached through the abstract scan and by following leads, not through any systematic crawl. Together they give verified additions and leads, not a count of how many papers have public data. Nothing can be said about papers whose data sit on INFORMS, Wiley, SAGE, ICPSR or openICPSR pages.

Still unresolved Management Science leads: **Artificial Intelligence, Lean Startup Method, and Product Innovations** (DOI `10.1287/mnsc.2022.03905`; the source data are described as a commercial Chinese enterprise database) and **The Uneven Impact of Generative Artificial Intelligence on Entrepreneurial Performance** (DOI `10.1287/mnsc.2024.06909`; pre-registered on OSF but no data link found). The INFORMS supplements for both could not be opened. Do not count them as unavailable or as published additions.

## Next steps for an authorized continuation

1. Pull the repository and read AGENTS, HANDOFF, METHODS and this checkpoint. Everything published is already in `main`; no local-only files need to be retrieved.
2. Finish reviewing the DataCite sweep output (the outputs are kept outside the repository; rerun `_research/archive/datacite-sweep.py` over the topic list if needed) and rerun the DOIs that failed with a transient error.
3. Ask the owner whether a person can open the blocked hosts for the priority papers (INFORMS supplements for Management Science, M&SOM and POM first), or whether another route is acceptable.
4. Possible new sources of leads: Dryad and figshare searches by journal title, OSF searches by DOI, authors' GitHub repositories named in papers. Read the abstract's whole data sentence before trusting a repository word.
5. Before any Firebase rules deployment, repair the missing project configuration and deployment guard reported above, following the website repository instructions. This is separate from catalog publication and remains unfinished.
6. Keep the documentation current: record observed outcomes, not intended ones, and keep unresolved leads.
