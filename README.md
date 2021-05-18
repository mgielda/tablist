# tablist

## Installation

```
pip3 install pyyaml typer typer-cli click click-repl
```

## Preparation

You will need a YAML config file in `~/.tablist.yml`:

```
Section name 1:
  Tab name 1: https://some.url.com
  Tab name 2: https://another.url.com
Section name 2:
  Tab name 3: https://yet.another.url.com
```

## Running

Run using:

```
./tablist.py
```

## Generating help

```
typer tablist.py utils docs
```

## TODO

* [ ] simpler usage (to be replicated with aliases for now)
  * [ ] make it list sections by default (may be difficult - see [issue](https://github.com/tiangolo/typer/issues/18))
  * [ ] non-existing command lists sections
  * [ ] make sections into auto-loaded subcommands with optional arg (no arg - lists tabs, number - open specific tab)
* [ ] add tags (brackets after names)
* [X] add fuzzy find
* [X] shorten command names
* [ ] add remote endpoints (e.g. GH issues) via twill with caching/indexing - and fuzzy search
