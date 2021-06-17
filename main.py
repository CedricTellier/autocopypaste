import logging
import os
import shutil
import sys
import time
from os.path import expanduser

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class launcher():
    def __init__(self):
        self.downloadPath = expanduser("~/Downloads")
        self.extensionList = [(".exe", "C:/Executables"),
                              (".ifc", "D:/Fichiers IFC")]
        self.processed = 0
        self.launchObserver()

    def detectedChange(self, event):
        print(f"hey, {event.src_path} has been created!")
        self.fileList = os.listdir(self.downloadPath)
        self.unprocessed = len(self.fileList)
        self.transferIteration()

    def launchObserver(self):
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True
        event_handler = PatternMatchingEventHandler(
            patterns, ignore_patterns, ignore_directories, case_sensitive)
        observer = Observer()
        observer.schedule(event_handler, self.downloadPath, recursive=False)
        observer.start()
        event_handler.on_created = self.detectedChange
        event_handler.on_modified = self.detectedChange

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def transferIteration(self):
        for file in self.fileList:
            for extension in self.extensionList:
                if file.find(extension[0]) != -1:
                    current = self.downloadPath + "\\" + file
                    if self.isValid(extension[-1]):
                        destination = extension[-1] + "\\" + file
                        fileTransfert = transfert(current, destination)
                        if fileTransfert:
                            self.processed += 1
                            self.unprocessed -= 1
        return True

    def isValid(self, directory):
        try:
            if os.path.isdir(directory):
                return True
            else:
                os.mkdir(directory)
                return True
        except OSError:
            print("OS Error trying to create directory %s" % directory)
            return False

    def getCountProcessed(self):
        return self.processed

    def getCountRemaining(self):
        return self.unprocessed


class transfert():
    def __init__(self, current, destination):
        self.current = current
        self.destination = destination
        self.processTransfert(self.current, self.destination)

    def processTransfert(self, current, destination):
        shutil.move(current, destination)
        return True


def main():
    processed = launcher()
    if processed:
        print("Nombre de fichiers transferes : {}. Nombre de fichier(s) restant(s) : {}".format(
            processed.getCountProcessed(), processed.getCountRemaining()))


if __name__ == '__main__':
    main()
