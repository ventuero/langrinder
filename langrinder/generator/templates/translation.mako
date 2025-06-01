

class ${translation_name}(BaseTranslation):
    pack = ${pack if pack else {}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str):
        return self.var(name, this=self)
