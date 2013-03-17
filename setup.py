#!/usr/bin/env python3

import distutils.core
import os.path

if __name__ == "__main__":
    README = "https://github.com/sbp/gin/blob/master/README.md"

    if os.path.isfile(".git/refs/heads/master"):
        with open(".git/refs/heads/master", encoding="ascii") as f:
            version = f.read(7)
        with open("VERSION", "w", encoding="ascii") as f:
            f.write(version)
    else:
        with open("VERSION", encoding="ascii") as f:
            version = f.read(7)

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
