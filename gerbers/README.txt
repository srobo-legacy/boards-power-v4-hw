Company: Student Robotics
Contact: Rich Barlow
Email:   rbarlow@studentrobotics.org
Phone:   XXXXXXXXXXXX
--------------------------------------------------------------------------------
Board Reference:  pbv4
Board Issue:      b
--------------------------------------------------------------------------------
Board Details:
Bare Board Test:      Yes
Layers:               4
Copper Weight:        1oz (all layers)
Material:             1.6mm FR4
Solder Resist:        BLUE on 2 sides (65 off); RED on 2 sides (15 off)
Silk Screen:          WHITE on 2 sides
Notes:                Please tent vias with solder mask. Please do not pull-back
                      silk from around vias. The 1.45mm holes (D140) must have a
		      finished hole size of 1.45mm +-0.05mm.
--------------------------------------------------------------------------------
Panel Details:
Please panelise as appropriate for in-house assembly. Please position breakout
pips as shown in the drawing 'pbv4b.breakout.png'. When the boards are removed
from the panel it is required that the waste material is removed such that a
smooth round corner is left on the board, as shown in the drawing.
--------------------------------------------------------------------------------
Stack up:
top
group2
group3
bottom
--------------------------------------------------------------------------------
Assembly Notes:
J1, J2 and J3 (Wurth 7460305) are push-fit components and require a press
capable of applying around 1000N of force. A jig to support the board during
the press-fit process can be supplied if required. These three terminals do not
require soldering.

J5 is to be populated with the wire-ended fan X2. The wires must be cut
42mm +-5mm from the fan casing and soldered directly to the board. The red wire
must be soldered to the square pad.
--------------------------------------------------------------------------------
Included Files:

Board:
pbv4b.top.gbr            - Top Copper Layer (Layer 1)
pbv4b.group2.gbr         - First Inner Layer (Layer 2)
pbv4b.group3.gbr         - Second Inner Layer (Layer 3)
pbv4b.bottom.gbr         - Bottom Copper Layer (Layer 4)
pbv4b.topmask.gbr        - Solder Mask Top
pbv4b.bottommask.gbr     - Solder Mask Bottom
pbv4b.toppaste.gbr       - Solder Paste Top
pbv4b.topsilk.gbr        - Silk Screen Top
pbv4b.bottomsilk.gbr     - Silk Screen Bottom
pbv4b.outline.gbr        - Board Outline
pbv4b.plated-drill.cnc   - Plated Hole Drill Information
pbv4b.unplated-drill.cnc - Unplated Hole Drill Information
pbv4b.breakout.png       - Drawing showing positioning of breakout pips

Assembly:
pbv4b.assembly.gbr       - Assembly drawing showing component locations
pbv4b.xy.csv             - XY Placement Data (in mm)
--------------------------------------------------------------------------------
If there are any problems please contact Rich Barlow using the details at
the top of this file.
