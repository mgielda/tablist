#!/usr/bin/env python3

import typer
import yaml

app = typer.Typer(help="A tab list app", add_completion=False)

data = None

@app.command()
def list_sections():
    "list available sections"
    print('Sections:\n%s' % ('\n'.join(list(data.keys()))))

@app.command()
def show_tabs(section_name: str, pretty: bool = False):
    "show tabs in section"
    tabs = list(data[section_name].values())
    if pretty:
        print(f'Tabs in section {section_name}:')
        print(yaml.dump(tabs, default_flow_style=False).strip())
    else:
        for t in tabs:
            print(t)

@app.callback(hidden=True)
def main(file: str = "tabs.yml"):
    global data
    if data is None:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

if __name__ == "__main__":
    app()