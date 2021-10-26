<p align="center">
The pipi tool is to install PyPi packages using pip from any source: dir, PyPi projects, Github.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20tool%20to%20install%20PyPi%20packages!&url=https://github.com/anki-code/pipi" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
python -m pip install -U git+https://github.com/anki-code/pipi
```

## Usage

```bash
pipi .                                                         # install from dir
pipi https://github.com/anki-code/xontrib-prompt-bar           # install from repo
pipi https://github.com/anki-code/xonsh/tree/history_json_dir  # install from branch
pipi git@github.com:xonsh/xonsh.git                            # install from git
```
