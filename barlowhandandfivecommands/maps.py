"""
Plot parameter maps for the paper.
"""
import json
import itertools
import subprocess

from cldfbench_barlowhandandfive import Dataset


def plot(format, pid, colors, mdpath, mapdir):
    o = mapdir / '{}.{}'.format(pid, format)
    cmd = [
        'cldfbench',
        'cldfviz.map',
        '--parameter', pid,
        '--colormaps',
        json.dumps(colors),
        '--pacific-centered',
        '--no-open',
    ]
    if format == 'html':
        cmd.extend(['--with-layers', '--value-template', '__{code}__'])
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
    readme = ["""\
# Maps

The maps below have been created using the `cldfviz.map` command from the [`cldfviz` package](https://pypi.org/project/cldfviz/).

"""]
    for pid, codes in sorted(parameters.items(), key=lambda t: pids.index(t[0])):
        if pid == 'num_syst':
            continue
        readme.append('## {}\n'.format(
            cldf.get_row('ParameterTable', pid)['Name'].replace('_', ' ')))
        readme.append(cldf.get_row('ParameterTable', pid)['Description'] or '')
        readme.append('\n&nbsp; | Value | Count | Description')
        readme.append('--- | --- | ---:| ---')
        for c in codes:
            readme.append('$${{\color{{{}}}⏺}}$$ | {} | {} | {}'.format(
                c['color'], c['Name'], value_count[c['ID']], c['Description']))
        readme.append('&nbsp; | &nbsp; | **{}** | &nbsp;'.format(sum(value_count[c['ID']] for c in codes)))

        plotargs = (
            pid, {c['ID']: c['color'] for c in codes}, cldf.directory / cldf.filename, mapdir)
        p = plot('svg', *plotargs)
        readme.append('\n![{}]({})\n'.format(pid, p.name))
        p = plot('html', *plotargs)
        html = p.read_text(encoding='utf8')
        for c in codes:
            html = html.replace('__' + c['ID'] + '__', c['Name'])
        p.write_text(html, encoding='utf8')
        readme.append(
            'View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/'
            '{}.html).\n'.format(pid))
    #
    # Now add a "numeral systems" map
    #
    o = mapdir / 'num_syst.svg'
    cmd = [
        'cldfbench',
        'cldfviz.map',
        '--parameter', 'num_syst',
        '--language-properties', 'Melanesia',
        '--colormaps',
        json.dumps({c['ID']: c['color'] for c in parameters['num_syst']}),
        '--language-properties-colormaps', '{"yes":"circle","no":"triangle_up"}',
        '--pacific-centered',
        '--no-open',
        '--format', 'svg',
        '--padding-top', '5',
        '--padding-bottom', '5',
        '--projection', 'Mollweide',
        '--width', '10',
        '--markersize', '4',
        '--with-ocean',
        '--no-legend',
        '--output', str(o),
        str(cldf.directory / cldf.filename)]
    subprocess.check_call(cmd)
    assert o.exists()

    readme.append('## {}\n'.format(
        cldf.get_row('ParameterTable', pid)['Name'].replace('_', ' ')))
    readme.append(cldf.get_row('ParameterTable', pid)['Description'])
    readme.append('\n&nbsp; | Value | Count | Description')
    readme.append('--- | --- | ---:| ---')
    for c in codes:
        readme.append('$${{\color{{{}}}⏺}}$$ | {} | {} | {}'.format(
            c['color'], c['Name'], value_count[c['ID']], c['Description']))
    readme.append('&nbsp; | &nbsp; | **{}** | &nbsp;'.format(sum(value_count[c['ID']] for c in codes)))

    readme.append('\n&nbsp; | Value | Count | Description')
    readme.append('---:| --- | ---:| ---')
    readme.append('⏺| Melanesian | {} | '.format(sum(1 for l in cldf['LanguageTable'] if l['Melanesian'] == 'yes')))
    readme.append('▼| Non-melanesian | {} | '.format(sum(1 for l in cldf['LanguageTable'] if l['Melanesian'] == 'no')))

    readme.append('\n![num_syst](num_syst.svg)\n')

    o = mapdir / 'num_syst.html'
    cmd = [
        'cldfbench',
        'cldfviz.map',
        '--parameter', 'num_syst',
        '--language-properties', 'Melanesian',
        '--colormaps',
        json.dumps({c['ID']: c['color'] for c in parameters['num_syst']}),
        '--language-properties-colormaps', '{"yes":"circle","no":"triangle_up"}',
        '--pacific-centered',
        '--no-open',
        '--with-layers',
        '--value-template', '__{code}__',
        '--output', str(o),
        str(cldf.directory / cldf.filename)]
    subprocess.check_call(cmd)
    assert o.exists()

    html = o.read_text(encoding='utf8').replace('__no__', 'no').replace('__yes__', 'yes')
    for c in parameters['num_syst']:
        html = html.replace('__' + c['ID'] + '__', c['Name'])
    o.write_text(html, encoding='utf8')
    readme.append(
        'View [interactive map](https://cldf-datasets.github.io/barlowhandandfive/maps/'
        'num_syst.html).\n')
    mapdir.joinpath('README.md').write_text('\n'.join(readme))
