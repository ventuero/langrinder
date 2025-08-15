<div align="center">
    <h1>Langrinder</h1>
    <i>Flexible internationalization (i18n) engine based on <a href="https://github.com/sqlalchemy/mako">Mako</a> templates</i>
    <br><br>
    <p>
      <a href="#License"><img alt="GitHub License" src="https://img.shields.io/github/license/ventuero/langrinder.svg?color=lightGreen&labelColor=black&style=flat-square"></img></a>
      <a href="https://docs.astral.sh/ruff/"><img alt="Code Style" src="https://img.shields.io/badge/code_style-Ruff-D7FF64?logo=ruff&logoColor=fff&style=flat-square&labelColor=black"></img></a>
      <a href="https://github.com/ventuero/langrinder/blob/master/pyproject.toml"><img alt="Python versions" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fventuero%2Flangrinder%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&style=flat-square&logo=python&logoColor=fff&labelColor=black"></img></a>
      <a href="https://github.com/ventuero/langrinder/blob/master/pyproject.toml">
      <img alt="Project version" src="https://img.shields.io/badge/version-v3.2.0-black?style=flat-square&logo=python&logoColor=fff"></img></a>
    </p>
</div>

## Why Langrinder?
- Based on mako templates. Maximum flexibility and comfort
- Flexible compilers & parsers (default: JSON compiler)
- Variety of built-in functions and integrations
- Telegrinder integration

## Installation
```shell
pip install "langrinder @ git+https://github.com/ventuero/langrinder.git"
pip install "langrinder[telegrinder] @ git+..." # Just install latest telegrinder
pip install "langrinder[cli] @ git+..." # Recommended
```

## Usage
- Create locales files (`locales/<locale>/<smth>.mako`)
    - `locales/en/main.mako`:
        ```mako
        @start: Hello from ${html.bold('Langrinder')}!
        ```
    - `locales/ru/main.mako`:
        ```mako
        @start: Привет от ${html.bold('Langrinder')}!
        ```
- Compile locales
    ```shell
    langrinder locales/ locales/compiled.json
    ```
- Enjoy! See our [main example](./examples/main.py) and [bot example](./examples/bot.py)!

---

## License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!
