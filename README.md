# 🌍 Langrinder
Engine for i18n with telegrinder integration based on mako!

---

## 🤔 Why Langrinder?
- Based on mako templates
    Maximum flexibility and comfort
- Compiles directly into Python classes
- Variety of built-in functions and templates

---

## 📥 Installation
```shell
pip install git+github.com/tirch/langrinder.git
```
... or with uv:
```shell
uv add github.com/tirch/langrinder.git
```

---

## 📦 Usage
- Configure me in `pyproject.toml`
    ```toml
    # ...
    [tool.langrinder]
    default_locale = "ru"
    node = "langrinder.nodes.ConstLanguageCode"
    locales_path = "examples/locales"
    output = "{locales_path}/i18n.py"
    ```
- Create locales files (`<locale>.mako`)

    `en.mako`:
    ```yaml
    # main
    @start
        Hello, ${f.mention()}!
    ```
    `ru.mako`:
    ```yaml
    # main
    @start
        Привет, ${f.mention()}!
    ```
- Compile translations
    ```shell
    langrinder compile
    ```
- Enjoy! Read the full documentation [here](./docs/index.md)!

---

## 🔒 License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!