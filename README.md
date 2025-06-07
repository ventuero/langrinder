<div align="center">
    <h1>Langrinder</h1>
    <i>Flexible internationalization (i18n) engine based on <a href="https://github.com/sqlalchemy/mako">Mako</a> templates</i>
    <br><br>
    <p>
      <a href="#"><img alt="Still in development" src="https://img.shields.io/badge/still_in_development-E3956B?logo=textpattern&logoColor=fff&style=flat-square&color=black"></img></a>
      <a href="#License"><img alt="GitHub License" src="https://img.shields.io/github/license/timoniq/telegrinder.svg?color=lightGreen&labelColor=black&style=flat-square"></img></a>
      <a href="https://docs.astral.sh/ruff/"><img alt="Code Style" src="https://img.shields.io/badge/code_style-Ruff-D7FF64?logo=ruff&logoColor=fff&style=flat-square&labelColor=black"></img></a>
      <a href="https://github.com/tirch/langrinder/blob/master/pyproject.toml"><img alt="Python versions" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Ftirch%2Flangrinder%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&style=flat-square&logo=python&logoColor=fff&labelColor=black"></img></a>
      <a href="https://github.com/tirch/langrinder/blob/master/pyproject.toml">
      <img alt="Project version" src="https://img.shields.io/badge/version-v3.0.0-black?style=flat-square&logo=python&logoColor=fff"></img></a>
    </p>
</div>

## Why Langrinder?
- Based on mako templates. Maximum flexibility and comfort
- Compiles directly into Python classes
- Variety of built-in functions and integrations

## Installation
```shell
pip install "langrinder @ git+https://github.com/tirch/langrinder.git"
pip install "langrinder[telegrinder] @ git+..."
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
- Compile translations
    ```shell
    langrinder locales/ locales/compiled.json
    ```
- Enjoy! See our [main example](./examples/main.py) and [bot example](./examples/bot.py)!

---

## Latest update
### v3.0.0 - Big update!
- Free of Telegrinder
- Free of Pendulum (switched to Babel)
- New compiling style
- Code rewriting and refactoring
- CLI interface (`pip install langrinder[cli]`)

## License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!
