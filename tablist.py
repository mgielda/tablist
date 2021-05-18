#!/usr/bin/env python3

import typer
import yaml
from typing import Optional
from termcolor import colored

app = typer.Typer(help="A tab list app", add_completion=False)

data = None

@app.command("ls")
def list_sections():
    "list available sections"
    print('Sections:\n%s' % ('\n'.join(list(data.keys()))))

@app.command("lt")
def list_tabs(section_name: str, just_urls: bool = False):
    "list tabs in section"
    try:
        tabs = data[section_name]
    except KeyError:
        print(f"Section '{section_name}' not in the YAML file, trying fuzzy find")
        tabs = fzf(section_name)

    urls = list(tabs.values())
    if not just_urls:
        items = tabs.items()
        print(f'Tabs for "{section_name}":' if len(items) > 0 else f'No tabs for {section_name}.')
        for index, (key, value) in enumerate(items):
            print(colored(index, attrs=['bold']), colored(key, 'yellow'), value)
    else:
        for u in urls:
            print(u)

# TODO allow fuzzy finding of arguments / tab names in CLI mode
# perhaps in a new CLI library?

@app.command("ot")
def open_tabs(section_name: str, tab_no: Optional[int] = typer.Argument(None)):
    "open tabs in section in browser"
    try:
        tabs = data[section_name]
    except KeyError:
        print(f"Section '{section_name}' not in the YAML file, trying fuzzy find.")
        tabs = fzf(section_name)

    urls = list(tabs.values())
    import subprocess
    if tab_no is not None:
        if tab_no >= len(urls):
            print(f"Number {tab_no} higher than number of tabs in '{section_name}'")
            return
        process = subprocess.Popen(['xdg-open', urls[tab_no]])
    else:
        for u in urls:
            process = subprocess.Popen(['xdg-open', u])

from pathlib import Path
home = str(Path.home())

@app.callback(hidden=True)
def tablist(file: str = home + "/.tablist.yml"):
    global data
    try:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
    except:
        import sys
        print(f"File {file} not found or is not a proper YAML file.")
        sys.exit(1)

def fzf(search_string: str):
    from fuzzyfinder import fuzzyfinder
    keys = []
    tabs = {}
    for s in data:
        for k in data[s]:
            keys += [k]
            tabs[k] = data[s][k]
    suggestions = fuzzyfinder(search_string, keys)

    filtered_data = { x: tabs[x] for x in suggestions }
    return(filtered_data)

import click
from click_repl import repl

@app.command("i")
def interactive():
    "run in interactive mode"
    click.echo("Running in interactive mode. This supports tab completion.")
    click.echo("Use ':help' for help info, or ':quit' to quit.")
    repl(click.get_current_context())

if __name__ == "__main__":
    app()
