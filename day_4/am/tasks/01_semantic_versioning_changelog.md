TASK 01 — Semantic Versioning & Changelog Practice
===================================================

Goal:
-----
1. Write clear, standardized changelog entries for a real scientific package.  
2. Decide the correct next semantic version (MAJOR.MINOR.PATCH) based on the changes.  
3. Record a brief rationale explaining your version bump.

Why this matters:
-----------------
- Ensures collaborators (and future you) immediately understand what changed.  
- Ties code versions to experimental results for reproducibility.  
- Prevents accidental breaking changes by signaling impact level.

---

Step 1 — Fill in the Changelog Template
---------------------------------------

1. Open the task's `CHANGELOG.md`.  
2. Locate the `## [Unreleased]` section and replace the placeholders exactly as follows:

   ```markdown
   ## [Unreleased]

   ### Added
   - Export processed data as JSON files for easier downstream analysis  
     (ensures flexibility in data pipelines)

   ### Fixed
   - Corrected rounding error in standard-deviation function (was truncating .999 →0.99)  
     (improves accuracy of statistical summaries)

   ### Changed
   - Refactored `plotting.py` to Matplotlib 4.0 API (updated axes object return patterns)  
     (maintains compatibility with latest plotting features)
   ```

3. After each bullet, in parentheses, state **why** that change matters.

---

Step 2 — Choose & Apply Your Next Version
-----------------------------------------

1. Review each change’s impact:
   - **Patch** = only bug‑fixes  
   - **Minor** = added features/new functionality (backward‑compatible)  
   - **Major** = breaking API changes
2. Decide the bump level—for these entries, e.g. **Minor** (new feature + non‑breaking refactor).  
3. Rename the header and add today’s date:

   ```markdown
   ## [0.2.0] – 2025‑07‑17
   ```

4. Directly under that header, write a one‑sentence rationale, for example:
   > Bumped to 0.2.0 for JSON export feature and non‑breaking Matplotlib refactor.

---

Step 3 — Peer Review & Finalize
--------------------------------

1. **Pair up** with a colleague and exchange your updated `CHANGELOG.md`.  
2. **Verify** you both agree on:
   - The clarity of each entry.  
   - The chosen version bump (patch/minor/major).  
   - The quality of the rationale.  
3. Each pair should suggest **one improvement** to make the changelog more descriptive.

---

**Deliverable:** A completed `CHANGELOG.md` file with:
- The new entries under `[0.2.0] – 2025‑07‑17`  
- Clear “why” annotations for each change  
- A concise rationale sentence for the version bump  

---
