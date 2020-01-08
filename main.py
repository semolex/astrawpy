
import os
import rawpy
import imageio
import click

from cfa import CFA
import echo

PREFIX = 'CFA_'


@click.command()
@click.option('-f', '--file', help='File to use.', type=click.Path(exists=True))
@click.option('-d', '--directory',  help='Directory to use.', type=click.Path(exists=True))
@click.option('-o', '--out', default='.', help='Output directory.', type=click.Path(exists=True))
def extract(file, directory, out):
    files = []
    if file:
        files.append(file)
    if directory:
        files.extend([i for i in os.listdir(directory)])

    for _f in files:
        echo.info(f'Using file {_f}')
        with rawpy.imread(_f) as raw:
            cfa = CFA(raw)
            for n, plane in cfa.extract_cfa():
                name = f'{PREFIX}{n}_{_f}.tiff'
                output = os.path.join(out, name)
                echo.info(f'Writing output: {output}')
                imageio.imwrite(output, plane, format='tiff')
                echo.ok(f'File saved: {name}')


if __name__ == '__main__':
    extract()



