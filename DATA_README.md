# DATA_README — Automated Feedback Sentiment Analysis

**Last updated:** 2025-09-09

## Sources & Licensing
- **Source(s):** Replace with the actual dataset names/URLs (e.g., Kaggle product reviews, Twitter API data, academic corpora, or internal surveys).
- **Licence(s):** Respect original dataset licences. Do **not** commit proprietary or sensitive data.
- **This repo ships only tiny synthetic/sample data** to enable the pipeline and tests to run.

## Directory structure
```
data/
  raw/            # (not versioned) place original external datasets here
  interim/        # intermediate cleaned files
  processed/      # final data ready for modelling
  sample/         # tiny anonymised samples for demo (optional)
  bench.csv       # append-only benchmark log (one row per run)
  metrics.csv     # latest headline metrics (copied from the latest bench row)
```

## Reproducing the pipeline with sample data
1. Place tiny samples or synthetic data under `data/sample/` that mirror the schema of the real dataset.
2. Update paths in notebooks/scripts to read from `data/sample/` for demo runs.
3. Document any sampling, cleaning, or label-generation decisions here.

## Privacy & Ethics
- Avoid storing PII or sensitive text in the repository.
- If using API data (e.g., Twitter), cache only permissible fields and adhere to TOS.
- Clearly mark synthetic data.

## Notes
- Original build window: **Nov 2012 – Jan 2013** (as declared in the README/portfolio).
- Modernisation in **September 2025**: environment pins, tiny demo, smoke tests, CI, and metrics snapshot.
