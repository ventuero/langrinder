import logging
import time
from dataclasses import dataclass

from mako.template import Template
from telegrinder.tools.global_context import GlobalContext, GlobalCtxVar

from langrinder.tools import GenderGenerator

logger = logging.getLogger(__name__)
ctx = GlobalContext("langrinder")


@dataclass
class TextResult:
    template: Template
    args: dict

    def __call__(self, **kwargs):
        start = time.perf_counter()
        if kwargs.get("gender"):
            gender_gen_type = (
                ctx
                .get("gender_generator")
                .unwrap_or_none()
            )
            if gender_gen_type:
                gender_gen = gender_gen_type.value(kwargs["gender"])
            else:
                gender_gen = GenderGenerator(kwargs["gender"])
            kwargs["gender"] = gender_gen.gender
        rendered = self.template.render(
            **self.args,
            **kwargs,
        )
        stop = time.perf_counter()
        logger.debug("Rendered in %f s", stop - start)
        logger.debug("Render result: %s", rendered)

        return rendered
