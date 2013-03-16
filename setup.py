#!/usr/bin/env python3

import distutils.core

if __name__ == "__main__":
    with open(".git/refs/heads/master", encoding="ascii") as f:
        version = f.read(7)

    distutils.core.setup(
        name="gin",
        version=version,
        author="Sean B. Palmer",
        url="https://github.com/sbp/gin",
        description="Git index file parser",
        long_description="See `@sbp/gin <https://github.com/sbp/gin>`_ for details",
        scripts=["gin"],
        platforms="Linux and OS X",
        classifiers=[
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3"
        ]
    )
