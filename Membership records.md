**Membership records processes**

## Records management
Records are currently derived from TidyHQ.

## Extracting from TidyHQ
When exporting member lists from TidyHQ to update the door controller or get membership counts:

1. Log in to TidyHQ (https://hobarthackerspace.tidyhq.com/. as a user with admin rights
2. Go to the Admin dashboard
3. Select `Memberships` >> `Reports`
4. Next to `Membership level`, select `All`
5. Click `Options` and select fifteen (15) fields:
	- First col
		- Membership Level	
		- Contact
		- Contact ID
		- Start Date	
		- End Date	
		- Status	
		- Registered	
	- Second col
		- First Name	
		- Last Name	
		- Nickname	
		- Contact Email	
	- Third col
		- Phone	
	- Fourth col
		- (none)	
	- Last col
		- RFID Tag
		- Door access only
		- Member badge issued
6. Click `Search` then sort by End Date descending
7. Click `Export CSV` and save to the `Members` directory.
	- If you have a replica of the Committee OneDrive folder, this is a single step process.
	- Otherwise, export it to you local storage and then upload to the OneDrive folder (see below).
8. Adjust the file name if necessary.
9. Move the previous dated CSV to the `Archive` directory.

## Monthly membership stats reporting

1. The files for this are stored within [the `Members` directory in the Committee area of our Microsoft365 OneDrive store](https://hobarthackerspace.sharepoint.com/:f:/r/sites/Committee/Shared%20Documents/Members?csf=1&web=1&e=2xMyNv).
	- This is within the Committee share, and you have to be logged in to modify or create files in this directory.
1. Open the most recent (last month's?) `memberships_<date>.xlsx` file and save with the current date.
1. Move the old one to the Archive sub-folder.
1. Open the CSV file exported from TidyHQ with Excel.
	- Allow the leading zero conversion to take place.
	- As a sanity check, you should have 16 cols (`A`-`P`) and over 200 rows.
1. On the CSV spreadsheet, copy all columns with data (but no more). Include the headings.
1. On the new `.xlsx` spreadsheet click in cell `A1` and paste using `Paste values`
	- This should populate the spreadsheet with the current values and update the "Membership counts" table in the top right corner.
1. Ensure that the page layout includes just the "Membership counts" table, then either:
	- Print to PDF or
	- Select the "Membership counts" table and `Save as` a PDF.

## Processing to update door system
The TidyHQ CSV can be processed by Brian's Python script (thq2db.py),
to create both:

- a current local SQLite database and
- a file for Mailchimp.

(Note that that script runs in a Python virtual environment - see the associated `read_me.pdf`)

You still have to manually export the new database to the Door Controller:
``` bash
scp -P 8386 ./xxx.db pi@office.hobarthackerspace.org.au:~/HHSAccessControlV4/
```

## Mailchimp mailing lists
The python script mentioned above produces a Mailchimp-compatible CSV file.
Use that to import to Mailchimp, and assign a suitable tag to the imported records. Date (or month) works well.
