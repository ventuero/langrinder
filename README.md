<div align="center">
    <h1>Langrinder</h1>
    <i>Engine for i18n with <a href="https://github.com/timoniq/telegrinder">telegrinder</a> integration based on <a href="https://github.com/sqlalchemy/mako">mako</a>!</i>
    <br><br>
    <p>
      <a href="#contributors"><img alt="Still in development" src="https://img.shields.io/badge/still_in_development-E3956B?logo=textpattern&logoColor=fff&style=flat-square&color=black"></img></a>
      <a href="#license"><img alt="GitHub License" src="https://img.shields.io/github/license/timoniq/telegrinder.svg?color=lightGreen&labelColor=black&style=flat-square"></img></a>
      <a href="https://docs.astral.sh/ruff/"><img alt="Code Style" src="https://img.shields.io/badge/code_style-Ruff-D7FF64?logo=ruff&logoColor=fff&style=flat-square&labelColor=black"></img></a>
      <a href="https://github.com/tirch/langrinder/blob/master/pyproject.toml"><img alt="Python versions" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Ftirch%2Flangrinder%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&style=flat-square&logo=python&logoColor=fff&labelColor=black"></img></a>
      <a href="https://github.com/tirch/langrinder/blob/master/pyproject.toml">
      <img alt="Python versions" src="https://img.shields.io/badge/version-v2.1.0-black?style=flat-square&logo=python&logoColor=fff"></img></a>
    </p>
</div>

## Why Langrinder?
- Based on mako templates. Maximum flexibility and comfort
- Compiles directly into Python classes
- Variety of built-in functions, integrations and templates

## Installation
```shell
pip install git+https://github.com/tirch/langrinder.git
uv add "langrinder @ https://github.com/tirch/langrinder.git"
```
> [!NOTE]
> Langrinder is available on PyPI, but is only updated on GitHub

> [!NOTE]
> You can install pendulum for use this integration: `uv add "langrinder[pendulum] @ https://github.com/tirch/langrinder.git"`

## Usage
- Create locales files (`<locale>/<smth>.mako`)
    - `en/main.mako`:
        ```mako
        @start
            Hello, ${F.mention()}!
        ```
    - `ru/main.mako`:
        ```mako
        @start
            Привет, ${F.mention()}!
        ```
- Create `locales/compile.py` (or ahother):
    ```python
    from telegrinder.modules import logger
    from langrinder import Langrinder

    langrinder = Langrinder(logger=logger) # You can input other parser, generator and node here
    langrinder.compile(
        input_dir="locales/",
        output_file="locales/i18n.py",
    )
    ```
- Compile translations
    ```shell
    python3 locales/compile.py
    ```
- Enjoy! Read the full documentation [here](./docs/index.md), and see our [example](./examples/main.py)!

---

## Latest update
### v?.?.?

## License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!
