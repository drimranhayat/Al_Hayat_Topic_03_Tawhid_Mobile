# Al-Hayat Forty Hadith Series — Topic 003

## Tawhid and Worshipping Allah Alone

A standalone static website for Dr. Imran Hayat, containing forty source-linked hadith selections in Arabic, English and Urdu. This is the third topic in the finalized series catalogue. Topic 1 is a separate website and repository.

## Learning organization

1. The meaning and foundation of tawhid.
2. Sincere devotion to Allah.
3. Calling upon and remembering Allah.
4. Guarding speech and reliance.
5. Protecting worship and sustaining hope.

Each section has eight selections. This is an editorial learning order inspired by the broad subjects of the classical books of faith; it does not reproduce a single collection's table of contents.

## Focused learning

There are **46 explanatory Q&A and 40 MCQs**, with the count determined by each report's content. Short reports generally have one question; longer reports receive additional questions only for a distinct important point. Q&A explains the meaning in connected prose. Quizzes check selected points through interpretation and application. There are no repeated narrator, sanad, or grading templates used to inflate the bank.

Every editorial answer and MCQ has an exact anchor in the supplied text, explanation, or benefit, and an expandable supporting passage. Editorial prose and exercise distractors are clearly separate from transmitted hadith. Questions do not claim to exhaust every scholarly issue.

## Reading tools

- Read → Explanation → Q&A → Practice, with Back step, Next step and Main menu.
- Forty separate reading pages, with previous and next hadith at the top and bottom.
- Search in Arabic, Urdu, English, titles and references; section filters and direct entry selection.
- Distinct colors for languages, references and optional learning panels; day/night mode and text-size controls.
- Optional explanations, benefits, notes and practice stay collapsed until opened.
- Bookmarks, reading progress, private notes, study backups and memorization mode.

Topic 3 uses its own browser storage and backup format, `alhayat-topic003-v1`, separate from Topic 1. Quiz attempts use a topic-specific key. Data stays in the browser; there are no accounts or automatic synchronization. Export a study backup to keep a copy of notes and reading progress. Quiz scores are stored separately and are not part of that backup.

## Deploy the downloadable ZIP to GitHub Pages

Upload the **contents** of the ZIP to a repository root: `index.html`, `assets/`, `hadith/` and `sources.html` should be at the root. Choose Settings → Pages → Deploy from a branch → main → /(root) → Save.

No Node installation, secret, database, or build command is required to deploy the already generated files.

After GitHub provides the final URL, configure the search metadata:

```sh
python3 configure_seo.py --base-url https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/ --directory .
```

Upload the updated HTML, robots file and sitemap. The release includes canonical URLs for the public Al-Hayat site. Search ranking is not guaranteed.

## Sources and limits

Arabic, English and Urdu texts, explanations and benefits are reproduced from **HadeethEnc.com**, with original files in `source-data/`. All forty selected records are labelled Authentic by that publisher; references include Sahih al-Bukhari, Sahih Muslim, Sunan Abi Dawud and Jami at-Tirmidhi. Attribution is preserved, including other collections where the publisher names them. Publisher labels are not new independent authentication by this website.

Each entry links its publisher record and a primary-collection reference on **Sunnah.com**. Full chains are accessed through those references; missing transmitters are not reconstructed. Numbering and wording may vary. Publisher selections may omit material present in the primary version.

Snapshot: 17 October 2026. Interface: HadeethEnc API v1. The API supplies no separate publisher translation revision number; the retrieval date is not represented as a publisher edition. Retain publisher attribution and consult https://hadeethenc.com/en/home terms when reusing or maintaining the material. No affiliation with either source is claimed.

See `SOURCE_REVIEW.md`, `reference-provenance.json`, `reference-register.csv` and `content-manifest.json` for the checks, reference record, and source checksums. No independent specialist sign-off is claimed.

## Regeneration and checks

The portable ZIP uses the repository root as output:

```sh
python3 build.py
node scripts/check-site.mjs .
node scripts/check-learning.mjs .
python3 scripts/check_learning_sources.py .
python3 scripts/check_content.py .
python3 scripts/check_markup.py .
```

The development checkout writes to `dist/`; use `dist` in the check commands. Reapply URL configuration after regeneration.

`topic_config.py` sets the learning order, titles, primary references and Companion attribution. `learning_content.py` contains the editorial questions, explanations, hints and source anchors. `learning_builder.py` validates and assembles them. `source-data/` contains eighty original language records. Do not replace missing source text with generated material.

Arabic uses Amiri; Urdu prefers locally installed Jameel Noori Nastaleeq with Noto Nastaliq Urdu as the downloadable fallback. Fonts load from Google Fonts. Source links open external websites.

## Mobile reading update

Dedicated layouts for phones and tablets, including 320–430px screens: wrapping section buttons, stacked search and selectors, single-column study menus, larger text, 44px or larger action controls, wrapped pagination, safe-area spacing, and scrollable dialogs. The phone dock remains clear of the final content and notification messages. Arabic and Urdu keep normal word boundaries. Existing topics, source text, IDs and browser progress keys are preserved. Automated behavior/content checks pass; browser viewport and device visual testing was unavailable in this environment.


## Final reading layout
The homepage offers five trilingual section cards. The library shows eight compact cards per page; each opens one focused lesson with previous/next links and optional learning panels. All 45 Arabic editorial card headings have vowel marks. Urdu uses black text, with light surfaces in dark mode.

The original 40 hadith, 46 explanatory answers and 40 MCQs are preserved, including source wording notes and publisher grading qualifications. This focused question bank does not claim exhaustive coverage of all scholarly discussions. Browser progress IDs, question IDs and quiz storage keys are unchanged.

Public site: https://al-hayat-tawhid-worship.aquaearth3.chatgpt.site/
The release includes canonical URLs, unique descriptions, social metadata, structured data, robots.txt and a 44-page sitemap. Submit the deployed sitemap through your own Search Console account. Search indexing and rankings are not guaranteed.

Upload the ZIP contents directly to the GitHub repository root. Enable Pages from main / root. No build step, database or API key is required. Run `python3 build.py` to regenerate; reconfigure canonical URLs when moving to another host.
