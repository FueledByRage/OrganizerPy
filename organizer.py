import os
import shutil

class Organizer:
    def return_path(self, file):
        split_file = file.split('.')
        return 'Folder for ' + split_file[len(split_file) - 1]


    def move_file(self, file):
        newFolder = self.return_path(file)
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        shutil.move(file, newFolder + '/' + file)


    def do_it(self):
        files = [
            filename for filename in os.listdir('.')
        ]
        for filename in files:
            file_split = filename.split('.')
            if len(file_split) >= 2 and file_split[0] != 'organizer':
                self.move_file(filename)
                

organizer = Organizer()
organizer.do_it()
