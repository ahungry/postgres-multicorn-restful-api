# Postgres Multicorn Foreign Data Wrapper for RESTful API

Modified from: https://github.com/schne324/foreign-keycloak-wrapper

# Installation

## Prerequisites

PostgreSQL must be linked against Python in order to use Multicorn extensions. You can check whether Python is enabled by examining the output of `pg_config --configure` for the `--with-python` flag.

Multicorn must be installed alongside foreign-keycloak-wrapper. This is available through PGXN or can be installed manually. On OSX there may be issues which necessitate a manual install; see Troubleshooting below.

After installing foreign-keycloak-wrapper, PostgreSQL must be restarted.

## Python Versions

Whether Postgres uses Python 2 or 3 is important: this determines the appropriate installation directory for the extension. `pg_config --configure` may show a `PYTHON` environment variable, or your package manager may show which version of Python Postgres was built with (`brew info postgresql`). Unfortunately, there is not a consistent way to determine the correct version.

If Postgres' Python version is different from your system Python (`python --version`) you will need to set the `PYTHON` environment variable to the correct Python executable when installing.

## PGXN

To use PGXN, install `pgxnclient` through `pip`.

PostgreSQL

## Manually

Install Multicorn, then clone this repository.

```bash
$ make install
```

# Usage

```sql
CREATE EXTENSION IF NOT EXISTS multicorn;

DROP SERVER IF EXISTS ahu_fdw CASCADE;

CREATE SERVER ahu_fdw FOREIGN DATA WRAPPER multicorn OPTIONS(
  wrapper 'ahu.Ahu',
  url 'http://ahungry.com',
);

CREATE FOREIGN TABLE wts (
  id text,
  seller text,
  listing text) SERVER ahu_fdw;

SELECT * FROM wts;

-- Oh, you want it faster?  use a materialized view to cache it:
DROP MATERIALIZED VIEW IF EXISTS mv_wts;
CREATE MATERIALIZED VIEW mv_wts AS SELECT * FROM wts;

-- Periodically refresh (use a trigger or something)
REFRESH MATERIALIZED VIEW mv_wts;
```

If you see an ImportError when trying to `CREATE SERVER` doublecheck
your python versions and make sure ahu is installed to the site-packages directory of the Python version Postgres expects.

# Troubleshooting

## Multicorn on OSX

In [some OSX environments](https://github.com/Kozea/Multicorn/issues/139) Multicorn must be installed manually. Clone the [Multicorn repository](https://github.com/Kozea/Multicorn) and edit the Makefile, changing `darwin` to `Darwin`. Then `make && sudo ARCHFLAGS="-arch x86_64" make install`.
