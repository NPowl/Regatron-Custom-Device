# Regatron Custom Device
 Repo for creating a VeriStand Custom Device for Regatron G5 devices.

Only supports Veristand 2021!

This custom device can be build from Labview and the build will be copied to Public Documents/National Instruments/NI VeriStand 2021/Custom Devices for local testing

For a release please use the "build_package" command through the pydoit python package. Set the version in the "dodo.py" file!



> **Important:**  Install the "HTTP Client with SSL Support" package on the NI Real-Time target using NI MAX. Without this package the deployment will fail!
 
############

To build from source:

## Dependencies:
LabVIEW 2021 64-bit
Labview Real Time Module 2021

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


