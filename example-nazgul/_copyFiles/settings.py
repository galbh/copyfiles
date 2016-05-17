import os


# The parent of the folder from which the program is activated
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Folder to copy files from
SOURCE_DIRNAME = ROOT_DIR + "\\public"

# Folder to copy files to
DESTINATION_DIRNAME = ROOT_DIR + "\\nazgul-server\\lib\\hub-webapp-0.1-SNAPSHOT\\static"

# Destination to drop zipped file
ZIP_FILE_DESTINATION = ROOT_DIR + "\\nazgul-server\\lib"

# Zipped file name no extension needed
ZIP_FILE_NAME = "hub-webapp-0.1-SNAPSHOT"

# Folder to zip
FOLDER_TO_ZIP = ROOT_DIR + "\\nazgul-server\\lib\\hub-webapp-0.1-SNAPSHOT"

