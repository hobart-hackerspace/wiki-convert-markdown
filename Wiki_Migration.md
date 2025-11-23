Some notes on where I'm at, what has to be done and what has been done in migrating the Wiki from `Wikmd` to `Obsidian`.

## Base plan
- Start from HHS `wikimd` files
- Establish a new `git` fork line and  replicate to Github
- Make base obvious changes like moving `img` dir to be `attachments` and fixing link syntax
- publish a trial
- work through each page to:
	- review content for necessity & currency
	- adapt from `wikmd` to `Obsidian` flavours of Markdown
## Immediate tasks
- Copy the files backup to a working directory
- Check that in to a new `Git` repository (not the old `Wikmd` one)
	- That gives a base point to work from.
	- Mark that as  a branch that's in sync with the live one: "`wikmd`"
	- Given that I've part started, I'll pause in this directory and start with a new "virgin" copy
		- Then when that's checked in, replace all files with those in my part-started directory and check those in as changes on a new branch: "`draft`"
- Change `/img/` dir to `attachments/`
	- Make the same change globally in the links within markdown files
- Change all indenting to tabs
- Look for some easy way to url-encode the link references
	- append their names with `.md`
- Then work through each page & check for mis-formatting
	- Adjust image sizes - post-link {} to prefix []
- Add a logo file
- And a suitable theme...