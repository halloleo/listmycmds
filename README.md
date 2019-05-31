# listmycmds - Print the commands in some ("my") directories of the ones available in PATH

I created this tool, because too often I cannot remember the exact name of a
little helper script I wrote, say, a year ago. Just trying command expansion
isn't very effective, because it lists not only my own helpers, but all the
standard UNIX commands as well, plus it does not find commands of which I
remember only a *middle* portion of the command name.

This tool to the rescue: It goes through the directories in your `PATH` and
lists only command which are in "my" own bin directories. Additionally the tool
can take a string as parameter which will limit the output to commands
containing this string.

The directories classified as "my" directories are determined by the following
two rules:

1. Directories beginning with my home directory (something like `/home/me/bin`
   or `/home/me/dev/bin`)
2. Additional directories explicitly specified in the colon-separated
   environment variable `MYCMDSPATH`

Rule 1 can be tuned through `MYCMDSPATH` as well: Entries in MYCMDSPATH which
start with a minus sign ('-') are excluded from the search. (For example an try
`-/home/me/go/bin` in `MYCMDSPATH` indicates that this directory won't be
searched through although it is in my home directory.)


As  basic use of the tool call the script with a file pattern:

``` bash
listmycmds.py img
```

This will print all executable commands in "my" directories containing the
string `img`. Let's say I have a `script rotate_img.sh` in `/home/me/bin`, then the
command line above will list it.

The pattern can be a file globbing pattern like '`*.sh`' (all shell scripts) or
'`img*`' (all commands starting with `img`).

`listmycmds` has more options. Here its help message:

```
usage: listmycmds.py [-h] [-a] [-1] [-d] [-e] [PATTERN [PATTERN ...]]

positional arguments:
  PATTERN              (file glob) pattern to filter commands on (default: -)

optional arguments:
  -h, --help           show this help message and exit
  -a, --all-files      list not only executable commands, but all files
                       (default: False)
  -1, --single-column  list one command per line (default: False)
  -d, --list-dirs      list directories which are searched (default: False)
  -e, --list-env       show environment variables used (default: False)
```

<!--  LocalWords:  listmycmds globbing MYCMDSPATH
 -->
