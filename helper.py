from pathlib import Path
import bibtexparser

THIS_DIR = (Path(__file__) / "..").resolve()
PAPERS_DIR = THIS_DIR / "papers"


bibs = [p for p in PAPERS_DIR.iterdir() if str(p).lower().endswith(".bib")]
pdfs = [p for p in PAPERS_DIR.iterdir() if str(p).lower().endswith(".pdf")]

parsed_bibs = {}
for b in bibs:
    with b.open() as f:
        parsed_bibs[b.name] = bibtexparser.load(f).entries[0]


def get_global_context() -> dict:
    return dict(parsed_bibs=parsed_bibs)
