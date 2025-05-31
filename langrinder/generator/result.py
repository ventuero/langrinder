import logging
import time
from dataclasses import dataclass

from mako.template import Template

logger = logging.getLogger(__name__)


@dataclass
class TextResult:
    template: Template
    args: dict

    def __call__(self, **kwargs):
        start = time.perf_counter()
        rendered = self.template.render(
            **self.args,
            **kwargs,
        )
        stop = time.perf_counter()
        logger.debug("Rendered in %f s", stop - start)
        logger.debug("Render result: %s", rendered)

        return rendered
