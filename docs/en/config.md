# ⚙️ Configuration

## 🧩 "Core" Settings

These settings define Langrinder's behavior, compilation, and parsing.
They are set directly within `langrinder.Langrinder.__init__(...)`:

  * `generator: type[LangrinderBaseGenerator] = LangrinderTranslationsGenerator` - Practically the most important parameter.
    It generates the `output_file` and also parses `.mako` files under the hood (via `parser`).
  * `parser: type[LangrinderBaseParser] = LangrinderSyntaxParser` - The parser for text blocks and lines.
    **Important:** All formatting happens solely through Mako; the parser only collects the text\!
  * `node_template: str = "{LANGRINDER_PATH}/generator/templates/node.mako"` - Template for the base node.
  * `translation_template: str = "{LANGRINDER_PATH}/generator/templates/translation.mako"` - Template for the translation node.
  * `translation_name: str = "Translation"` - The name of the translation class.
  * `node: type[Node] = ConstLanguageCode` - The node for retrieving the locale.
  * `logger: logging.Logger | None = None` - Logger (describes generator actions at `DEBUG` level).

## 👀 Behavior Settings

These are defined within `telegrinder.tools.global_context.GlobalContext("langrinder")`:

```python
ctx = GlobalContext("langrinder")
ctx["foo"] = "bar"
```

  * `locale` - The default locale (also used for `ConstUserLocale`).
  * `tz` - The timezone. Specified in `Europe/Moscow` format (e.g., "America/New\_York", "Asia/Tokyo").
  * `args` - Global arguments always passed to the locale (e.g., config, links, or names of entities).
  * `gender_generator` - The generator for gender-dependent forms. Default: `langrinder.tools.GenderGenerator`.
  * `plural_generator` - The generator for quantity-dependent forms. Default: `langrinder.tools.PluralGenerator`.

-----

**[◀️ Back to Table of Contents](./index.md)**