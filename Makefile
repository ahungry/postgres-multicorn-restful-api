MODULE_NAME = ahu
PYTHON ?= python2
PKGDIR = $$($(PYTHON) -c "import site; print(site.getsitepackages()[0])")
NAME = $$($(PYTHON) setup.py --name)
VERSION = $$($(PYTHON) setup.py --version)
PYVERSION = $$($(PYTHON) -c "import sys; print(sys.version[:3])")

.PHONY: all install uninstall clean

all: install

install:
	@$(PYTHON) setup.py install

uninstall:
	@rm -f $(PKGDIR)/$(NAME)-$(VERSION)-py$(PYVERSION).egg

clean:
	@$(PYTHON) setup.py clean
