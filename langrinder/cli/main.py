from pathlib import Path

from typer import Argument, Option, Typer, echo

from langrinder import ABCCompiler, ABCParser, ParserParameters
from langrinder.tools.imports import import_class

app = Typer()

DEFAULT_LOCALES = "*"
DEFAULT_COMPILER = "langrinder.JSONCompiler"
DEFAULT_PARSER = "langrinder.CommonParser"
ERROR_COMPILER = "Compiler must be a subclass of ABCCompiler"
ERROR_PARSER = "Parser must be a subclass of ABCParser"

default_params = ParserParameters()


@app.command("compile")
def compile_locales(
    locales_dir: str = Argument(
        ..., help="Directory containing .mako locale files",
    ),
    output_file: str = Argument(..., help="Path to output compiled file"),
    locales: str = Option(
        DEFAULT_LOCALES,
        "--locales",
        "-l",
        help="Comma-separated list of locales to compile (e.g. 'ru,en')",
    ),
    _compiler: str = Option(
        DEFAULT_COMPILER,
        "--compiler",
        "-c",
        help="Dotted path to compiler class",
    ),
    parser: str = Option(
        DEFAULT_PARSER,
        "--parser",
        "-p",
        help="Dotted path to parser class",
    ),
    vars_prefix: str = Option(default_params.vars_prefix),
    indent: str = Option(default_params.indent),
    blocks_end: str = Option(default_params.blocks_end),
    joiner: str = Option(default_params.joiner),
    message_separators: str = Option(
        ",".join(default_params.message_separators),
        help="Comma-separated list of message separators",
    ),
):
    echo("Compiling...")
    compiler = import_class(_compiler)
    if not issubclass(compiler, ABCCompiler):
        raise TypeError(ERROR_COMPILER)

    parser_class: type[ABCParser] = import_class(parser)
    if not issubclass(parser_class, ABCParser):
        raise TypeError(ERROR_PARSER)

    locale_list = (
        DEFAULT_LOCALES
        if locales == DEFAULT_LOCALES
        else locales.split(",")
    )
    separators = message_separators.split(",")

    params = ParserParameters(
        vars_prefix=vars_prefix, # type: ignore
        indent=indent, # type: ignore
        blocks_end=blocks_end, # type: ignore
        joiner=joiner, # type: ignore
        message_separators=separators, # type: ignore
    )
    results = {}

    compiled = (False, "")

    for file in Path(locales_dir).rglob("*.mako"):
        relative_path = file.relative_to(locales_dir)
        locale = relative_path.parts[0]

        if locale_list != DEFAULT_LOCALES and locale not in locale_list:
            continue

        echo(f"    > {locale}: '{file.stem}'")

        with file.open("r", encoding="utf-8") as f:
            content = f.readlines()

        parser_instance = parser_class(content=content, params=params) # type: ignore
        parsed = parser_instance.parse_all()
        if parsed:
            if results.get(locale):
                results[locale].update(parsed)
            else:
                results[locale] = {}
                results[locale].update(parsed)

        compiled = compiler.compile(results)
    if isinstance(compiled, tuple):
        compiled = compiled[1]

    if not compiled:
        return echo("Result is None!")

    Path(output_file).write_text(compiled, encoding="utf-8")
    return echo("Locales compiled sucessfully!")
