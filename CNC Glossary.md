**A Glossary of terms used in CNC design and machining**

4th Axis
: An additional axis to a traditional 3-axis machine that enables the CNC to operate as a lathe.

Allowance
: This is the difference in dimensions of mating parts, some parts may require a tighter fit whilst others may need a looser fit.

Automatic Tool Changer
: Also known as ATC, is a system that automatically changes the tools in a CNC machine to fit whatever task is needed without the need for human operator interaction. The automatic tool changes are controlled by the G-Code commands.

Axis
: Direction of movement. On a three-axis machine: X (left-right), Y (front-back) & Z (up-down).

Ball End (Ball Nose)
: A cutting tool that has a rounded cutting arc tip, where the arc diameter is equal to the cutting diameter. This tool is typically used for cutting flutes, 3D toolpaths, pocket trays, cutting board juice grooves, and much more.

Ball-screw
: Drive system component. The ball-screw is rotated by the drive motor and provides the means for moving the gantry and/or spindle along an axis.

Bed
: The work surface top of your machine that a spoil board or material is placed on to be machined.

Bezier
: A vector curve that is defined by a set of control points and can be altered by moving the control handles. Also known as a smooth curve.

Breakpoint
: The point in a toolpath file where a break is created. In a job file, a breakpoint will allow you to stop work and save a location to resume from later. Not all machines are capable of this.

CAD
: Computer aided design using software

Caliper
: A very accurate device used to measure inside or outside dimensions.

CAM
: Computer aided manufacturing using software to define toolpaths and assist in manufacturing processes.

Chamfer
: The bevel or angular surface cut on the edge or a corner of a machined part.

Chipload
: Chipload is the measure of the thickness of a chip a cutter will cut. It is best to check with the manufacturer of the tool to optimize your feeds and speeds and get the correct chipload. This will allow you to get the best performance out of your tools and have them stay sharp longer.

CNC
: Stands for computer numerical control and is a machine that the movement is controlled by a computer using numerical (g-code) commands.

Climb Cut
: Refers to the relationship of the cutting tool rotation to the direction of feed. A climb cut deflects the cutting away from the cut, with the direction of the feed.

Closed Vector
: A vector with two or more arc or bezier curve segments or a vector with three or more straight line segments that connects with itself to form a shape. Sometimes a shape could look like a closed vector when nodes are touching but not connect to each other, it would be then considered an open vector until you join those nodes together.

Collet
: A metal collar that holds the cutting tool within a spindle nut.

Conventional Cut
: Refers to the relationship of the cutting tool rotation to the direction of feed. A conventional cut deflects the cutting toward the cut, against the direction of the feed.

Compression Bit
: A cutting tool with a combination of up and down shear cutting edges. Typically used for cutting plywood, veneer, or laminate material to prevent tear-out on both sides of the sheet.

Datum
: See Origin

Deflection
: Tool deflection occurs when the spindle speed and feed rate exert sufficient force to deflect the cutting tool. Deflection leads to excessive wear and chatter which can shorten tool life and will leave unwanted tooling marks on the material. 

Depth Per Pass
: The depth of which the tool will cut on each pass in the z-axis. If the depth per pass is set less than the material thickness, it will cut multiple passes until it reaches the final cut depth specified for that toolpath.

Down Cut Bit
: A cutting tool whose edges carve downward on the face of the material. This reduces the potential for tear-out on the top of the material but requires a slower feed-rate because the down flutes push the chips of material into the cut, rather than clearing them out.

Drag Knife
: A cutting tool that holds a razor or knife blade used to cut and inscribe material. Used with spindle or router motors turned off, the drag knife freely spins as it follows the direction of the toolpath. (Cut2D Pro, VCarve Pro, and Aspire can create toolpaths for this with the Drag Knife Gadget.)

Drill
: A pointed tool that is rotated to cut holes in the material. Normal drill bits usually require slower RMP spindle speeds to work properly.

Dust Shoe
: An accessory which aids in limiting the spread of dust and debris by channeling the airflow through an attached dust collection system.

End Mill
: A cutting tool with a straight end, typically with a spiral flute(s). It creates a channel with a flat bottom perpendicular to the sides. Commonly referred to as a “bit.”

Extrude
: Creates a 3D solid or surface by extending a 2D or 3D component. Extrusions can extend in any direction or be set to taper or follow a path.

Feed and Speed
: A combination of factors that must be set to control the work performed by the cutting tool. (See RPM, feed rate, plunge rate, and depth per pass.)

Feed Rate
: The speed at which the cutting tool moves along a workpiece in the X and Y axis.

Fixture
: A term given to the apparatus or structure that is holding your work which is often custom-made to hold your specific part.

Flute Length
: The length of the cutting portion on a router bit or cutting tool.

Flutes
: The cutting edges or inserts of a router bit or cutting tool. More flutes typically allow for more material removal, which in turn allows for faster feed rates. Although, some material machines better with less flute.

File Type
: Format at which a file is saved as. See different types below:

- **2D File Formats**:

	AI
	: Adobe Illustrator (.ai) is a proprietary file format developed by Adobe Systems for representing single-page vector-based drawings.

	CRV
	: CRV (.crv) is a CAD file created by Vecric software that saves the vector design geometry and includes toolpaths for machining the design.

	CRV3D
	: CRV3D (.crv3d) is similar to CRV above but is used for Aspire software only to be able to retain all of the 3D data.
	
	DWG
	: Drawing (.dwg) is a proprietary binary file format used for storing two and three dimensional design data and metadata. Typically used by AutoCAD software.
	
	DXF
	: Drawing eXchange Format (.dxf) is a file extension for a graphic image format typically used with AutoCAD. (DXF files usually add more nodes to smooth curve lines, making machining time longer. This requires additional node editing work to clean them up before making toolpaths.)
	
	EPS
	: Encapsulated PostScript (.eps) is a Document Structuring Conventions–conforming (DSC) PostScript document format usable as a graphics file format.
	
	PDF
	: Portable Document Format (.pdf) is a file format developed by Adobe to present documents and vector graphics.
	
	SVG
	: Scalable Vector Graphics (.svg) is a file extension for a vector image format for two-dimensional graphics.
	
- **3D File Formats**:

	3DCLIP
	: 3D Clipart files that are exported from Aspire. This format maintains the component structure of clipart pieces at the time of saving, so will import all the components comprising the clipart piece.
	
	3DM
	: 3DM (.3dm) is an open-source file format which is used for 3D graphics software.
	
	3DS
	: 3DS (.3ds) is one of the file formats used by the Autodesk 3ds Max 3D modeling, animation and rendering software.
	
	ASC
	: Action Script Communication (.asc) is a file written in script and is used by a particular application or program.
	
	CRV3D
	: CRV3D (.crv3d) is similar to CRV above but is used for Aspire software only to be able to retain all of the 3D data.
	
	DXF
	: 3D DXF (.dxf) files from AutoCAD and many other CAD orientated modeling packages, these must be 3D meshes and not just wireframe data of the models vertices.
	
	LWO
	: LWO (.lwo)Three-dimensional file created by LightWave 3D, a program used for 3D modeling, animation, and rendering.
	
	OBJ
	: Object (.obj) is a simple data-format that represents 3D geometry developed by Wavefront Technologies.
	
	PRJ
	: Project (.prj) file contains a project that may be created by a variety of different programs, such as AutoCAD.
	
	RLF
	: RFL (.rfl) is an ArtCAM 3D Relief model file format.
	
	SKP
	: Sketchup (.skp) is a three-dimensional model file created by SketchUp software.
	
	STL
	: Standard Triangle Language (.stl) is a fairly standard file extension for 3D objects. These models can be completely 3 dimensional (i.e. have a front, back, etc.), this means that when this type of file is opened that it must first be sized and oriented before a Component can be created (Aspire only represents base-relief so cannot work with a completely 3D object). Once the file becomes a Component it will have the same name as the original STL file.
	
	V3M
	: Vectric 3D Model (.v3m) is a proprietary file format developed by Vectric for Design and Make. Files in this format can be purchased from www.designandmake.com and when imported into Aspire will create a new Component with the same name as the file. This will be imported at the size and position the part was saved in the original file.
	
	WRL
	: WRL (.wrl) is a standard file format for representing 3D interactive vector graphics. It has been superseded by X3D file format.
	
	X
	: X (.x) is a simple file containing geometry meshes and material information that can be viewed in the DirectX Viewer.
	
- **Image File Formats**:

	BMP
	: Bitmap (.bmp) is a raster graphics image file format developed by Microsoft used to store bitmap digital images.
	
	GIF
	: Graphics Interchange Format (.gif) is a bitmap image file format.
	
	JPG/JPEG
	: Joint Photographic Experts Group (.jpg or .jpeg) is a commonly used image file for compressed digital images. JPG is typically lower resolution quality than a PNG file format.
	
	PNG
	: Portable Graphics Format (.png) is an uncompressed raster image file format. This is typically the highest quality image format and also has the ability to have transparent backgrounds.
	
	TIF/TIFF
	: Tag Image File Format (.tif or .tiff) is a file format for storing raster graphics images.
	
	
Finish 3D Toolpath
: A 3D toolpath that reduces or eliminates the irregular contours left by the rough cut.

Flat Depth
: The final depth at which the toolpath will cut to. Usually used in the vcarve toolpath.

Form Bit
: A bit that carves a standard profile such as a round over, ogee or similar contours.

Gantry
: The frame structure that straddles the bed and carries the spindle. It moves on guide rails along the length of the bed and is driven by stepper or servo drive motors.

G-Code
: A machine language that uses axis points and commands which the machine uses to move and perform functions. This code is auto generated from your toolpaths and must be saved with a post processor specific to your machine. (Think of g-code as the directions from a map route at which your machine will move and follow precisely.)

Hold-down
: A clamp or other such device used to firmly hold a workpiece or fixture to the table. Includes cams, clamps, double-sided tape, vacuum table, vacuum pods and others.

Home Position
: Mechanical position where the X, Y, and Z axis will reference from. Generally set from a g-code command with the help of limit or homing switches.

Inserts
: Cutting tips made of carbide, diamond, ceramic, or other materials, which can be easily inserted onto a cutting tool so you don’t have to remove and replace the entire tool when a tip becomes dull.

Jig
: A production work holding device that locates the workpiece and guides the cutting tool (see fixture). Used primarily for accuracy and in production machining.

Kerf
: The width of the cut removed by the cutting bit.

Milling
: CNC milling is a process that employs rotating, multi-point cutting tools to remove material from a workpiece.

Nesting
: The process of laying out patterns of a cut so as to reduce the amount of material waste in a project.

Node
: A point at which lines or pathways intersect; a central or connecting point. In Vectric software, there are a few types of nodes - start point, end point, mid-point, smooth point(biezer), arc point, and line point.

Open Vector
: A vector that does not connect back onto itself to create a complete loop, therefore leaving an opening in part of the vector. Sometimes a shape could look like a closed vector when nodes are touching but not connect to each other, it would be then considered an open vector even though it looks closed.

Origin
: User designated zero point for the work piece. From which the router will reference the positioning of all movements. This point must match what was set up in your CAM software.

Plunge
: The distance on the Z axis that the spindle and cutting tool moves toward, into, or along the material.

Plunge Rate
: The speed of descent of the spindle on the Z axis. 

Pocket Toolpath
: A toolpath that creates a cavity in the horizontal surface of a workpiece.

Polyline
: A continuous line composed of one or more line segments.

Post Processor
: A software function that enables the CAD/CAM application to format G-Code enabling the control system of a CNC to follow the designated toolpaths. This is usually specific to each different CNC machine manufacturer and model.

Profile Toolpath
: A toolpath that cuts along the profile of selected vector(s). Typically used to cut out the shape of a design.

Proximity Switch
: A limit switch that is used to find the home position or movement limits of an axis.

Rapid Movement
: Movement at which the CNC moves in between toolpath operations. Typically faster movements to save time when the cutter is not contacting the material.

Re-cutting
: What happens when material chips are not removed fast enough and the cutting tool hits them again. Re-cutting can result in a bad surface finish or excessive tool wear.

Resolution
: Describes the accuracy at which a CNC machine or component can distinguish position.

Restore Point
: The point along a toolpath where the spindle will start to resume a toolpath following a break. (Not all machines are capable of this.)

Roughing 3D Toolpath
: A 3D toolpath where the initial cut is designed to remove unwanted material, leaving a rough contour.

RPM
: Revolutions per minute that the spindle will spin when cutting.

Shank
: The solid, perfectly cylindrical part of a router bit. It is the part of the bit that goes into the collet of the spindle and is secured with the collet nut.

Soft Limits
: Limits on movement availability in each axis. Imposed by the workspace boundaries and based on controller settings and the location of home position. An “out of soft limits error” implies that based on the positioning of the workpiece, there is not enough room to move in a designated direction. 

Spindle
: A rotating motor that holds tools and is used to machine parts. (Sometimes substituted for a router.)

Spindle Speed
: Rotational speed of cutting tool (RPM).

Step Down
: Distance in Z-axis that the cutting tool plunges into the material.

Stepover
: The amount the cutting tool moves away from the previous cutting path as it cuts a new path.

Stepper Motor
: DC motor that moves in very precise steps upon the receipt of “pulses”, which result in very accurate positioning and speed control.

Surfacing
: The process of levelling the surface of the spoil board or material so that they are perpendicular to the spindle.

Taper
: A uniform increase or decrease in the size or diameter of a workpiece.

Thread Mill
: Cutters used in CNC milling machines to produce internal and external threads in a workpiece.

Toolpath
: User defined route at which the cutter follows to machine a workpiece. (Think of this as the “map” that you give your CNC to travel.)

Touch-Off Plate
: A device used to set the zero point (Origin) for the Z axis and sometimes the X and Y axis.

Up Cut Bit
: A cutting tool whose edges carve upward along the face of the material. This increases the potential for tear-out on the top surface but allows for a slightly higher feed-rate because the up flutes clear the material chips out of the cut.

V-Bit
: A rotating cutting tool shaped as a "V" and defined by the angle of the cutter. Used for V-carving; common size angle v-bits used are 30°, 45°, 60°, 90°, & 120°.

Vector
: Computer graphics images that are defined in terms of 2D points, which are connected by lines and curves to form polygons and other shapes.

VFD
: Variable Frequency Drive which controls the speed (RPM) of the spindle. Enables the fine tuning of the spindle during the operation of a toolpath. (Not available on all machines.)

Working Envelope
: The three-dimensional area that the spindle can travel within while cutting or milling.

X-Axis
: Left to right horizontal axis.

Y-Axis
: Front to back vertical axis.

Z-Axis
: Up and down axis representing depth.

