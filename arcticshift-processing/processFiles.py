import sys
import json

version = sys.version_info
if version.major < 3 or (version.major == 3 and version.minor < 10):
    raise RuntimeError("This script requires Python 3.10 or higher")
import os
from typing import Iterable

from fileStreams import getFileJsonStream
from utils import FileProgressLog

time_lower_bound = 1735344000
fileOrFolderPath = r"/scratch/jacobli/post_zst/"
subreddits_to_search = ["cybersecurity", "teachers", "k12sysadmin", "technology", "edtech", "highschool", "canadianteachers", "k12cybersecurity", "technews", "msp", "internationalteachers", "canada", "toronto", "askto", "raleigh", "sacramento", "chicagosuburbs", "connecticut", "winnipeg", "bullcity", "masssachusetts", "anchorage", "ontarioteachers", "pwnhub", "privacy", "askuk", "teachinguk", "columbus", "charlotte"]
recursive = True

def process_file(path: str):
    out_data = []
    print(f"Processing file {path}")
    with open(path, "rb") as f:
        json_stream = getFileJsonStream(path, f)
        if json_stream is None:
            print(f"Skipping unknown file {path}")
            return None
        progress_log = FileProgressLog(path, f)
        for row in json_stream:
            progress_log.onRow()
            if row["subreddit"].lower() in subreddits_to_search and time_lower_bound < row["created_utc"]:
                out_data.append(row)
        progress_log.logProgress("\n")
    return out_data

def processFolder(path: str):
    file_iterator: Iterable[str]
    if recursive:
        def recursiveFileIterator():
            for root, dirs, files in os.walk(path):
                for file in files:
                    yield os.path.join(root, file)
        file_iterator = recursiveFileIterator()
    else:
        file_iterator = os.listdir(path)
        file_iterator = (os.path.join(path, file) for file in file_iterator)

    for i, file in enumerate(file_iterator):
        print(f"Processing file {i+1: 3} {file}")
        out_data = process_file(file)
        with open(f"/scratch/jacobli/posts/output{i+1}.jsonl", "w") as f:
            for obj in out_data:
                f.write(json.dumps(obj) + "\n")

def main():
    if os.path.isdir(fileOrFolderPath):
        processFolder(fileOrFolderPath)
    else:
        out_data = process_file(fileOrFolderPath)
        with open("output.jsonl", "w") as f:
            for obj in out_data:
                f.write(json.dumps(obj) + "\n")

    print("Done :>")

if __name__ == "__main__":
    main()
