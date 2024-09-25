"""
Plot parameter maps for the paper.
"""
import json
import itertools
import subprocess

from cldfbench_barlowhandandfive import Dataset


def register(parser):
    parser.add_argument('--format', choices=['html', 'svg'], default='svg')


def plot(format, pid, colors, mdpath, mapdir):
    o = mapdir / '{}.{}'.format(pid, format)
    cmd = [
        'cldfbench',
        'cldfviz.map',
        '--parameter', pid,
        '--colormaps',
        json.dumps(colors),
        '--pacific-centered',
    ]
    if format == 'html':
        cmd.append('--with-layers')
    else:  # format == 'svg'
        cmd.extend([
            '--format', 'svg',
            '--padding-top', '5',
            '--padding-bottom', '5',
            '--projection', 'Mollweide',
            '--width', '10',
            '--markersize', '4',
            '--with-ocean',
            '--no-legend',
        ])
    cmd.extend(['--output', str(o), str(mdpath)])
    subprocess.check_call(cmd)
    assert o.exists()
    return o


def run(args):
    cldf = Dataset().cldf_reader()
    mapdir = cldf.directory.parent / 'maps'
    pids = [r['ID'] for r in cldf.iter_rows('ParameterTable')]
    parameters = {
        pid: list(rows) for pid, rows in itertools.groupby(
            sorted(cldf.iter_rows('CodeTable'), key=lambda r: r['Parameter_ID']),
            lambda r: r['Parameter_ID'])}
    value_count = {
        cid: len(list(rows)) for cid, rows in itertools.groupby(
            sorted(cldf.iter_rows('ValueTable'), key=lambda r: r['Code_ID'] or 'xxxx'),
            lambda r: r['Code_ID'])}
    readme = ['# Maps\n']
    for pid, codes in sorted(parameters.items(), key=lambda t: pids.index(t[0])):
        readme.append('## {}\n'.format(cldf.get_row('ParameterTable', pid)['Name'].replace('_', ' ')))
        readme.append('&nbsp; | Description | Count')
        readme.append('--- | --- | ---:')
        for c in codes:
            readme.append('$${{\color{{{}}}⏺}}$$ | {} | {}'.format(
                c['color'], c['Name'], value_count[c['ID']]))
        readme.append('&nbsp; | &nbsp; | **{}**'.format(sum(value_count[c['ID']] for c in codes)))

        p = plot(
            args.format,
            pid,
            {c['ID']: c['color'] for c in codes},
            cldf.directory / cldf.filename,
            mapdir)
        readme.append('\n![{}]({})\n'.format(pid, p.name))
        plot(
            'html',
            pid,
            {c['ID']: c['color'] for c in codes},
            cldf.directory / cldf.filename,
            mapdir)
        readme.append(
            'View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/{}.html).\n'.format(pid))
    mapdir.joinpath('README.md').write_text('\n'.join(readme))
