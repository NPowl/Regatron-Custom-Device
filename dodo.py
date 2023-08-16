from pathlib import Path
from doit.tools import result_dep
import shutil
import os

cwd = Path.cwd()
output_path = cwd / 'output'

file_list = []

#Write the release version to file
version = "1.0.0"
f= open("version.txt",'w')
f.write(version)
f.close()


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
