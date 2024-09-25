from setuptools import setup


setup(
    name='cldfbench_barlowhandandfive',
    py_modules=['cldfbench_barlowhandandfive'],
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
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
