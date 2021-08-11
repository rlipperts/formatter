# text formatter
Simple text output formatter that helps with printing pretty stuff 

## installation
There are no PyPI releases. Neither are they planned.

### manual
For installation with pip directly from this GitHub repository simply open a terminal and type
```
pip install git+ssh://git@github.com/rlipperts/formatter.git
```

### setup.py
To automatically install the text formatter with your python package include these lines in your setup.py
```python
install_requires = [
    'text-formatter @ git+ssh://git@github.com/rlipperts/formatter.git@master#egg=text-formatter-0.0.2',
],
```
Make sure you update the version in the `egg=text-formatter-...` portion to the correct version specified in the logging-configurators setup.py. This might not work if you plan on publishing your package on PyPI.

## usage

Just wrap your text inside the functions and see what happens.
