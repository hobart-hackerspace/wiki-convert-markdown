# The Membership System

The membership system at the moment is TidyHQ (often abbreviated in this document as 'THQ'). This is the external system that you pay your membership to, so you have a login to it already. Committee members should have admin access to this system - if you don't, ask Brian or Leo to set you up.

1. Log in to [TidyHQ](https://hobarthackerspace.tidyhq.com) (it's an externally hosted & maintained system). Once you're logged in, it should bring up a page with a big (pixelated) copy of our logo and not much else.
1. Click on the little square in the top RH corner that has your initials. If you have admin access, it will include in the dropdown a link to the dashboard. Click that. That should bring up the admin dashboard.

# Verification of a Member's details
1. Click on `Contacts` on the LH navigation list. It'll bring up a page with a few names on it, starting with the THQ account itself.
1. Type some part of the member's name into the `Name, Phone, ID, ...` field and hit return. It should bring up a short list of names (likely only one). Click on the relevant person (the underlined actual name).
1. Check that in the `Groups` box is included `Current Members`. You should also see an `Active` membership in the list below that.
1. If you're setting up a member's RFID:
	- In the page that comes up there is a `Contact Details` block that includes an `ID Number`. 
		You'll need that ID number to give to the door controller.
	- Keep that page open - you'll need to go back to it to provide the RFID number when you've allocated and confirmed it.

# Getting a list of members
1. From the admin dashboard, select `Memberships` >> `Reports`
3. Choose a Membership Level appropriate for what you need (most likely *Active* or *All*)
4. Click on Options and select all of: 
	- Membership Level	
	- Contact	
	- Start Date	
	- End Date	
	- Status	
	- Registered	
	- First Name	
	- Last Name	
	- Nickname	
	- Contact Email	
	- Phone	
	- RFID Tag
	- Door access only
	- Member badge issued
5. Click `Search` then sort by End Date descending
6. `Export CSV` and choose a file name.
1. There is [a Python script](https://hobarthackerspace.sharepoint.com/:f:/s/Committee/Eps4lcgNIO9MvPD3DqaEmdcBnXzkc4ulAWxUGtWNAX-HUg?e=IkrVGl) to process this file.
	- The script will read an export file of the above form to produce:
		- a complete SQLite3 database and
		- a Mailgun import file. 
	- Note that this script needs to be run from a directory on your local machine.

