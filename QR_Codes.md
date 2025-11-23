# Notes on customised QR Code generation

*Brian Marriott's  notes:-)*

## Purpose
We're trying to set up QR codes on posters near significant equipment, linking to documentation on the Hackerspace wiki. 
They look more acceptable and obviously Hackerspace-related if they have a log in them.
Properly set up this doesn't interfere with the readability of the code.

Created images are saved in a [`QR Codes` sub-folder of the `Stationery, signs, etc.` folder in our OneDrive store](https://hobarthackerspace.sharepoint.com/:f:/s/Committee/EkgTY-5QndBFowPNYvKfox0BoR1-x9SEdaoY2PTzs5aQuQ?e=e3gmbA).
They are then available for import into posters etc.

## Creation
We build them using `Inkscape` and the `Inkscape` QR Code plugin.

### Base document
Create a base document in `Inkscape`.

- Size (in `File` >> `Document properties...`):
	- 80x80mm
		- Set both `Format` and `Display units` to mm.
	- Note that, as Inkscape works basically in vectors, we don't need to specify a DPI at this point.
- Depending on what the default document size is for your installation of Inkscape, you may have to scale up the document view to see the base document.

### QR Code Generation
- Under `Extensions` choose `Render` >> `Barcode` / `QR Code` >> `QR Code ...`
  - parameters
	  - Add the relevant URL
		  - If it's for the Wiki, make it with the `wiki.local` prefix, eg: `wiki.local/3D_Printers`
		  - This makes it useful within the Space while keeping the text short. 
	  - Size 29x29 unit squares
	  - 8px/unit square
	  - Error correction - Q (25%)
	  - Mode `Bytes array` ("ALPHAnum" doesn't allow lower case)
	  - Latin 1 encoding
	  - Neutral smoothing
	  - Square shape
	  - Smooth square value 0.2

  This produces a vector image with the QR code inside a goodly white border.
  It includes a white background and small white border to properly cover the underlying QR code

- Slide the image over the base document - it should fit with a bit to spare.
- Scale the image to fit the document cleanly (hold CTRL to keep aspect ratio)
- Save the new document before you proceed - see [File title](#file_title) below.

### The Hacky logo
- Create a new layer *above* the current layer
	- Under `Layer` choose `Add Layer ...`
	- Call it "Hacky" for clarity
	- Use the `Layers and Objects` tool to ensure that it is the top layer
- Import the Hacky source file [`Hacky source 7x11.svg`](attachments/Hacky_source_7x11-kxzr34ldff7ygkwwnhxid75mnoh4.svg) into it.
	- Either download the file linked above and then import it into Inkscape
		- Select option `Include as editable object`
		- Set `DPI for rendered SVG` to 96
	- or use the `Import Web Image ...` tool (if that works for your installation).
- Slide it that so that:
	- its LH edge is 11 unit squares in from the LH of the pattern, and
	- its top edge is 9 unit squares down from the top of the pattern
- Then scale it so that the RH edge and bottom edge are the 11 and 9 respectively from RH and bottom of pattern
	- Once again hold CTRL to keep tha aspect ratio
- Note that the Hacky image includes a white background and small white border to cleanly cover the underlying QR code.

## Saving the file
Export the lot to PNG for import into Word or whatever.

- Use a resolution of 96 DPI. 
- This should create a PNG that's 302px square or thereabouts.

### File title
If this is a QR code linking into the Wiki, save it with a name that represents where it links to. 
So, for example a code linking to `wiki.local/3D_Printers` will have an SVG title of `3D_Printers.svg` and the exported PNG will be `3D_Printers.png`

Created images are saved in a [`QR Codes` sub-folder of the `Stationery, signs, etc.` folder in our OneDrive store](https://hobarthackerspace.sharepoint.com/:f:/s/Committee/EkgTY-5QndBFowPNYvKfox0BoR1-x9SEdaoY2PTzs5aQuQ?e=e3gmbA).

