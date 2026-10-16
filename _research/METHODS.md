# Research methods and evidence standard

Last updated: 2026-10-16. Update this document when the research procedure changes.

Reproducibility materials: historical discovery/verification helpers are in [archive/](archive/README.md), and dated discovery metadata and Zenodo file-check results are in `evidence/`. The initial candidate snapshot omits publisher abstract excerpts and does not supersede current CSV review statuses. Historical scripts require adaptation before reuse; some overwrite older outputs.

## Discovery, not automatic inclusion

Start with the owner's GitHub paper database. Deduplicate normalized DOI values. The first exploratory scan used metadata years 2006–2026 and title/abstract terms `new product`, `innovat`, `entrepreneur`, `technology management`, `patent`, `start.?up`, and `crowdfund`. It screened abstracts for data-availability phrases, `replication`, `publicly available`, Dataverse, Zenodo, OSF, GitHub, and `open data`.

The priority CSV requires a priority-topic title match, plus manually verified additions that the initial heuristic missed. The broader CSV preserves other candidates. Order by the requested journal priorities, then recent publication year. Do not treat a publication's DOI suffix as its year.

This screen has false positives and false negatives: “replication” may describe a method, GitHub may be the subject of research, and a publisher's standard “data files are available” sentence can refer to code-only or restricted packages. Papers without these cues still need review. Add searches for product life cycles, R&D, invention, venture capital, and other relevant terms in later passes, recording changes and counts.

Before claiming comprehensive FT50 coverage, reconcile the scan with the active journal configuration, validate journal membership, check coverage gaps and exact boundary dates, and log paper-level dispositions. The initial scan included all files found, including potentially retired/non-FT journals. Calendar years 2006–2026 are an exploratory window, not an exact twenty-year interval. Online and issue publication dates may differ; store both when known.

## Verification gates for each published addition

1. **Paper identity:** confirm exact title, authors, journal, DOI and dates against publisher or institutional/author primary sources; corroborate with the local metadata or Crossref. Do not invent volume/pages for articles in advance.
2. **Explicit connection:** locate the paper section, endnote, supplement or author repository that explicitly identifies the dataset as used or released. A related topic or citation alone is insufficient.
3. **Dataset identity:** confirm the official provider/author repository, release/version, coverage, unit of observation, and relevant files. Prefer stable landing pages and persistent identifiers.
4. **Actual access:** follow the real file link. Check HTTP response and content, not merely a successful landing page. Inspect a CSV header/sample, archive listing, or a bounded byte range as appropriate. A 200 HTML sign-in/challenge response is not a successful download. Record any registration, application, payment or other restriction.
5. **Scope:** distinguish complete replication data, author-shared partial data, external public components, reuse copies, code-only material, and synthetic/example data. Do not label a whole study public because one figure uses a public series.
6. **Terms and accuracy:** use only documented license/access terms. “Publicly downloadable” does not imply unrestricted reuse. Record unknown licenses as unknown; do not infer CC0 from the original collection's license.
7. **Second check:** cross-check metadata and evidence independently, reconcile versions/years, check for duplicate entries, and make sure every displayed claim is supported. This is source verification, not full reproduction of a paper's results.

Do not bypass paywalls, authentication or bot challenges. Record what could not be verified and continue with another lead. Never contact authors unless the user authorizes it. Use bounded downloads for large archives; record that the full archive was not tested. Keep personal or restricted raw records out of public review logs.

## Catalog representation

`research-additions.json` holds a `papers` map keyed by DOI and a `datasets` array. Follow existing field names; inspect the parser/UI before introducing new taxonomy values.

Paper records include title, authors, journal, issue year, optional online date/volume/issue/pages, DOI URL, evidence URL, evidence section, verification date and a precise verification note. Dataset records include stable ID, title, topic, provider URL, description, years, access, geography, types, units, tools, designs where supported, tags, date added, date verified, scope notes, checked links, verification note, and `paperDois`.

Merge with an existing collection using its ID or matching URL rather than adding duplicates. Keep one dataset with multiple paper citations where appropriate. Preserve original date added; a later link check changes verified date, not the addition date. Never equate paper publication years with dataset coverage years.

Descriptions should be concise paraphrases. Cite papers by clickable titles for signed-in verified members. Keep limitations visible in dataset notes. Do not copy full publisher abstracts or copyrighted papers into the catalog.

## Review log and validation

Update both queue files when a listed paper's status changes. Use explicit statuses such as `Unverified metadata lead`, `Under review — actual files not yet checked`, `Verified public data component`, or `Code only — not a dataset addition`. An inaccessible link is `unresolved`, not proof that no public data exists. Record checked date, evidence location, file check and limitations in STATUS or a linked review log.

Before publication parse the JSON, verify unique IDs and valid paper references, merge against the current upstream catalog, and check URLs/date formats. Existing website checks are under `datasets/_tools/*.test.mjs`; when using them ensure their bundled inputs match the new authoritative fork data. Confirm the generated public feed contains no source URLs or protected citation links. Existing membership access tests are for changes to authentication/rules, not routine metadata additions.

After publication check the actual GitHub workflow outcome and live feed. Record the run URL/ID and dataset IDs, including unresolved checks. Update [STATUS.md](STATUS.md), [HANDOFF.md](HANDOFF.md) and this file where needed in the same work session.

## Practical access notes (added 2026-10-16)

- The INFORMS and some publisher sites answer automated requests with HTTP 403 challenges. Do not try to bypass them. Use Crossref for paper identity, author or institutional copies (arXiv, NBER, eScholarship) for text, and repository APIs for data.
- Repository APIs work without login: Zenodo `/api/records/ID` (file list, size, MD5), Harvard Dataverse `/api/datasets/:persistentId/?persistentId=doi:...` and `/api/access/datafile/ID`, OSF `/v2/nodes/ID/files/`. Check the license field, whether each file is restricted, and a real byte range or full stream.
- A repository record that names the paper (or the paper that names the record) is the explicit connection. Say in the entry when the paper's own full text was not read.
- Searching OSF by title filters is noisy and not evidence of absence.
- A good discovery shortcut: filter the priority queue for clues naming Zenodo, Dataverse, GitHub or OSF, then query the repository directly.

