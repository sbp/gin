#!/usr/bin/env python

import distutils.core
import os.path
import sys

if __name__ == "__main__":
    README = "https://github.com/sbp/gin/blob/master/README.md"

    if os.path.isfile("gin"):
        with open("gin", "r+", encoding="ascii") as f:
            f.seek(66)
            version = f.read(7)

            if os.path.isdir(".git") and ("sdist" in sys.argv):
                patch = int(version[-3:]) + 1
                if patch > 999:
                   raise ValueError("Update major/minor version")
                version = version[:-3] + "%03i" % patch

                f.seek(66)
                f.write(version)
    else:
        print("Unable to find gin script: refusing to install")
        sys.exit(1)

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
            "Programming Language :: Python :: 2"
        ]
    )
