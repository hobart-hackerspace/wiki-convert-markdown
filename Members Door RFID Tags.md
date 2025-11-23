# Door tag management
**(Registration and changing of door fobs/tags)**

Members are provided with RFID tags to enable 24/7 access to the Space.
The door tags are read by the RFID reader outside the door, and processed by the Raspberry&nbsp;Pi&nbsp;Zero just inside the door.
Members' tag RFID numbers are also stored on our membership system [TidyHQ](https://hobarthackerspace.tidyhq.com). So when a member joins or we replace a tag, we have to update both systems.

## Issuing or renewing a tag for a member

If a member has no tag (new member or lost tag), get a new one from the tags store. This is the top drawer of the small chest of drawers in the back of the Bertrand Russell room.

Wave the tag past the tag reader to verify that it works. If the reader beeps once the tag is ok.

The tags have a number printed on the outside, but it's best to confirm that that matches the number that is stored within. That's easy to do by accessing the controller. [See steps [1:5] below under "Updating tags on the door controller".](#updating-tags-on-the-door-controller)

Before we add the tag to the controller, it's prudent to verify the member's registration in our membership system. (This helps to avoid spelling errors in the name, allows us to find the membership number, and verifies in passing that they have actually paid their membership.)

## Accessing the Membership System

The membership system at the moment is TidyHQ (often abbreviated in this document as 'THQ'). This is the system that you pay your membership to, so you have a login to it already. Committee members should have admin access to this system - if you don't, ask Brian or Leo to set you up.

1. Log in to [TidyHQ](https://hobarthackerspace.tidyhq.com). Once you're logged in, it should bring up a page with a big (pixelated) copy of our logo and not much else.
1. Click on the little square in the top RH corner that has your initials. If you have admin access, it will include in the dropdown a link to the dashboard. Click that.
1. Click on "Contacts" on the LH navigation list. It'll bring up a page with a few names on it, starting with the THQ account itself.
1. Type some part of the member's name into the "Name, Phone, ID, ..." field and hit return. It should bring up a short list of names (likely only one). Click on the relevant person (the underlined actual name).
1. In the page that comes up there is a "Contact Details" block that includes an "ID Number". you'll need that ID number to give to the door controller in the next bit.
1. Check that in the "Groups" box is included "Current Members". You should also see an "Active" membership in the list below that.
1. Keep that page open - you'll need to go back to it to provide the RFID number.

## Updating tags on the door controller

This is done by logging into the controller from a terminal. Any terminal program on windows, Linux or MacOS will do, as will those on phones or pads.

1. Connect to the controller:

	 ~~~ {.sh}
	 ssh -p 8386 pi@office.hobarthackerspace.org.au
	 # (password is same as wifi)
	 ~~~

1. Change to the controller's working directory

	 ~~~ {.sh}
	 cd ~/HHSAccessControlV4/
	 ~~~

1. If you've scanned the tag to test it, it will show up in the log. Print the recent log entries to see it

	 ~~~ {.sh}
	 tail -20 access_log.log
	 ~~~

1. You should see some records like:

	 ~~~ {.sh}
	 2024-07-11 19:13:40,929;Tag scanned: 9520825
	 2024-07-11 19:13:40,951;Unknown ID.
	 2024-07-11 19:13:40,959;Multiple invalid tag attempts for Unknown
	 ~~~

1. Take note of the number after `Tag scanned: ` as that's the tag's RFID code. It should match the number printed on the outside of the tag.

1. Before modifying the controller database, we should copy the file to another name as a backup:

	 ~~~ {.sh}
	 cp -p members.db members_backup.db
	 ~~~

1. Listed towards the bottom of this document are several boilerplate SQL code blocks. There are examples there for:
	- [a new tag](#add-a-new-member), 
	- [updating a tag](#change-tag-for-a-member), 
	- [suspending a member](#suspend-a-member),
	- [reinstating a member](#re-activate-a-member) and
	- [deleting a member](#remove-a-member).

1. Pick the one that's relevant to what you're about to do and copy it into a text editor on your local machine. Then replace the relevant sample field contents (the ones with single quotes around them) with the actual values for `THQ_ID`,`firstname`,`lastname`&`RFID_no` as required for the particular need. THQ_ID is the "ID Number" from the THQ "Contact" information page.

1. Start the SQLite command processor by typing `sqlite3` at the linux command line
	 1. Then copy your changed command sequence from your text editor and paste into `sqlite3`.
		  Note that it's a classic Unix-style command so it won't tell you that you got things right, only if you have an error.
	 1. You can verify that your update went ok by typing:

~~~ {.sql}
		select * from members where 
			first_name = 'the_members_first_name';
		-- Don't forget the semicolon at the end.
~~~~

You should see a terse listing of the member's database entry. Something like:

~~~ {.sql }
		sqlite> select * from members where first_name = 'Jason';
		3000015|Jason|Hammond|7922112|activated|
		sqlite>
~~~~


Type `control/D` or `.exit` to terminate the command processor

## Adding the RFID to the Member Database

Now that you've identified the RFID code on the member's tag, you need to add that to the member database. This provides ain independent record of the tag that we've issued, so that we can cross-reference it with details in the door system. This is useful when things go wrong, as can too easily happen.

1. Connect to the membership system (if you're not still connected), [as described above](#accessing-the-membership-system).

1. Go to the member's contact page (the one that shows the ID number.)

1. At the bottom of that page is a field for RFID code. Add the code number to that field and save the record.

## Tidying up

- When you're done, copy the newly-updated .db file to one with today's date in the filename in the `DBarchive/` sub-directory within the controller's working directory:

	~~~~ {.sh }
	cp -p members.db DBarchive/members_`date -Idate`.db
	~~~~

- and then copy that to offline storage (preferably to our `Microsoft365 OneDrive` store, but at least to your local machine.) 
	 - The relevant OneDrive directory is:  
		`/Committee - Documents/Systems/Door controller/db archive/`
	 - Here is a link to that folder online:  
	  - [you'll need to log in with your `name.family@hobarthackerspace.org.au` credentials](https://hobarthackerspace.sharepoint.com/:f:/s/Committee/Ejbz-OQDDitGpETFAIVa2zcBEG_7fRNVQRTWhyNrZAdhTQ?e=5vh7rM)
- If you can't copy it to the OneDrive, please copy the updated .db file to your local machine and then email it to:  
	- [door.system@hobarthackerspace.org.au](mailto:door.system@hobarthackerspace.org.au)

- Note that for a long time we kept copies of the members database under git control with the source code for the door controller. This is now no longer the case as it caused confusion when updating the code. There is a copy in the source directory, but it's not kept up-to-date. Up-to-date copies are now only held in the archive directory.

# Boilerplate `SQLite3` commands

## Usage

Copy the relevant code snippet into an editor, replace the sample field contents with the desired values and paste into the `sqlite3` interpreter.

## Code snippets

### Add a new member
~~~~ {.sql }
.open members.db
BEGIN TRANSACTION;
INSERT INTO "members" 
	("id", "first_name", "last_name", "rfid", "status")
  VALUES 
	('THQ_ID','firstname','lastname','RFID_no','activated');
COMMIT;
.exit
~~~~

### Change tag for a member
~~~ {.sql}
.open members.db
BEGIN TRANSACTION;
UPDATE "members" set "rfid" = 'New_Number'
	 WHERE "id" = 'THQ_ID';
COMMIT;
.exit
~~~

### Suspend a member
~~~ {.sql}
.open members.db
BEGIN TRANSACTION;
UPDATE "members" set "status" = 'suspended'
	 WHERE "id" = 'THQ_ID';
COMMIT;
.exit
~~~

### Re-activate a member
~~~ {.sql}
.open members.db
BEGIN TRANSACTION;
UPDATE "members" set "status" = 'activated'
	 WHERE "id" = 'THQ_ID';
COMMIT;
.exit
~~~

### Remove a member
~~~ {.sql}
.open members.db
BEGIN TRANSACTION;
DELETE FROM "members" WHERE "id" = 'THQ_ID';
COMMIT;
.exit
~~~

*Brian Marriott*
