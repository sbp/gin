#!/usr/bin/env python3
version = "0.1363554331"

import distutils.core
import os.path

if __name__ == "__main__":
    README = "https://github.com/sbp/gin/blob/master/README.md"

    if os.path.isdir(".git"):
        import subprocess
        date = subprocess.check_output(["git", "log", "-1", "--format='%ct'"])
        date = date[1:11]

        if os.path.isfile("setup.py"):
            with open("setup.py", "r+b") as f:
                f.seek(36)
                f.write(date)

    distutils.core.setup(
        name="gin",
        version=version,
        author="Sean B. Palmer",
        url="https://github.com/sbp/gin",
        description="Git index file parser",
        long_description="Documented in `@sbp/gin/README.md <%s>`_" % README,
        scripts=["gin"],
        platforms="Linux and OS X",
        classifiers=[
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3"
        ]
    )
