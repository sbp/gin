#!/usr/bin/env python3
version = "0.1.002"

import distutils.core
import os.path

if __name__ == "__main__":
    README = "https://github.com/sbp/gin/blob/master/README.md"

    if os.path.isdir(".git") and os.path.isfile("setup.py"):
        with open("setup.py", "r+", encoding="ascii") as f:
            f.seek(34)
            version = f.read(7)

            patch = int(version[-3:]) + 1
            if patch > 999:
               raise ValueError("Update major/minor version")
            version = version[:-3] + "%03i" % patch

            f.seek(34)
            f.write(version)

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
