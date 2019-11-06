import time
import logging
from watchdog.observers import Observer
import sys
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# Goal f the file
# Select the folder Downlad and automate transfer of specific extension file
# 1 get directory
# 2 list all file in it
# retrieve by extension
# automate transfer

# 1 get Directory of Downlad
# import os
# import shutil
# from os.path import expanduser

# class launcher():
#     def __init__(self):
#         self.downloadPath = expanduser("~/Downloads")
#         self.fileList = os.listdir(self.downloadPath)
#         self.unprocessed = len(self.fileList)
#         self.extensionList = [(".exe", "D:/Executables"),
#                               (".ifc", "D:/Fichiers IFC")]
#         self.processed = 0
#         self.transferIteration()

#     def transferIteration(self):
#         for file in self.fileList:
#             for extension in self.extensionList:
#                 if file.find(extension[0]) != -1:
#                     current = self.downloadPath + "\\" + file
#                     if self.isValid(extension[-1]):
#                         destination = extension[-1] + "\\" + file
#                         fileTransfert = transfert(current, destination)
#                         if fileTransfert:
#                             self.processed += 1
#                             self.unprocessed -= 1
#         return True

#     def isValid(self, directory):
#         try:
#             if os.path.isdir(directory):
#                 return True
#             else:
#                 os.mkdir(directory)
#                 return True
#         except OSError:
#             print("OS Error trying to create directory %s" % directory)
#             return False

#     def getCountProcessed(self):
#         return self.processed

#     def getCountRemaining(self):
#         return self.unprocessed


# class transfert():
#     def __init__(self, current, destination):
#         self.current = current
#         self.destination = destination
#         self.processTransfert(self.current, self.destination)

#     def processTransfert(self, current, destination):
#         shutil.move(current, destination)
#         return True


# def main():
#     processed = launcher()
#     if processed:
#         print("Nombre de fichiers transferes : {}. Nombre de fichier(s) restant(s) : {}".format(
#             processed.getCountProcessed(), processed.getCountRemaining()))


# if __name__ == '__main__':
#     main()
