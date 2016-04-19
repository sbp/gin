# gin - a Git index file parser

The `gin` script parses the databases that live at `.git/index` in any Git repository, and shows the contents in a readable form, or as a JSON dump. These databases store the current state of the stage area, sometimes called the index or cache.

## Install

    pip install gin

Or clone this repo and use the `gin` script.

Or download the script directly.

## Use

```
usage: gin [-h] [-j] [-v] [path]

parse a Git index file

positional arguments:
  path           path to a Git repository or index file

optional arguments:
  -h, --help     show this help message and exit
  -j, --json     output JSON
  -v, --version  show script version number
```

### Examples

*   Show the Git index file in the current repository, if in the repository root:

        gin

*   Show the Git index file in the `~/git-repo` repository:

        gin ~/git-repo    

*   Show the Git index file `~/git-repo/.git/index`:

        gin ~/git-repo/.git/index

The script supports index file versions 2 and 3, and will skip over extensions.

Use the `-j` or `--json` flags to dump JSON.

### Advanced

To use the script as a module, rename it to `gin.py`.

## Report issues

[Submit issues](https://github.com/sbp/gin/issues) on Github.

Tweet [@sbp](https://twitter.com/sbp) with short comments or enquiries.

## Example

### Pretty print an index

    $ gin test/01.index

Output:

```ini
[header]
  signature = DIRC
  version = 3
  entries = 5

[entry]
  entry = 1
  ctime = 1363549359.0
  mtime = 1363549359.0
  dev = 16777217
  ino = 1154043
  mode = 100644
  uid = 501
  gid = 20
  size = 6
  sha1 = d5f7fc3f74f7dec08280f370a975b112e8f60818
  flags = 9
  assume-valid = False
  extended = False
  stage = (False, False)
  name = added.txt

[...]

[checksum]
  checksum = True
  sha1 = 1ef0972eb948e6229240668effcb9c600fe5888d
```

### Get name fields from an index

    $ gin | egrep '^  name ='

Output:

```
  name = .gitignore
  name = MANIFEST
  name = Makefile
  name = README.md
  name = gin
  name = setup.py
  name = test/01.index
  name = test/01.json
  name = test/01.txt
  name = test/run
```

Which should be equivalent to `git ls-files`.
