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
pip install git+https://github.com/tirch/langrinder.git
```
> [!NOTE]
> Langrinder is available on PyPI, but is only updated on GitHub 

---

## 📦 Usage
- Configure me in `pyproject.toml`
    ```toml
    # ...
    [tool.langrinder]
    default_locale = "ru"
    node = "langrinder.nodes.ConstLanguageCode"
    locales_path = "examples/locales"
    output = "examples/locales/i18n.py"
    translation_name = "Translation" # i18n class
    # base_node_template = "foo/bar.mako"
    # base_translation_template = "foo2/bar2.mako"
    ```
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
- Compile translations
    ```shell
    langrinder compile
    ```
- Enjoy! Read the full documentation [here](./docs/index.md)!

---

## 🧪 To-Do
- [x] Node based on user Telegram language
- [x] Allow to put args in `F.mention()`
- [x] Plural forms
- [ ] Gender based forms

---

## 🔒 License
Langrinder licensed under [MIT license](LICENSE). Free and open-source!