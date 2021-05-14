# tablist

## Installation

```
pip3 install pyyaml typer typer-cli click click-repl
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
  * [ ] make sections into auto-loaded subcommands with optional arg (no arg
  - lists tabs, number - open specific tab)
* [ ] add tags (brackets after names)
