from dataclasses import asdict
from pathlib import Path
from pprint import pformat

from typer import Option, Typer, echo

from langrinder.cli.formatter import loading, message, success
from langrinder.config import config
from langrinder.generator import LangrinderTranslationsGenerator

cli = Typer()


@cli.command("compile", help="Compile locales from dir")
def compile_locales(
    gen_init: bool = Option(  # noqa: FBT001
        default=False,
        help="Generate __init__.py in i18n directory",
    ),
):
    anim = loading("Compiling...")
    anim.start()
    LangrinderTranslationsGenerator.generate()
    if gen_init:
        import_path = (
            config.output
            .replace("/", ".")
            .replace(".py", "")
        )
        generated_init = (
            f"from {import_path} import {config.translation_name}\n"
        )
        with (Path(config.output).parent / "__init__.py").open("w") as f:
            f.write(generated_init)
    anim.succeed(success("Locales compiled!"))


@cli.command("config", help="See Langrinder config")
def see_config():
    echo(message("Current config", "\n" + pformat(asdict(config))))
