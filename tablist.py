#!/usr/bin/env python3

import typer
import yaml
from typing import Optional
from termcolor import colored

app = typer.Typer(help="A tab list app", add_completion=False)

data = None

@app.command()
def list_sections():
    "list available sections"
    print('Sections:\n%s' % ('\n'.join(list(data.keys()))))

@app.command()
def list_tabs(section_name: str, pretty: bool = False):
    "list tabs in section"
    try:
        tabs = data[section_name]
    except KeyError:
        print(f"Section '{section_name}' not in the YAML file")
        return
    if pretty:
        print(f'Tabs in section {section_name}:')
        for index, (key, value) in enumerate(tabs.items()):
            print(colored(index, attrs=['bold']), colored(key, 'yellow'), value)
    else:
        for t in list(tabs.values()):
            print(t)

# TODO allow fuzzy finding of arguments / tab names in CLI mode
# perhaps in a new CLI library?

@app.command()
def open_tabs(section_name: str, tab_no: Optional[int] = typer.Argument(None)):
    "open tabs in section in browser"
    try:
        tabs = list(data[section_name].values())
    except KeyError:
        print(f"Section '{section_name}' not in the YAML file")
        return
    import subprocess
    if tab_no is not None:
        if tab_no >= len(tabs):
            print(f"Tab number {tab_no} not existent in '{section_name}' section")
            return
        process = subprocess.Popen(['xdg-open', tabs[tab_no]])
    else:
        for t in tabs:
            process = subprocess.Popen(['xdg-open', t])

@app.callback(hidden=True)
def tablist (file: str = "tabs.yml"):
    global data
    try:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
    except:
        import sys
        print(f"File {file} not found or is not a proper YAML file.")
        sys.exit(1)

import click
from click_repl import repl

@app.command()
def interactive():
    "run in interactive mode"
    click.echo("Running in interactive mode. This supports tab completion.")
    click.echo("Use ':help' for help info, or ':quit' to quit.")
    repl(click.get_current_context())

if __name__ == "__main__":
    app()
