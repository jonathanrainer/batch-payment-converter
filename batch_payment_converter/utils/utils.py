import subprocess
import shutil
import os
import sys

from pathlib import Path
from zipfile import ZipFile


class Utils(object):

    pyinstaller_path = \
        Path("venv", "Scripts", "pyinstaller.exe")

    def build_application(self, output_location, working_dir_path, spec_path, name):
        # Run PyInstaller to create the exe
        if Path(output_location, name).exists():
            shutil.rmtree(Path(output_location, name).absolute())
        self.create_folder(Path("build"))
        working_dir_path = Path("build", working_dir_path)
        self.create_folder(working_dir_path)
        spec_path = Path("build", spec_path)
        self.create_folder(spec_path)
        subprocess.run("\"{}\" --distpath=\"{}\" --workpath=\"{}\" --clean \"{}\"".format(
            self.pyinstaller_path, Path("dist"), working_dir_path,
            str(Path("build", "spec", "batch_payment_converter.spec"
        ).absolute())), shell=True)
        # Clear out temporary files
        shutil.rmtree(working_dir_path.absolute())

    @staticmethod
    def create_folder(path):
        if not os.path.isdir(str(path.absolute())):
            os.mkdir(str(path.absolute()))


if __name__ == "__main__":
    utils = Utils()
    utils.build_application(*sys.argv[1:])
