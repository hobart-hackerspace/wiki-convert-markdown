# Brian's wishlist for things he'd like to see in Wikmd to make it more useful for our needs
PLease add your own suggestions, but put your name on them so that Brian can follow up.

## Localised software
A preliminary to doing anything is the ability to either:

- run the docker image in a fork of the primary repository or
- run from a fork of the Github repo.

Either of these would allow us to develop some of the capabilities listed below (and feed them back upstream). 

## Author identification/authentication
- We need to be able to track who is adding/editing content
	- Maybe link create/update to github users?
		- Would this be too much of an inhibitor?
- Do we want pages to be publicly visible?
	- Maybe authenticate using emmail address & RFID no

## Styling
- Local CSS adjustments
- Header & footer customisation
- Move "Edit" & "Save" to header so they are always available

## Within pages

- Extraction of YAML header information for use as link rollovers
- Within-page ToC (similar to that provided by Jekyll)
	- Ability to float this so that it stays in the window

## Pages structure

- Multi-level page structure (this may actually exist - yet to be explored)
	- Recognition of "/" in page name
	- Multi-level site ToC in `/list` ("All files" page)

## Attachment handling

- Can webserver (`Flask`, presumably) recognise links to other file directories?
- Upload of PDFs in a way that makes them available for linking and page viewing.

## Page editing

- Provide a (ajax?) facility to add comments to end of page without having to edit the whole thing.