---
title: HHS Wiki document formatting 
subtitle: Notes on format for the HHS Wiki documents
abstract: >-
  A collection of notes on the formatting and format tweaks used for  HHS wiki documents. These are set up to be both PDF standalone documents and HTML web pages for the Wiki. 
---
# Notes on HHS Markdown documents

These are some notes on the format and formatting tweaks used in the documents on the Hobart Hackerspace Wiki pages. 
They also describe the process used to compose the documents as PDF standalone documents and HTML web pages for the Wiki.

# Formatting choices

The formatted documents are intended to be read both on the HHS wiki web pages (ie on a screen) and as printed documents. Both forms are useful in the Hackerspace environment:  
- it's useful to keep printed instructions near the relevant tools, so that they can be consulted without having to refer to a device that may not be to hand.  
- conversely, the display of the pages via a searchable wiki allows much more convenient discovery and helps members to find what documentation, if any, is available relating to the task that they have at hand.  

With that requirement, it's important that only a single document source is used, so that inconsistencies in information don't creep in. For that reason, the document sources are in Markdown (more details on that below).

The printable documents are held in PDF format, derived from the  Markdown sources. The rendered form is date-stamped so that out-of-date documents can be identified. They are set up to be printed single-sided on A4 paper with corner stapling. If we get a duplex printer, simply change the value of `twoside` in the `hhs_header.yaml` file. 

The PDF typeface (TeX Gyre Pagella) is freely downloadable and was chosen for readability as well as looking good. That and the fine details of margin sizes etc were aesthetic choices on the part of the designer(Brian Marriott); feel free to evolve or otherwise change them over time.

The Wiki documents are derived from the same Markdown sources as the PDFs. In fact the Wiki server holds them in Markdown format and converts to HTML at display time.

# The process
We keep source files of our documents in a simple, universal format and and *render* them into a more visibly-structured format for distribution and reading.

## Source files
- Our documents start out as Markdown (`.md`) formatted files.
- Markdown is used because:
	1. It is clean and easy to compose, without details of format interrupting your thinking. You think at the level of document structure, not format.
	1. It is pure text and so doesn't require any particular proprietary software or operating environment. Any text editor can be used.
	1. As documents are pure text, it's extremely easy to apply source control to them.
	1. It is (relatively) standard.
	1. It's familiar to many of us as it's used across many tech environments, in particular:
		- GitHub
		- Discord and other online forums and instant messaging platforms
		- Software documentation, ReadMe files etc. (eg Python Docstrings)
	1. We already use it in some of our systems:
		- Our website (running on GitHub Docs)
		- Our Wiki

## Rendering the documents for viewing
We render the Markdown documents into both PDF and HTML for viewing. HTML is used for Wiki pages and PDF provides standalone documents that can be printed or viewed off-line. (The process of taking a code-like source file and creating a formatted, human-readable document is called "rendering".)

- Rendering the Wiki documents is easy - we simply post the text of the documents to the wiki and it formats them.
	- Behind the scenes the `wikmd` uses both `pandoc` and `LaTeX` in the same way that we do for the PDF files. This means that we get some consistency in formatting between the PDF & Wiki presentation.
- Rendering the PDF documents is a bit more complicated:
  - Briefly:
	- First they are processed with `pandoc`, which is a versatile document format converter. This transforms them to `TeX` format. (`TeX` is a typesetting language.)
	- `Pandoc` then passes them automatically to `LaTeX` (strictly: `xelatex`) for typesetting. This transforms a mixed stream of text and commands into (hopefully) cleanly-presented, easily readable document.
  - In detail:
	- There are some format settings that are consistent across all our documents. For these settings there is a header file in "YAML" format that is used for all documents. This is `hhs_header.yaml`.
	- There are other (content-related) metadata settings that are specific to each document (things like title, subtitle etc). These sit in a YAML header within the markdown document.
	- We also have some consistent settings for `LaTeX` that are applied via a `pandoc` template file (`hhs_template.latex`).
	- So we have:
	  - (format header + markdown source) + (template file) => `pandoc` => `LaTeX` => PDF document
	- Each program within that sequence has some specific settings to get a clean & consistent result.
	- This whole process is automated with a small script to ensure that the right arguments are applied to the various programs.

# Tweaks for `pandoc`
In addition to customising the template that `pandoc` uses to generate `LaTeX` code (discussed below), there are some settings passed to `pandoc` that directly affect the process.

- `raw_tex` is turned on. This allows pure `TeX` or `LaTeX` code snippets to be included in the body of the document and executed by `LaTeX` at render time. 

- `top-level-division=section` -- this allows Markdown top-level headings to be recognised as the highest level in the document. Without that, they could be seen as second level, with the highest level reserved for chapter headings.

- `highlight-style` -- this determines the styling applied to "fenced code blocks". "Fenced" code blocks are code blocks identified by three backticks or tildes before and after the block. If the opening triplet is followed by the name of the language of the code, the code's syntax elements will be highlighted and may be rendered against a coloured background.

# Tweaks for `LaTeX`
As `pandoc` passes the documents to `LaTeX`, it applies a pre-defined template to the resultant document. This template controls much of the actual format of the final document. `Pandoc` as installed has a standard template for this but we have made some adjustments to that template to suit our needs. We pass our template to `pandoc` via a command line argument.

## `LaTeX` packages added.
`LaTeX` is, by design, a highly extensible system, and extensions are applied with plug-ins that are called "packages". Details of `TeX` and `LaTeX` and package installation are [described below]().

The additional `LaTeX` packages are specified in the template. Their purpose and use are:

### `fancyhdr` and `extramarks`
`fancyhdr` is used to control headers & footers (using `\fancyhf`,  `\fancyhead`, `\fancyfoot`, `fancypagestyle`, `\headrulewidth` & `\footrulewidth`). These give fine and flexible control of the size and content of our headers and footers. 
`extramarks` is part of `fancyhdr` -- it's used for `\firstrightmark` and `\firstleftmark`, which provide footer references to where we are in the document structure.

### `datetime2`
`datetime2` provides sensibly formatted dates and times in our headers and footers and also extracts the current system date and time without using any external utilities (using `\DTMusemodule`,` \DTMlangsetup`)

### `titling`
`titling` allows us to adjust the format of the "title" on first page (using `\pretitle`)

### `wallpaper`
`wallpaper` is used to place a background image on the first page (using `\ThisULCornerWallPaper`). We use this image as a colourful page header.

### `pagegrid`
`pagegrid` is a package that adds a background graph paper-like grid to the formatted document. This is extremely useful when debugging layout issues. The package is left in the template but turned off for normal use in the common header file..

# Installing `LaTeX` and `TeX`

Depending on which `TeX` installation has been used, most of the packages are available without further installation. They just need to be loaded. 

`TeX` installations tend to be large -- in the Gigabytes, but they come with all the sub-packages as well as the commonly-used `TeX`/`LaTeX` font packs. The safest way to install a `TeX` environment is to install TeX Live. For full information go to [www.tug.org/texlive/](https://www.tug.org/texlive/).
  

# Code files
Included in this document here for reference (and possibly recovery) are listings of the code files that are necessary to implement all of the above.

## The common header file `hhs_header.yaml`
~~~ yaml
---
papersize: A4
fontsize: 11pt
mainfont: TeX Gyre Pagella
geometry:
  - layoutvoffset=0mm
  - includeheadfoot=true
  - top=10mm
  - head=5mm
  - foot=10mm
  - bottom=15mm
  - twoside=false
  - inner=25mm
  - outer=25mm
  - bindingoffset=10mm
listings: true
pagestyle: empty
toc: true
linkstyle: sansserif
linkcolor: DarkBlue
linkcontrastcolor: DarkBlue
urlstyle: italic
grid: false
---
~~~

## The shell script to run `pandoc`
As you can see, there are a lot of settings embedded.

``` bash
#!/bin/bash
pandoc -s -t latex+raw_tex --highlight-style tango \
 --from markdown --top-level-division=section \
 --pdf-engine=xelatex --template=hhs_template \
  -o $1.pdf hhs_header.yaml $1.md
```

Run it by providing the relevant file name as an argument (without the `.md` suffix). For example:

``` bash
./update_docs.sh notes
```

Will create a file called `notes.pdf` from `notes.md`, provided that `hhs_header.yaml`, `hhs_template.latex` and `hhs_banner.jpg` exist in the current directory.

## Creating the `pandoc` => `LaTeX` template
The template file that `pandoc` uses to construct input to `LaTeX` is about 700 lines long, so too big to include here. We do, however include a patch file to create it from `pandoc`'s standard template.
If the template file that we want `pandoc` to use is unavailable or `pandoc` is updated, we can recreate the template that from the small-ish (74-line) patch file appended to this document.

1. Extract the current current (as-distributed) default latex template into a file by use of the command:
~~~ {.sh}
pandoc -D latex > dist.latex
~~~
1. Copy the patch text below into a local file (`latex.patch`), apply it to the default file and then rename the new file:
~~~ {.sh}
patch dist.latex < latex.patch
mv dist.latex hhs_template.latex
~~~

### The patch file
This file was created by `diff -u dist.latex hhs_template.latex > latex.patch`

~~~ {.patch}
--- default_orig.latex	2024-08-04 09:49:18.902096552 +1000
+++ default.latex	2024-08-07 16:52:21.126119435 +1000
@@ -479,6 +479,24 @@
 $if(csquotes)$
 \usepackage{csquotes}
 $endif$
+$if(grid)$
+\usepackage{pagegrid}
+$endif$
+\usepackage[headings, myheadings, nocheck]{fancyhdr} % fancyhdr is used to control headers & footers (\fancyhf and \fancyhead&foot)
+\usepackage{extramarks} % part of fancyhdr - used for \firstrightmark and \firstleftmark
+
+\usepackage[useregional=text]{datetime2}
+\DTMusemodule{english}{en-AU}
+\DTMlangsetup[en-AU]{abbr=true}
+
+\pagestyle{fancy}
+\renewcommand{\sectionmark}[1]{%
+    \markboth{#1}{}}
+
+\usepackage{titling} % allows us to adjust the "title" on first page (\pretitle)
+
+\usepackage{wallpaper} % used to place a background image on the first page (\ThisULCornerWallPaper)
+
 \usepackage{bookmark}
 \IfFileExists{xurl.sty}{\usepackage{xurl}}{} % add URL line breaks if available
 \urlstyle{$if(urlstyle)$$urlstyle$$else$same$endif$}
@@ -519,6 +537,23 @@
 $endif$
   pdfcreator={LaTeX via pandoc}}
 
+\fancyhf{}% clear all header and footer fields
+\fancyhead[RO,LE]{\small{\thepage}}
+\fancyhead[C]{\textbf{\large{\thetitle}}}
+\fancyhead[LO,RE]{\small{\today{}}}
+\fancyfoot[RO,LE]{ \firstrightmark }
+\fancyfoot[LO,RE]{ \firstleftmark }
+
+\fancypagestyle{plain}{ %
+  \fancyhf{} % remove everything
+  \fancyfoot[C]{\textit{\DTMNow}}
+  \renewcommand{\headrulewidth}{0pt} % remove lines as well
+  \renewcommand{\footrulewidth}{0.2mm}
+}
+
+\pretitle{
+  \begin{center}\huge\sffamily\textbf}
+
 $if(title)$
 \title{$title$$if(thanks)$\thanks{$thanks$}$endif$}
 $endif$
@@ -549,6 +584,14 @@
 $endif$
 
 \begin{document}
+
+\renewcommand{\headrulewidth}{0.2mm}
+\renewcommand{\footrulewidth}{0.2mm}
+\ThisULCornerWallPaper{1.0}{hhs_banner_v4.jpg}
+$if(grid)$
+\pagegridsetup{top-left}
+$endif$
+
 $if(has-frontmatter)$
 \frontmatter
 $endif$
@@ -557,6 +600,7 @@
 \frame{\titlepage}
 $else$
 \maketitle
+%\thispagestyle{empty} % /maketitle overrides pagestyle
 $endif$
 $if(abstract)$
 \begin{abstract}
~~~


Applying the above patch to the installed `default.latex` file will produce about 700 lines of almost-unintelligible code, so it's best to put that directly into a file: `hhs_template.latex`

*Brian Marriott*
