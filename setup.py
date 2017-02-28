# fake minimal setup for Invoke

project = dict(
    name = 'py-generic-project',
    version = '1.2',
    packages = [],
    url='https://github.com/Springerle/py-generic-project',
)

if __name__ == '__main__':
    import setuptools
    setuptools.setup(**project)
