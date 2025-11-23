
I have added a few more items for discussion at the end of the document - David Giffard



# Draft CNC usage rule ideas – for discussion purposes only

# 1. Conditions of Use
## All persons that use, or come into contact with, the CNC router system MUST:  

-  understand what a CNC router is and can do 
-  read and understand the content of the user manual prior to using the system 
-  be able to exercise control of the router system at all times 
-  follow all the guidelines presented including the use of appropriate PPE 
-  seek further instruction if anything is unclear 
-  be sure that you have understood these instructions completely 

# 2. Checklists

**If any issues are found, *DO NOT USE THE MACHINE* but report the issue(s) using:**
 - the machine condition report sheets on the clipboard.
 - To the CNC machine manager Mark Pearson.

## Pre-Use Checklist (Before Operation or Between Operators)

### Machine Condition:

- Inspect for visible damage, loose fasteners, or worn cables.
- Check emergency stop button function (note this powers down controller so only do it on initial power up.) 
- Confirm machine bed & spill board area is clean and free of obstructions.

### Power & System:

- Turn on main power; check for error lights or alarms.
- Verify coolant level.
- Check operation of dust extractor.
- Turn on control computer, log in and start the `UCCNC` program.
- Confirm proper homing of all machine axes.
- Verify that the machine stops within soft limits without triggering limit switches on all 3 axes.

### Tooling:

- Inspect tool condition (sharpness, no damage).
- Ensure correct collet and tool length for the job.
- Confirm tool is securely mounted in spindle.

### Material & Workholding:

- Material securely clamped/fixed.
- Zero position confirmed (machine/home/work offsets set).
- Check for clearance in all axes during the programmed operation.

### File & Program:

- Verify correct G-code file is loaded.
- Confirm units (mm/inch) match setup.
- Perform a dry run (with spindle off) if uncertain, running a new file or settings have been changed.


## Shutdown Checklist

### Machine

- Remove and store your tools and collets.
- Put spanners, tool touch off puck etc away in correct drawers.
- Clear spill board area and sweep it down.
- Turn off power at the wall.

### Computer

- Place any workfiles that you'd like to keep in a directory under your name (*on the desktop?* -- *in the Documents folder?*)
- Remove any unwanted files that you've created or loaded.
- Shut PC down fully before powering off.
	- If it wants to do an update, let it do it.
- Power off at the wall

### Usage log

- Log your use on the sheets provided
	- Date
	- Name
	- Approx Hours
	- Class of use

# 3. Maintenance Schedule

## Daily:

- Wipe down machine, clean dust from surfaces, especially leadscrews.
- Check dust collection bag and empty if it's more than half full.
- Visual inspection for loose fasteners, damaged cables.

## Weekly:

- Lubricate linear rails/ball screws (as specified by manufacturer).
- Check spindle runout (visually or with dial indicator).
- Inspect collets for wear or damage.
- Check cooling system fan operation.

## Monthly:

- Inspect spindle bearings for abnormal noise/play.
- Test emergency stop, limit switches and tool touch off puck.
- Clean inside electrical cabinet (if accessible).

## 6-Monthly

- Flush and refill cooling system

## Annually:

- Full service by qualified technician (spindle, electronics, alignment).
- Replace worn collets.
- Check all axis calibration and backlash.

# 4. Recommended Tool & Collet Sets

## Beginner / Soft Materials (e.g., MDF, Plastics):

- 1-flute or 2-flute straight cutters, Ø3mm to Ø6mm
- 1/4" and 1/8" ER 20 collets
- Surfacing bit (e.g., 22mm flycutter)
- V-bit for engraving (e.g., 60-degree)

## Intermediate / Woods & Composites:

- 2-flute spiral up-cut and down-cut, Ø3mm to Ø6mm
- Compression bits for plywood
- ER20 collet set (1mm to 7mm range)
- 90-degree V-bit for signs

## Advanced / Hardwoods & Aluminium:

- Coated carbide 2-flute end mills Ø3mm to Ø6mm
- Ball nose end mills for 3D carving
- ER 20 collet set, high precision
- Mist coolant setup (for metals if applicable)

## Alternate suggestion: Approx $140 from BG Precision

- 3mm Downcut Endmill
- 6mm Downcut Endmill
- 3mm Upcut Endmill
- 6 mm Upcut Endmill
- 3mm Ball Nose Endmill
- 6mm Ball Nose Endmill
- 60deg V-Bit 
- 30mm Surfacing Bit

**Note:** Ensure only rated, manufacturer-approved tools and collets are used to avoid spindle damage.

# 5. Operator Experience Criteria

## Absolute Beginners:
- Must complete Hackerspace CNC induction.
- May only operate under supervision.

## Basic Operators:
- Minimum of 2 supervised sessions completed.
- Demonstrated ability to safely load/unload tools and materials.
- Can run pre-approved jobs independently.

## Advanced Users:
- Minimum of 10 hours logged CNC time.
- Can perform basic toolpath setup (CAM) and troubleshooting.
- Authorised to mentor new members.

## External Experience Recognition:
- Prior CNC experience may be recognised with assessment by a Hackerspace mentor.

# 6. Basic CNC Induction Guide (Outline)

## Session Duration: ~1.5 hours

## Topics Covered:

### Safety First:
- Emergency stop procedures
- PPE requirements (eye/ear protection)
- Danger zones to avoid.
- Handling tools and sharp components

### Machine Introduction:

- Overview of machine axes and components
- Explanation of control system (UCCNC)
- Power-up and shutdown sequence

### Tool & Material Setup:

- Installing and securing tools
- Workholding principles
- Zeroing (setting work origin)

## Basic Operation:
- Loading G-code files
- Understanding simple G-code structure
- Running a test file (supervised)

## Post-Use:

- Cleaning procedures
- Reporting issues and logging usage
- Storage of tools and accessories

## Assessment:

- Hands-on demonstration of safe machine start-up, tool change, and running a simple job.



***Additional comments from David Giffard

1. Mandatory Rule – Operator Safety and PPE
Operators must follow standard industry safety practices at all times, including:

Long hair must be tied back.

Eye protection is mandatory while the machine is running.

Hearing protection must be worn if noise levels are deemed excessive.

Loose clothing is not permitted.

Items such as ties, scarves, or dangling jewellery are strictly prohibited.

Rationale:
A tool breaking at 24,000 RPM becomes a dangerous projectile. Loose items pose a serious entanglement risk.

2. Mandatory Safety Rule – Spindle Disengagement and Tool Changes
All users must be trained and demonstrate how to properly disable the spindle before changing tools.

While a tool change is underway, no other person shall touch the machine or computer.

Any infraction of this rule will result in a penalty (e.g. retraining, access suspension).

Rationale:
Tool changes are high-risk actions and must be performed with full operator control and zero external interference.

3. Mandatory Rule – Avoidance of Tool Collision
Operators must be able to explain how their G-code prevents collisions with clamps, fixtures, or other obstructions.

They must understand Z-clearances, entry/exit paths, and fixture locations.

Rationale:
Collision avoidance is a basic responsibility. Running code without spatial awareness is unsafe and unacceptable.

4. Mandatory Rule – No Damage to Spoil Board
Operators must not damage the machine spoil board under any circumstances.

Rationale:
This rule encourages deliberate planning and reinforces the operator’s confidence in where every tool movement will go.

5. Mandatory Rule – Responsibility for Chip and Spoil Removal
One person must be assigned responsibility for cleaning at the start of each session.

That person is responsible for:

Cleaning chips, dust, and spoil from the machine and surrounding area.

Emptying the dust and chip collector without fail at the end of the session.

Being trained in how to properly and safely perform this task.

Rationale:
Ensures accountability, cleanliness, and proper maintenance practices are consistently followed.

6. Discussion Point – Fine Dust Is Inevitable
It must be accepted that fine airborne dust will settle in the area, regardless of how effective the current extraction system is.

The group should actively consider mitigation strategies such as:

Secondary air filtration

CNC machine enclosures or containment curtains

Scheduled deep cleaning

Air quality monitoring solutions

Rationale:
This is both a health and equipment issue. Ignoring it will result in long-term build-up and possible member exposure.

*** end of additional comments by David Giffard