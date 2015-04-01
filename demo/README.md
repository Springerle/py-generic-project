# Demo for creating + releasing a project in 10 minutes

## Preparation

Install a few tools.

```sh
# create demo sandbox
rm -rf ~/src/cc-demo; mkdir -p ~/src/cc-demo; cd ~/src/cc-demo

git clone -b "enriched-context-for-hooks" "https://github.com/jhermann/cookiecutter.git"
git clone "https://github.com/jhermann/rituals"
git clone "https://github.com/Springerle/py-generic-project"
git clone "https://github.com/Springerle/dh-virtualenv-mold"
```


## Bootstrap
Now use the locally cloned Cookiecutter template “py-generic-project”
to create our demo project.

```sh
cd py-generic-project
. .env --yes --develop
pip -q install -e ../cookiecutter # activate patched version
cookiecutter --version
```

![Bootstrap #1](img/demo010.png)


```sh
rm -rf new-project # make sure there is nothing there
cookiecutter --no-input .
```

![Bootstrap #2](img/demo020.png)

```sh
cd new-project
git init; git add .
git commit -m "New project from py-generic-project cookiecutter"
git tag -a "v0" -m "Cookiecutter update reference"
```

![Bootstrap #3](img/demo030.png)

```sh
. .env --yes --develop
```

![Bootstrap #4](img/demo040.png)


## Developing

```sh
inv test
```

![Development Test](img/demo110.png)

```sh
inv check
```

![Development Check](img/demo120.png)

```sh
devpi use "http://localhost:3141/"
devpi login "local"
devpi use "local/dev"
```

![Development "devpi use"](img/demo130.png)


```sh
inv bump
inv dist --devpi
```

![Development Dist](img/demo140.png)
…
![Development Dist](img/demo141.png)


```sh
# use this to add new modules with a simple "cp"
view project.d/skeleton_module.py
```


## Releasing

```sh
inv release.prep
```

![Release Prep try'n'error](img/demo151.png)

```sh
git checkout HEAD -- setup.cfg
inv release.prep
git show HEAD
```

![Release Prep #1](img/demo152.png)
…
![Release Prep #2](img/demo153.png)


```sh
inv dist --devpi >/dev/null
devpi list new-project
```

![Release devpi](img/demo160.png)


## Packaging

```sh
cookiecutter ../../dh-virtualenv-mold
dch -r ''
```

![Packaging create 'debian'](img/demo210.png)


```sh
echo "usr/share/python/new-project/bin/new-project usr/bin/new-project-cli" \
    >debian/new-project.links
dpkg-buildpackage -uc -us -b
dpkg -I ../*.deb
```

![Packaging create 'debian'](img/demo220.png)
…
![Packaging create 'debian'](img/demo221.png)


```sh
sudo dpkg -i ../*.deb
/usr/bin/new-project-cli --version
```

![Packaging create 'debian'](img/demo230.png)


## References

**Tools**

* [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.org/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [pypa/setuptools](https://bitbucket.org/pypa/setuptools)
* [twine](https://github.com/pypa/twine#twine)
* [autoenv](https://github.com/kennethreitz/autoenv)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)
* [devpi (DEB)](https://github.com/jhermann/devpi-enterprisey/tree/master/debianized-devpi)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)
* [Click](http://click.pocoo.org/)
