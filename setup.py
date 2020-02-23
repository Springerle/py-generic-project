# fake minimal setup for Invoke

project = dict(
    name = 'py-generic-project',
    version = '1.4',
    author='jhermann',
    author_email='jh@web.de',
    license='MIT',
    packages = [],
    url='https://github.com/Springerle/py-generic-project',
    description='A cookiecutter template that creates a basic Python setuptools project.',
)

if __name__ == '__main__':
    import setuptools
    setuptools.setup(**project)
