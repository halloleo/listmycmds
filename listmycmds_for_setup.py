import argh
import listmycmds

def main():
    argh.dispatch_command(listmycmds.listmycmds)
