import subprocess
import shutil
import os

from pathlib import Path


class Utils(object):

    pyinstaller_path = \
        Path("..", "..", "venv", "Scripts", "pyinstaller.exe")

    def build_application(self, output_location, working_dir_path, spec_path, name, script_path):
        # Run PyInstaller to create the exe
        if not os.path.isdir("temp"):
            os.mkdir("temp")
        subprocess.run(
            "\"{0}\" --distpath=\"{1}\" --workpath=\"{2}\" --clean -F --specpath=\"{3}\" -w -n={4} {5}".format(
                self.pyinstaller_path.absolute(), output_location, working_dir_path, spec_path, name, script_path
            ), shell=True)
        # Clear out temporary files
        shutil.rmtree(working_dir_path)
        shutil.rmtree(spec_path)
        # Return the path of the .exe file to the caller
        return Path(output_location, "{}.exe".format(name))
