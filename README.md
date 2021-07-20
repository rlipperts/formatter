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
To automatically install the logging configurator with your python package include these lines in your setup.py
```python
install_requires = [
    'text-formatter @ git+ssh://git@github.com/rlipperts/formatter.git@master#egg=text-formatter-0.0.2',
],
```

## usage

Just wrap your text inside the functions and see what happens.
