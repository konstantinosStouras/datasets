# Historical research helpers

These scripts preserve the discovery, verification and entry-preparation work from 16 October 2026. They were previously stored only in the original assistant's local working folder. They are reference material, not part of the website build or an instruction to repeat completed work.

**Do not run them unchanged.** Several contain original-machine paths. In particular, `export-shortlist.py` overwrites the research README and reconstructs review statuses from an older candidate snapshot; running it could erase newer manual findings. The two `add-*.py` files reconstruct older catalog entries and could replace later improvements. Adapt paths and behavior, preserve current records, and review proposed diffs before any reuse.

| File | Historical purpose |
| --- | --- |
| `shortlist.py` | Initial heuristic metadata screen; no claim of exhaustive FT50 coverage |
| `export-shortlist.py` | Original queue export; superseded by the maintained CSV files |
| `check-zenodo.py` | Public API metadata and bounded file checks for two Zenodo records |
| `verify-research.py` | NBER page links and Crossref metadata check |
| `datacite-sweep.py` | Added 2026-10-16 by the continuation session. Usage: `python3 -I datacite-sweep.py dois.txt out.json` (one DOI per line). Queries DataCite for deposits that mention each paper DOI; read-only, polite 6-thread pool. Output is a list of leads to verify by hand |
| `datacite-inspect.py` | Added 2026-10-16. `python3 -I datacite-inspect.py <DOI> ...` prints DataCite metadata, related papers, license and (for Zenodo and Dataverse) the file list. Read-only |
| `dataverse-report.py` | Added 2026-10-16. `python3 -I dataverse-report.py 10.7910/DVN/XXXXX ...` prints license, publication link, restricted flags and README clues for Harvard Dataverse and DataverseNL records; downloads small README files into a local `dvr/` folder |
| `openalex-fulltext.py` | Added 2026-10-16. `python3 -I openalex-fulltext.py <DOI> '<regex>'` finds an open-access PDF through OpenAlex, converts it with `pdftotext` and prints lines matching the regex |
| `add-dell-data.py` | Prepared the already-published Dell entry and citations |
| `add-verified-technology-data.py` | Prepared the already-published firm technology and DISCERN entries |

Historical discovery metadata is in `../evidence/initial-discovery-candidates.json`; copyrighted abstract excerpts were omitted. Current review dispositions belong in the maintained CSV queues. Zenodo verification results are in `../evidence/zenodo-link-checks-2026-10-16.json`; these are dated checks, not a guarantee of current availability.

All essential research state is now in this repository. Local duplicate CSV exports and one-off helper copies are not separate sources of truth. Unrelated GitHub Desktop recovery backups, account/session state and temporary lock files were not copied into this public research repository.
