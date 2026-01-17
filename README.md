# A little I made to assist in the conversion of WikMD markdown files to Obsidian markdown

**`WikMD`** is flexible with link formats. In particular:
 - it allows both standard MarkDown links `[displayed words](hidden URL)` and Wiki links `[[words which are also the link]]`.
 - For internal links:
	 - It allows the "URL" bit to have embedded spaces
	 - It doesn't add the `.md` suffix to file titles

The Python script in `main.py` brings these links into conformance with the Obsidian standard, and in the process enables them to be used by `Obsidian Publish` to produce clean HTML.

This script is set up to run under the `uv` package manager. The directory includes a `.venv` sub-directory which is not in the `git` repository, but will be created when you do a `uv sync`. 
