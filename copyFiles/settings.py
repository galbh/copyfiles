import os


# The folder from which the program is activated
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Folder to copy files from
SOURCE_DIRNAME = ROOT_DIR + "\\public"

# Folder to copy files to
DESTINATION_DIRNAME = ROOT_DIR + "\\destination"

# Destination to drop zipped file
COMPRESSED_FILE_DESTINATION = ROOT_DIR + "\\compressed_file_destination"

# Zipped filed name
COMPRESSED_FILE_NAME = "gal_ben_haim"

# Folder to zip
SERVER_DIR = ROOT_DIR + "\\server"


