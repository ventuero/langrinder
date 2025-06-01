import logging

from langrinder import Langrinder

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

langrinder = Langrinder(logger=logger) # You can input other parser, generator and node here
langrinder.compile(
    input_dir="examples/locales/",
    output_file="examples/locales/i18n.py",
)
