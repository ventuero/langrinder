from langrinder import Langrinder
from telegrinder.modules import logger

langrinder = Langrinder(logger=logger) # You can input other parser, generator and node here
langrinder.compile(
    input_dir="examples/locales/",
    output_file="examples/locales/i18n.py",
)
