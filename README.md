# Regatron Custom Device
 Repo for creating a VeriStand Custom Device for Regatron G5 devices.

To use - clone the "Built" folder. There are 2020 and 2021 releases in this folder.
Copy the internal "G5 Regatron Custom Device" folder into "C:\Users\Public\Documents\National Instruments\NI VeriStand 202X\Custom Devices\G5 Regatron Custom Device", replacing X with your VeriStand version.

############

To build from source:

Dependencies:
LabVIEW 2020 32-bit 
OR LabVIEW 2021 64-bit

JKI Rest Client: https://www.vipm.io/package/jki_lib_rest_client/

niveristand Custom Device Development Tools 21.0.0: https://github.com/ni/niveristand-custom-device-development-tools/releases/tag/v21.0.0

Microsoft HTML Help Workshop: http://web.archive.org/web/20160201063255/http://download.microsoft.com/download/0/A/9/0A939EF6-E31C-430F-A3DF-DFAE7960D564/htmlhelp.exe
(From Nicola Palma - OpenG TK may be required: https://www.ni.com/en-gb/support/downloads/tools-network/download.openg-libraries-for-labview.html#379041)

#####################

Completed:
Initial addition of channels

Initial addition of IP Address Property

Implementation of REST API from channels being interacted with.

To do:
Changing Glyphs of channels

Creation of full channel documentation.

Creation of HTML help documents
