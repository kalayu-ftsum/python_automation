import os
from pathlib import Path
SUBDIRECTORIES={
    "DOCUMENTS":['.pdf','.rtf','.txt'],
    "AUDIO":[".m4a",".m4a",".mp3"],
    "VIDEOS":[".avi","mp4",".mov"],
    "IMAGES":[".jpg",".jpeg",".png"]
}

def matchDir(value):
    for category, suffixs in SUBDIRECTORIES.items():
        for suffix in suffixs:
            if suffix==value:
                return category
    return "MISD"
def organize():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath=Path(item)
        fileSuffix=filePath.suffix.lower()
        fileDir=matchDir(fileSuffix)
        fileDirPath=Path(fileDir)
        if fileDirPath.is_dir() !=True:
            fileDirPath.mkdir()
        filePath.rename(fileDirPath.joinpath(filePath))



organize()