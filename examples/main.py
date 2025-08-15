from langrinder import Langrinder

i18n = Langrinder("examples/locales/compiled.json")
ru = i18n.get_manager("ru") # langrinder.LocaleManager
en = i18n.get_manager("en") # langrinder.LocaleManager

print(ru.start(name="Langrinder")) # Привет, Langrinder!
print(en.start(name="Langrinder")) # Hello, Langrinder!

print(ru.some.message()) # Что-то
print(en.some.message()) # Something
