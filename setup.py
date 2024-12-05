from setuptools import setup, find_packages


setup(
    name='cldfbench_barlowhandandfive',
    py_modules=['cldfbench_barlowhandandfive'],
    packages=find_packages(where='.'),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'barlowhandandfive=cldfbench_barlowhandandfive:Dataset',
        ],
        'cldfbench.commands': [
            'barlowhandandfive=barlowhandandfivecommands',
        ]
    },
    install_requires=[
        'cldfbench',
        'shapely',
        'clldutils',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
