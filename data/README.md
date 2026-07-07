# RAG corpus data

Raw source documents and derived artifacts for the Production RAG pipeline.
**Contents are git-ignored** (see root `.gitignore`) — only this README and the
`.gitkeep` markers are tracked. A fresh clone must re-download the sources below.

## Layout

| Dir | Contents | Notes |
| --- | --- | --- |
| `raw/` | Original source PDFs, untouched | Immutable ground truth. `rag/ingest/load.py` reads from here. |
| `processed/` | Extracted text, chunk caches, embedding caches | Fully derived — safe to delete and regenerate by re-running the ingest pipeline. |

## Sources

### Economic Survey of India

- **Official portal:** https://www.indiabudget.gov.in/economicsurvey/
- **All editions (archive):** https://www.indiabudget.gov.in/economicsurvey/allpes.php
- The Survey is published annually, one day before the Union Budget (~late Jan / early Feb).
  Each edition is a multi-hundred-page narrative PDF (macro trends, sectors, fiscal/monetary
  policy) — a good text-rich RAG corpus with verifiable Q&A.

**Download** the full-document PDF (or per-chapter PDFs) from the portal and place it in `raw/`, e.g.:

```
data/raw/economic-survey-2024-25.pdf
```

> Record here the exact edition you ingested so the eval set stays reproducible:
>
> - Edition ingested: _<fill in, e.g. 2024-25>_
> - Downloaded from: _<paste the exact PDF URL>_
> - Date downloaded: _<fill in>_
