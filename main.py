from os.path import join
from pathlib import Path
from subprocess import run

from prompt_toolkit import PromptSession
from tomli import TOMLDecodeError, load, loads

default_config = '''
                 prompt = "$ "
                 '''

with open(join(Path.home(), ".modshrc"), "rb") as config:
    try:
        parsed_config = load(config)
    except TOMLDecodeError:
        print("Configuration parse incorrect. Rolling back to defaults.")
        parsed_config = loads(default_config)

cli = PromptSession(message=parsed_config["prompt"])
command = ""

while True:
    command = cli.prompt()
    if command == "exit":
        break
    argv = str(command).split(" ")
    print(run(argv, capture_output=True, text=True).stdout)
