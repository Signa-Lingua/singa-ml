import os
import argparse


def bulk_rename_files(folder_path, start_number):
    folder_path = f"./storage/datasets/raw/{folder_path}"

    for filename in os.listdir(folder_path):
        file_number = int(filename.split(".")[0])

        new_number = file_number + int(start_number)

        new_filename = f"{new_number}.avi"

        # get full file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)

        # rename the file
        os.rename(old_file, new_file)
        print(f"Renamed {filename} to {new_filename}")


parser = argparse.ArgumentParser()
parser.add_argument(
    "folder", type=str, help="The path to the folder containing files to be renamed"
)
parser.add_argument(
    "start", type=str, help="Start renaming the file from"
)
args = parser.parse_args()

bulk_rename_files(args.folder, args.start)
