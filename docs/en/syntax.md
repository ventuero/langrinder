# 📝 Syntax

Langrinder's syntax is maximally simple, Mako's is slightly more complex.
Here are the main and most important concepts.

## 🌍 Langrinder

### 🔤 Text Blocks

No one will write each line as a separate variable.
Therefore, text blocks were created.

```mako
@variable
    your text
```

By default, each line is joined by a newline.
Of course, this is configurable (see [configuration](./config.md))
Variable names can contain numbers, letters, and underscores.

### ⚪️ Variables

Basic variables are created like this:

```mako
@foo = bar
@meow purr
```

(can be separated by = or a space)

## ✒️ Mako

Mako's syntax already contains all the power of this translation engine.
Let's consider its syntax below.

### 🖼 Embeddings

You can write Python code directly in localization files\!
This provides maximum flexibility and functionality.

```mako
@meow
    Purr, ${user}
```

In this case, the `user` variable is provided by the user.
But Langrinder also injects its own variables. See below.

### 💟 Default Variables

And here they are, Langrinder's variables.
They contain templates and other utilities.

  - ✍️ `F` - Formatting
      - `F.bold`: Creates bold text. `F.bold("text")`
      - `F.mono`: Creates monospace text. `F.mono("text")`
      - `F.italic`: Creates italic text. `F.italic("text")`
      - `F.(ex)quote`: Creates a quote (ex - expandable).
          - `F.quote("text")`
          - `F.exquote("big text")`
      - `F.link`: Creates a link. `F.link("text", url="https://example.com")`
      - `F.urlbutton`: Creates a URL-button.
          - `F.urlbutton("text", url="https://example.com")`
          - `F.urlbutton("text2", url="https://nometa.xyz", same=True) # Places the button on the same row`
  - ℹ️ `this` - A reference to itself (to the translation pack).
      - Allows retrieving variables from its own pack:
        ```mako
        Foo: ${this.bar()}
        ```
  - 👥 `gender` - Gender-dependent forms.
      - `You are ${gender("a man", "a woman", "an oak tree?")}` - masculine, feminine, neutral (other).
      - Use `gender=langrinder.tools.Gender (StrEnum)` to specify gender.
  - 🔢 `plural` - Number-dependent forms.
      - Supported locales:
          - en
          - ru
          - *Contributing is welcome ;)*
      - `I have ${number} ${plural(number, "friend", "friends", "friends")}`
          - one
          - a few
          - many
  - ⏱️ `time` - Time formatting
      - `${time.in_words(delta, seconds=True)}` - describes a delta in words
          - *18 hours 29 minutes 1 second*
          - `seconds` - whether to add seconds?
      - `${time.diff(dt_or_delta, other=None, absolute=False, seconds=True)}` - Describes the difference between two points in time (or one duration) in words.
          - `dt_or_delta` - compares with current time if it's a datetime and acts like `in_words()`, if it's a delta.
          - `other` - the second point in time for comparison (if None, compares with current time).
          - `absolute` - return only the difference without *"ago"* or *"from now"*.
          - `seconds` - whether to add seconds?
      - `${time.fmt(dt, fmt_string="YYYY-MM-DD")}` - time formatting
          - `dt` - time to format
          - `fmt_string` - formatting template

### 🐍 Python Code

Yes, it was mentioned for a reason.
When viewed in the context of integration with Telegrinder,
you can easily retrieve nodes (by passing them when calling the locale),
call any functions on objects, and so on!

**[◀️ To Table of Contents](./index.md)**