# m-dfp

A Python library to read Microchip Device Family Packs.

Exposes the xml as simple python properties. Follows the names and 
organisation of the original atdf file as possible. Most likely to 
be used by those who rarely use xml.

Only content likely to be used for generating visual datasheets is 
implemented at this point.

### Library Installation
```
mkdir <project-master>
cd <project-master>
python -m venv --prompt <my-prompt> venv
source venv/bin/activate
git clone github.com/coburnw/m-dfp
cd m-dfp
pip install --editable .
```

### Microchip DFP Installation
(see https://www.microchipdeveloper.com/xcc:introduction-to-dfps for info on what a DFP is)

* Download the latest from https://packs.download.microchip.com/
* rename the suffix to .zip
* unzip into <project-master> directory

### Use
```
python src/example/example.py
```