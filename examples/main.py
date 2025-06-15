from langrinder import Langrinder

i18n = Langrinder("examples/locales/compiled.json")
ru = i18n.locale("ru")
en = i18n.locale("en")

print(ru.start(name="Langrinder")) # Привет, Langrinder!
# `i18n.locale(...)` returns langrinder.LocaleManager
print(en.start(name="Langrinder")) # Hello, Langrinder!

print(ru.some.message()) # Что-то
print(en.some.message()) # Something
