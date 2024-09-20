#!/usr/bin/env python
import os
import nbformat as nbf
from jinja2 import Environment, FileSystemLoader, select_autoescape
from glob import glob

# A notebook is a CAL notebook if it defines CAL metadata
def is_cal_notebook(path):
    notebook = nbf.read(path, nbf.NO_CONVERT)
    return notebook.get('metadata', {}).hasattr('cal')

# The header cell must carry a cal.metadata tag
def get_or_create_header(notebook):
    header_cell = None
    
    for cell in notebook.cells:
        if 'cal.header' in cell.get('metadata', {}).get('tags', []):
            header_cell = cell
            
    if header_cell is None:
        header_cell = nbf.v4.new_markdown_cell(metadata={'tags': ['cal.header']})
        notebook.cells.insert(0, header_cell)
    
    return header_cell

if __name__ == '__main__':
    home = os.path.expanduser('~')
    
    # Initialize jinja2
    env = Environment(
        loader=FileSystemLoader(f"{home}/cal-notebooks/assets/templates"),
        autoescape=select_autoescape()
    )
    
    # Collect a list of all CAL notebooks in the repository
    notebook_paths = filter(is_cal_notebook, glob(f"{home}/cal-notebooks/**/*.ipynb", recursive=True))
    
    # Update all the headers
    for path in notebook_paths:
        cal_notebook = nbf.read(path, nbf.NO_CONVERT)

        cal_metadata = cal_notebook.get('metadata', {}).get('cal', {})

        template = env.get_template('header.html')
        header = template.render(**cal_metadata)

        header_cell = get_or_create_header(cal_notebook)
        header_cell['source'] = header

        nbf.write(cal_notebook, path)
