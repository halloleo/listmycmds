# listmycmds - Print the commands in some ("my") directories of the ones available in PATH

I created this tool, because too often I cannot remember the exact
name of a little helper tool I wrote, say, a year ago. Just trying
command expansion isn't very effective because it list all the
standard UNIX commands as well, plus it does not find commands of
which I remember only a *middle* portion of the command name.

This tool to the rescue: It goes through the directories in your
`PATH` and lists only command which are in "my" own bin
directories. Additionally the tool can take a string as parameter
which will limit the output to commands containing this string.

The directories why classify as  "my" directories are determined with 
the following two rules:

1. Directories beginning with my home directory (something like
   `/home/me/bin` or `/home/me/dev/bin`)

2. Additional directories explicitly specified in the environment
   variable `MYCMDSPATH`
