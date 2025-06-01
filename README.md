# 🌍 Langrinder
Engine for i18n with telegrinder integration based on mako!

---

## 🤔 Why Langrinder?
- Based on mako templates
    Maximum flexibility and comfort
- Compiles directly into Python classes
- Variety of built-in functions, integrations and templates

---

## 📥 Installation
```shell
pip install git+https://github.com/tirch/langrinder.git
```
> [!NOTE]
> Langrinder is available on PyPI, but is only updated on GitHub 

---

## 📦 Usage
- Create locales files (`<locale>.mako`)

    `en.mako`:
    ```yaml
    @start
        Hello, ${F.mention()}!
    ```
    `ru.mako`:
    ```yaml
    @start
        Привет, ${F.mention()}!
    ```
- Create `locales/compile.py` (or ahother):
    ```python
    import logging

    from langrinder import Langrinder

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

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

## 🧪 To-Do
### v1.1.0
- [x] Node based on user Telegram language
- [x] Allow to put args in `F.mention()`
- [x] Plural forms
- [x] Gender based forms

### v2.0.0
- [x] Additional args from context
- [x] Use `config.default_locale` if not const locale specified
    > Using `ctx["locale"]`
- [x] [Pendulum](https://github.com/python-pendulum/pendulum) integration
- [x] Flexibility
    > Now without CLI and config in `pyproject.toml`.
    > Only `telegrinder.Telegrinder.compile()` with params
---

## 🔒 License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!