# Project 1 — Production RAG: Build Plan

> Working plan for the flagship project in [`../PROJECTS.md`](../PROJECTS.md).
> Companion maps: [`../SYLLABUS.md`](../SYLLABUS.md) (AI knowledge) ·
> [`../PYTHON-SYLLABUS.md`](../PYTHON-SYLLABUS.md) (Python gaps).

## Starting picture

- **This repo is empty** — `main.py` is a hello-world, `dependencies = []`, empty
  README/requirements. Project 1 gets built here from scratch.
- **Existing RAG work** to extend: `AI-LANGCHAIN-BASICS/03-traditional-rag` — two
  notebooks (`01-document-loaders`, `02-rag-pipeline`) using ChromaDB. That's the
  toy we're turning into a measured, tuned, served system.
- ⚠️ **Settle first:** `pyproject.toml` pins `requires-python = ">=3.14"`. The ML
  stack (`torch`, `sentence-transformers`) often lags the newest Python. Verify
  wheels install on 3.14 — if not, pin to **3.12** (safest for ML) before anything.

## Guiding principle

Don't start with the shiny parts (hybrid search, reranking). Project 1's thesis is
**"measured, tuned, served"**, and the bar is *"show a before/after where a change
measurably improved retrieval."* That requires a **baseline + eval harness first** —
otherwise there's no "before" to compare against.

## Framework policy (LangChain?)

The "zero frameworks / no LangChain" rule was **specific to Project 0** (hand-roll
the agent loop). The projects are staged on purpose: hand-rolled loop (P0) →
directly-wired RAG components (P1) → orchestration framework, LangGraph (P2).

**For Project 1: wire the retrieval core directly — don't hide it behind LangChain's
RAG abstractions.** The thesis is "measured, tuned, served", and the tuning knobs
(hybrid fusion weights, rerank top-k, chunk strategy) are exactly what LangChain's
`Retriever` / `Chain` / `RetrievalQA` wrappers obscure. P0 already proved
framework-free competence; P1 should prove you understand RAG *internals*.

- ✅ **Fine to use LangChain for ingestion plumbing:** `langchain_community` document
  loaders (PDF / text / xlsx) and `RecursiveCharacterTextSplitter`. This is the §2
  chunking already done in `03-traditional-rag`; it hides nothing you're judged on
  and saves time.
- ❌ **Avoid for the retrieval core:** `RetrievalQA` / `Chain` / vectorstore-
  `Retriever` wrappers for `retrieve → rerank → generate`. Hand-wire these so the
  tuning knobs stay explicit and visible.

**Rule of thumb:** LangChain for *getting documents into chunks*; your own code for
*retrieval, fusion, reranking, and the eval loop*.

---

## Step 1 — Repo skeleton + `get_model()`  (~½ day)

Set up the `src/` layout, deps via `uv`, and the provider-agnostic `get_model()` shim
(swap Ollama / Groq / Gemini free).

- Python: §2/§3 of PYTHON-SYLLABUS — Pydantic settings, ABCs / `Protocol`, packaging.

## Step 2 — Naive RAG baseline, end-to-end  (~2–3 days)

Port the notebook into real modules: `load → chunk → embed → store → retrieve →
generate`. Move storage to **Qdrant** (easiest local Docker; choose pgvector only if
you want the SQL angle for Project 3). Keep it **deliberately dumb** — plain vector
search, no rerank. **This is the baseline to beat.**

## Step 3 — Eval harness (Ragas) + golden set  (~2–3 days)  ← the differentiator

Build eval **now**, against the naive baseline.

- Hand-write ~20–30 golden Q/A pairs from your docs.
- Wire Ragas: faithfulness, context precision/recall, answer relevance.
- Print metrics. Every later change is now measurable.

## Step 4 — Iterate, measuring each change  (~1 week)

Add one improvement at a time, re-run eval, record the delta:

1. Query rewriting — clean vague queries before retrieval
2. Hybrid search — BM25 (keyword) + dense (semantic), fused
3. Reranking — cross-encoder over top-k
4. Metadata filtering — by source / date / type

This is what *generates* the before/after story.

## Step 5 — Serve + trace  (~2–3 days)

Wrap in **FastAPI** (`/docs`, `Depends()` for the retriever), add **Langfuse**
tracing.

- Python: §4 async + §5 FastAPI of PYTHON-SYLLABUS.

---

## First action this week

Settle the Python version, scaffold the repo, get the **naive baseline returning an
answer** (Steps 1–2). Resist hybrid/rerank until the eval harness exists.

## "Done when" (from PROJECTS.md)

- [ ] Eval suite runs on a golden set and prints metrics
- [ ] A before/after where a change *measurably* improved retrieval
- [ ] Hybrid + rerank beats naive vector search on your metrics
- [ ] Exposed as a FastAPI endpoint with traced requests

**Stack:** sentence-transformers, Qdrant/pgvector, BM25, cross-encoder reranker,
Ragas, FastAPI, Langfuse, `get_model()`.
