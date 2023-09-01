from pathlib import Path
from doit.tools import result_dep
import shutil
import os
import xml.etree.ElementTree as ET

cwd = Path.cwd()
output_path = cwd / 'output'

file_list = []

#Write the release version to file
version = "1.0.4.6"
f= open("version.txt",'w')
f.write(version)
f.close()



# Load the custom device XML from a file
cd_xml = cwd / "G5 Regatron Custom Device" / "Custom Device G5 Regatron Custom Device.xml"
cd_xml_tree = ET.parse(cd_xml)
cd_xml_root = cd_xml_tree.getroot()

# Find the Version element and modify its text
version_element = cd_xml_root.find("Version")

if version_element is not None:
    version_element.text = version  # Modify the version here

# Save the modified XML back to the file
cd_xml_tree.write(cd_xml, encoding="utf-8", xml_declaration=True)


ET.register_namespace("i",  "http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace("z",  "http://schemas.microsoft.com/2003/10/Serialization/")
ET.register_namespace("",  "http://schemas.datacontract.org/2004/07/NationalInstruments.PackageBuilder.Engine")
ET.register_namespace("d8p1","http://schemas.datacontract.org/2004/07/NationalInstruments.PackageBuilder.Plugins.LabVIEWNXG")

# Load the custom device package builder XML from file
package_xml = cwd / "G5 Regatron Custom Device" / "Regatron Custom Device.pbs"
package_xml_tree = ET.parse(package_xml)
package_xml_root = package_xml_tree.getroot()

# Define the namespaces
namespaces = {
    "z": "http://schemas.microsoft.com/2003/10/Serialization/",
    "default": "http://schemas.datacontract.org/2004/07/NationalInstruments.PackageBuilder.Engine"
}

# Find the Version element using namespaces
version_elements = package_xml_root.findall(".//default:Version", namespaces)



version_elements[0].text = version # set the new version
version_elements[1].text = version

# Save the modified XML back to the file
package_xml_tree.write(package_xml, encoding="utf-8", xml_declaration=True)



#create output folder structure:
folder_list = [
    output_path,
    output_path / 'build',
    output_path / 'package',
    ]

for path in folder_list:
    try:
        os.mkdir(path)
    except:
        nothing = 0
        #print("%s already exists" % (path))

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


###########################################################################
# This task builds the labview CSB-Interface-App.vi application and       #
# Then it builds the nipm package based application, build_stm32, gen_dbc #
# and gen_manual tasks                                                    #
###########################################################################
def task_build_custom_device():

    labiew_app_build_command_config =         r'LabVIEWCLI -OperationName ExecuteBuildSpec -ProjectPath "C:\Git\Regatron-Custom-Device\G5 Regatron Custom Device\G5 Regatron Custom Device Custom Device.lvproj" -TargetName "My Computer" -BuildSpecName  "Configuration Release" -LabVIEWPath "C:\Program Files\National Instruments\LabVIEW 2021\LabVIEW.exe"'
    labiew_app_build_command_engine_windows = r'LabVIEWCLI -OperationName ExecuteBuildSpec -ProjectPath "C:\Git\Regatron-Custom-Device\G5 Regatron Custom Device\G5 Regatron Custom Device Custom Device.lvproj" -TargetName "My Computer" -BuildSpecName  "Engine Release" -LabVIEWPath "C:\Program Files\National Instruments\LabVIEW 2021\LabVIEW.exe"'
    labiew_app_build_command_engine_linux =   r'LabVIEWCLI -OperationName ExecuteBuildSpec -ProjectPath "C:\Git\Regatron-Custom-Device\G5 Regatron Custom Device\G5 Regatron Custom Device Custom Device.lvproj" -TargetName "RT PXI Target - Linux x64" -BuildSpecName  "Engine Release" -LabVIEWPath "C:\Program Files\National Instruments\LabVIEW 2021\LabVIEW.exe"'
    dep_files =  getListOfFiles(cwd / 'G5 Regatron Custom Device')

    def clean_folder():
        files = getListOfFiles(cwd / 'output')
        for file in files:
            print("Deleted File %s" % (file))
            os.remove(file)

    return{
        "actions": [
            clean_folder,
            labiew_app_build_command_config,
            labiew_app_build_command_engine_windows,
            labiew_app_build_command_engine_linux,
            
            ],
        "file_dep": dep_files,
        "verbosity": 2,
}


def task_build_package():
    packge_builder_command = r'"C:\Program Files\National Instruments\Package Builder\nipbcli" -o "C:\Git\Regatron-Custom-Device\G5 Regatron Custom Device\Regatron Custom Device.pbs" -b=packages'
    

    return{
        "actions": [
            packge_builder_command
        ],
        "uptodate": [result_dep('build_custom_device')]
    }
