import os
import fnmatch
from glob import glob
import shutil
import datetime
import time


def getSize(filepath: str) -> int:
    if not os.path.isdir(filepath):
        return
    name_list = os.listdir(filepath)
    size = 0
    for files in name_list:
        pathIndex = f'{filepath}/{files}'
        if os.path.isdir(pathIndex):
            size += getSize(pathIndex)
        else:
            size += os.path.getsize(pathIndex)
    return size


def find_files(filename: str, search_path: str) -> list[str]:
    if not os.path.isdir(search_path):
        return []
    result = []
# Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

#example : find_files("Python1.pdf","C:\\something\\")


def findFileByName(filename: str, search_path: str) -> list[str]:
    if not os.path.isdir(search_path):
        return []
    result = []
    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        for file in files:
            # since the splittext function does not accept the list. can I change the function to make it to accept the list?
            split_name, ext = os.path.splitext(file)
            if(filename == split_name):
                file_name = split_name + ext
                result.append(os.path.join(root, file_name))

    return result


def fuzzySearchFile(pattern, search_path):
    # this function just need to input the fuzzy file name under the specific directory and returns the path which contains the fuzzyName

    # if user doesn't enter the valid search_path, corece to the root path.
    search_path = "." if search_path == "" else search_path
    if not os.path.isdir(search_path):
        return []
    result = []
    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        files = (os.path.join(root, name) for name in files)
        result.extend(fnmatch.filter(files, f"*{pattern}*"))
    return result

    


def fuzzySearchFile2(pattern, search_path):
    # this function just need to input the fuzzy file name under the specific directory and returns the path which contains the fuzzyNam
    abspath = os.path.abspath(search_path)
    if os.path.exists(abspath):
        files = glob(os.path.join(abspath, "**", pattern), recursive=True)
    else:
        raise Exception(f"{abspath} does not exists")
    return files


def findFileByType(file_type: str, search_path: str) -> list[str]:

    if not os.path.isdir(search_path):
        return []

    file_type = file_type if file_type[0] == "." else f".{file_type}"

    result = []

    name_list = os.listdir(search_path)
    for file in name_list:
        pathIndex = os.path.join(search_path, file)
        if os.path.isdir(pathIndex):
            result.extend(findFileByType(file_type, pathIndex))
        else:
            _, ext = os.path.splitext(file)
            if ext == file_type:
                result.append(pathIndex)
            else:
                pass

    return result
# findFileByType("extention","filePath")


def findFileByTypes(search_path: str, *file_type: str) -> list[str]:
    # this function can allow you to input the multiple types of the postfix type and return their path

    # make sure that the search_path exists
    if not os.path.isdir(search_path):
        return []

    file_type = [
        f'.{ftype}' if ftype[0] != '.' else ftype
        for ftype in file_type
    ]

    # declare outcome list
    result = []

    name_list = os.listdir(search_path)
    for file in name_list:
        pathIndex = os.path.join(search_path, file)
        if os.path.isdir(pathIndex):
            result.extend(findFileByTypes(pathIndex, *file_type))
        else:
            _, ext = os.path.splitext(file)
            if ext in file_type:
                result.append(pathIndex)
            else:
                pass
    return result


def compare2Folder(path1: str, path2: str) -> list[str]:
    # this function compare 2 folders and output the different file name into an array from 2 directories provided

    # turn both path into abs paths
    abspath1 = os.path.abspath(path1)
    abspath2 = os.path.abspath(path2)

    # make sure both search path exists
    if not os.path.isdir(abspath1) or not os.path.isdir(abspath2):
        return []
    absList1 = _getAllFiles(abspath1)
    absList2 = _getAllFiles(abspath2)

    return list(set(absList1) - set(absList2)) + list(set(absList2) - set(absList1))


def _getAllFiles(path: str) -> list[str]:
    if not os.path.isdir(path):
        return []
    absPath = os.path.abspath(path)

    # declare the out put list
    result = []
    # Walking top-down from the root
    for root, dir, files in os.walk(absPath):
        result.extend(files)
    return result


def compare2FolderStrict(path1: str, path2: str) -> list[str]:
    # similar to compare2Folder, but would examine more parameters (etc, filelength)
    # turn both path into abs paths
    abspath1 = os.path.abspath(path1)
    abspath2 = os.path.abspath(path2)

    # make sure both search path exists
    if not os.path.isdir(abspath1) or not os.path.isdir(abspath2):
        return []

    # get the file and size pair
    absDict1 = _getFileAndSize(abspath1)
    absDict2 = _getFileAndSize(abspath2)

    return list({k: absDict2[k] for k in set(absDict2) - set(absDict1)} | {k: absDict1[k] for k in set(absDict1) - set(absDict2)}.keys())


def _getFileAndSize(path: str) -> dict[str, int]:
    if not os.path.isdir(path):
        return []

    # declare the output dict
    outDict = {}
    # Walking top-down from the root
    for root, dir, files in os.walk(os.path.abspath(path)):
        for file in files:
            filePath = os.path.join(os.path.abspath(root), file)
            size = os.path.getsize(filePath)
            outDict[file] = size
    return outDict


def copyUnzip(fromSource:str, toDestination:str) -> None:
    # this function copy from the source folder and paste it to the destination folder and unzip

    # 1: copy and paste logic
    _copy(fromSource, toDestination)

    # separate the fromSource filename and form the toDestination filename
    fileName = os.path.basename(fromSource)
    dest = os.path.join(toDestination, fileName)
    # 3: unzip logic
    _unzip(dest)


def _copy(src:str, dest:str) -> None:
    # fromsource must be the file not the directory
    if not os.path.isfile(src):
        print("you need to enter the valid file path")

    # if the destination not exists, then create the destination
    if not os.path.isdir(dest):
        dest = os.mkdir(dest)
    shutil.copy2(src, dest)


def _unzip(dest:str) -> None:
    # separate the fromSource filename and form the toDestination filename
    fileName = os.path.dirname(dest)
    shutil.unpack_archive(dest, fileName)


def batchPrintingByType(file_type, file_path):
    # this function will print all the file type under the specific path
    pass


def recentUpfiles(path):
    # this function get the most recent updated files from a directory
    if not os.path.isdir(path):
        return []
    # declare the output
    outFile = []
    # Walking top-down from the root
    for root, dir, files in os.walk(os.path.abspath(path)):
        for file in files:
            fileAbsPath = os.path.abspath(os.path.join(root, file))
            fileModifiedTime = os.path.getmtime(fileAbsPath)
            timeAgo = time.time() - fileModifiedTime
            sevenDays = datetime.timedelta(days=7).total_seconds()
            if timeAgo <= sevenDays:
                filePath = os.path.join(os.path.abspath(root), file)
                outFile.extend(filePath)
    return outFile


def collectSize(path):
#This function collectSize of the file under the certain directory
    pass



def collectByType(path):
    #This function collectSize of the file under the certain directory by type
    pass


def fileDiff(srcFile, desFile):
    #This function returns the difference of the content of the 2 files
    pass


def sizeChange(data,path):
     #This function returns the size of the file change since last time it's being saved
     pass


def countPathFolders(path):
    #count how many folders under certain path
    pass

def countPathFiles(path):
    #count how many files under certain path
    pass


def countPathType(path):
    #count how many files for certain types of the files under certain path
    pass