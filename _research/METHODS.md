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
- Discovery over the cloned site database: sparse-clone `lit/data`, `lit/data-ft50` and `lit/_scraper-ft50` from the site repository (`git clone --depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set ...`), load each `papers-*.json` list (fields: Title, Authors, DOI, Volume, Issue, Page, Year, Abstract, Journal) and regex the abstract. `journals.json` in `_scraper-ft50` defines the journal scope. OpenAlex lists `ft50` among a journal's classifications and can confirm scope per paper.
- Read an abstract's whole data sentence before trusting a repository word: a link to an Open Practices badge page is not a data location.
- When a record is public but anonymous requests show no files, do not add it; log it as an unresolved lead with the reason.
- For datasets containing personal data, state it in the entry notes and advise ethical use.
- DataCite quoted-DOI search is the best systematic finder: `https://api.datacite.org/dois?query="<paper DOI>"` returns deposits that mention the paper (Zenodo, Dataverse, Dryad, figshare, ICPSR, institutional repositories). A hit is a lead: confirm the deposit names the paper, then open the files. An ICPSR record that lists a paper in its bibliography does not by itself show the paper used the data.
- Publisher-hosted supplements (INFORMS, Wiley, SAGE) answer scripted requests with HTTP 403 or a challenge page; do not bypass them. Record such papers as unresolved and prefer open repositories.
- Government sites may return an HTML 'page not found' with HTTP 200. Open the downloaded bytes; for SAS transport files check for the `HEADER RECORD*****LIBRARY HEADER RECORD` text and parse with `pandas.read_sas(format='xport')`.
- For a dataset already in the upstream README, add a research record with the same `id` and `url`: the publisher merge replaces fields in place. Dry-run it with the repository's own `mergeResearch` and `parseCatalog` before pushing.
- Many replication packages contain inventor, author or repository-owner names. Say so in the entry notes.
- Named public datasets: regex the abstracts of in-scope papers for data-source names (Panel Study of Entrepreneurial Dynamics, Kauffman Firm Survey, Enterprise Surveys, Community Innovation Survey and so on), read the sentence around each match, and keep only papers whose abstract says the data were used. Build the paper records from Crossref programmatically. Distinguish the public-use from the restricted version of a dataset, and cite only papers that used (or may have used) the public part; say so in the notes when an abstract does not tell.
- Registration-gated sources (ICPSR, World Bank Enterprise Surveys microdata): check the provider's own statement, the DOI or catalog record, and any public documentation file. State in the entry that no data file was opened. Do not log in or try to get around the challenge.
- Compare against `sbir.gov`-style hosts that answer 403 to scripts: record as not verified rather than guessing.
- Hosts that show an anti-bot page (Anubis, Cloudflare 'Just a moment', plain 403) cannot be verified by script. Examples met so far: INFORMS, Wiley, SAGE, SBIR.gov, ICPSR, the Bielefeld repository. Record the paper as unresolved.
- DSpace repositories such as NUS ScholarBank may show a public landing page and metadata but zero files in the original-files bundle for anonymous requests. Treat as 'files not visible'; do not add.
- Zenodo concept DOIs resolve to the latest version. When a record has many versions (Reliance on Science has 64), say which version was inspected and that an older version may match the paper; list `/versions?size=10&page=N` (larger sizes return HTTP 400).
- Dataverse datasets may mix public and restricted files; list `restricted` per file and say which part is public in the entry.
- Build paper records from Crossref programmatically, and always state in `verification` that the full text was not read unless it was.
- Mendeley Data deposits: `GET https://data.mendeley.com/public-api/datasets/<id>/files?folder_id=root&version=1` lists files with sizes, SHA-256 and a `download_url`; compare downloaded byte counts with the declared sizes. Title, license and the linked article come from DataCite (`10.17632/<id>.<version>`), whose `IsSupplementTo` relation names the paper.
- A DataCite record's `IsDocumentedBy` list is the data provider's own list of publications that document or use the data (used for the Mannheim Innovation Panel). It is provider evidence, but it does not say which data version a paper used.
- Application-gated survey data (for example ZEW scientific use files): read the provider pages for who may apply and for what, classify as 'Agreement or mixed', and state that no data file was opened.
- Dataverse records can list zero files; do not add them.
- Eurostat tables: `https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en` lists every table (CIS tables are `inn_cis<n>_*`); data come from `.../statistics/1.0/data/<code>?format=JSON&lang=en` (JSON-stat; `format=SDMX-CSV` is rejected with HTTP 400). Methodology pages sit under `/eurostat/cache/metadata/en/<code>_esms.htm`.
- GEM downloads: the data page is `https://www.gemconsortium.org/data/sets`. The buttons carry a `file` id and the page's own script posts it to `https://www.gemconsortium.org/download@file` (`id=<file id>`); this is the same call a visitor's browser makes and needs no login. Files unzip to SPSS (.sav); read with `pyreadstat` (`pip install --target ./lib pyreadstat`, then `sys.path.insert`).
- Where only an aggregate component of a survey is public (Eurostat tables) while the papers use restricted microdata, make the entry about the public component and say what the papers used. Do not cite restricted-data papers for a public-use file.


- Large files: a server may ignore `Range` and send the whole file (ClinicalTrials.gov's bulk zip did). For anything that might be large, first send a HEAD request or use `curl --max-filesize` and a time limit.
- Economics replication deposits (Harvard Dataverse) are often README-only, code-only, hosted on SharePoint or Dropbox, restricted to secure data centres, or contain synthetic 'pseudo' data. Read the README and file list for each before adding. A deposit with only pseudo data and code is not a dataset addition.
- `_research/archive/` now also holds the helper scripts used for this work: `datacite-inspect.py` (record metadata and file lists for Zenodo and Dataverse DOIs), `dataverse-report.py` (license, restricted flags and README clues for Dataverse records) and `openalex-fulltext.py` (open-access full text lookup). They write to local folders and call public APIs only.

