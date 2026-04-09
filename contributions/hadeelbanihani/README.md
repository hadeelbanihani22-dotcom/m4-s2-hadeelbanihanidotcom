# AI.SPIRE Module 4 — Shared Chart Gallery

A class-wide gallery of polished data visualizations from Module 4. Each learner contributes one visualization and reviews two peers' contributions.

**Honors Track.** This stretch assignment is not required for program completion but counts toward Honors distinction.

---

## How to Contribute

1. **Fork** this repo to your GitHub account
2. **Clone** your fork locally
3. Create a branch: `chart-gallery/your-github-username`
4. Create a folder: `contributions/your-github-username/`
5. Add your files (see format below)
6. Commit, push, and open a PR to this repo's `main` branch
7. Review two peers' PRs (see review guidelines below)

---

## Contribution Format

Your folder `contributions/your-github-username/` must contain:

| File | What it is |
|---|---|
| `chart.png` | Your polished visualization (at least 800×600, PNG) |
| `generate_chart.py` | The Python script that produces `chart.png` — must run independently |
| `README.md` | 100-word write-up: what data, what finding, why it matters |

### Chart Quality Checklist

- [ ] Finding-based title (states the insight, not just the data)
- [ ] Labeled axes with units
- [ ] Colorblind-safe palette (viridis, cividis, or Seaborn colorblind)
- [ ] No chart junk (unnecessary gridlines, 3D effects, decorative elements)
- [ ] Annotations on key data points if applicable
- [ ] Saved with `fig.savefig('chart.png', dpi=150, bbox_inches='tight')`

---

## Peer Review

Review **two** open PRs from other learners. For each, leave a review comment with:

1. **One thing the chart does well** — be specific (e.g., "the sorted horizontal bars make the comparison easy to read")
2. **One improvement suggestion** — reference the chart type framework, Gestalt principles, or annotation practices from the Module 4 reading (e.g., "consider adding value labels at the end of each bar so exact numbers are visible without hovering")

---

## Submission

Paste your PR URL into TalentLMS → Module 4 → Thursday Stretch.

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
