# Tanishk Gupta — GitHub Profile README

## What changed

This second pass treats the profile as a designed developer landing page rather than a decorated Markdown résumé. The visual anchor is now an owned, source-controlled profile banner with a T monogram, command-line metadata, and the positioning statement **Build systems. Solve problems.** The projects carry the visual center of gravity through four custom previews, while the text stays compact and evidence-led.

The README follows this journey:

> identity → current status → selected work → engineering lens → stack → problem solving → now / next → proof of progress → activity → contact

The layout uses only GitHub-compatible Markdown and HTML. There is no JavaScript, no fake interactive control, no contribution snake that requires a workflow, and no hard-coded follower/star counter that will become stale.

## Files to add

Copy the delivered files into the root of the profile repository `tan-ishk007/tan-ishk007` using this structure:

```text
README.md
assets/
├── profile-header.png
├── studenthub.png
├── readmeforge.png
├── portfolio.png
└── portfolio-v1.png
```

The five PNG files are the production assets referenced by `README.md`. Their corresponding SVG files are also included in the delivery as editable source files:

```text
assets/
├── profile-header.svg
├── studenthub.svg
├── readmeforge.svg
├── portfolio.svg
└── portfolio-v1.svg
```

The SVG source files are not required for the profile to render. They are provided so the visual system can be edited later without recreating the assets from scratch. The PNGs are used in the README because they render consistently across GitHub’s image pipeline and do not depend on remote font support.

The delivered `generate_assets.py` file is optional. It deterministically regenerates the PNG assets from the source layout and installed fonts; it is not required in the GitHub repository unless Tanishk wants to maintain the assets programmatically.

## Why each supporting file exists

| File | Purpose | Required at runtime? |
| --- | --- | --- |
| `assets/profile-header.png` | Branded hero banner and identity anchor. | Yes |
| `assets/studenthub.png` | Project visual for the academic resource-sharing platform. | Yes |
| `assets/readmeforge.png` | Project visual for the live README workbench. | Yes |
| `assets/portfolio.png` | Project visual for the advanced motion-led portfolio. | Yes |
| `assets/portfolio-v1.png` | Project visual for the earlier structure-first portfolio. | Yes |
| `assets/*.svg` | Editable source versions of the five visuals. | No |
| `generate_assets.py` | Optional deterministic regeneration script. | No |

The complete content of every file listed above is included as a directly downloadable attachment alongside this guide. No placeholders are present in the README or assets.

## External services

Only two external services remain in the README:

| Service | Use | Configuration | If unavailable |
| --- | --- | --- | --- |
| [Skill Icons](https://skillicons.dev/) | Compact icons for the technology map. | None. | The stack headings and text descriptions remain visible. |
| [GitHub Profile Summary Cards](https://github-profile-summary-cards.vercel.app/) | One activity summary card. | None for the hosted endpoint. | The native GitHub contribution graph and the direct GitHub profile link remain available. |

The redesign deliberately removes hosted decorative headers, typing SVGs, profile-view counters, follower/star counters, streak stacks, random quotes, WakaTime, Spotify, and contribution snakes. This makes the profile more owned, less fragile, and easier to maintain.

## Setup

Create or open the public repository named exactly `tan-ishk007` under the `tan-ishk007` account. GitHub displays a profile README when the repository is public, the repository name matches the username, and a non-empty `README.md` exists in the repository root [1].

Replace the repository’s root `README.md` with the delivered file. Copy the five production PNG assets into the repository’s `assets/` directory. Commit and push both the README and assets to the default branch.

No secret, personal access token, workflow, build command, or deployment step is required. GitHub will render the local PNGs directly from the profile repository.

## Verification checklist

Open `https://github.com/tan-ishk007` after pushing and check the following:

| Check | Expected result |
| --- | --- |
| Hero | Custom T monogram, tagline, metadata, and status block are visible as one coherent banner. |
| Work | Four project visuals appear above their project cards and link to the correct live demos/repositories. |
| Stack | Icons appear in three compact groups; the text-only labels remain understandable if icons fail. |
| Metrics | LeetCode shows the supplied 240+ / 1572 values. Codeforces shows the live-verified 1130 / 1131 values. |
| Activity | The summary card loads, and the direct GitHub profile link remains visible. |
| Mobile | Narrow the browser to phone width and confirm that project tables remain readable; GitHub may stack table cells depending on its renderer. |
| Accessibility | Confirm every visual has meaningful alt text and that the important claims are present as text. |

## Content maintenance

Update only the factual values when they change: LeetCode count/rating, Codeforces rating, CPI, project status, project URLs, and the Now / Next table. If an external service fails, remove its image tag rather than adding another competing widget. If a project changes materially, update both its short card copy and its local visual so the visual remains an honest summary rather than an invented screenshot.

## Final audit

| Area | Result |
| --- | --- |
| Premium visual identity | Pass — custom profile banner and custom project visuals create a distinct authored system. |
| Personal branding | Pass — T monogram, command-line language, MNNIT identity, full-stack/DSA focus, and understated personality are specific to Tanishk. |
| Project emphasis | Pass — projects are the first major content section and each has purpose, stack, architecture signal, links, and a visual. |
| Restraint | Pass — two external services, one compact activity card, no badge wall, no duplicate analytics. |
| Credibility | Pass — project details come from the supplied source material and inspected repositories; no unsupported employment or certification claims were added. |
| Interactivity | Pass — links and `<details>` are real GitHub-compatible interaction; no JavaScript is implied. |
| Graceful degradation | Pass — important information remains visible as text if local or remote images fail. |
| Accessibility | Pass — local assets include accessible alt text in the README and semantic titles/descriptions in SVG source. |
| Visual QA | Pass — all five production PNG assets were inspected after correcting an SVG font-rendering issue. |

## References

[1]: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme "GitHub Docs — Managing your profile README"

[2]: https://github.com/vn7n24fzkq/github-profile-summary-cards "GitHub Profile Summary Cards — API documentation"

[3]: https://github.com/orgs/community/discussions/193030 "GitHub Community — external image rendering discussion"
