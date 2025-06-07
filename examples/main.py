from langrinder import Langrinder

lgr = Langrinder("examples/locales/compiled.json")
print(lgr.locale("ru").start(name="Langrinder")) # Привет, Langrinder!
# `lgr.locale(...)` return langrinder.LocaleManager
print(lgr.locale("en").start(name="Langrinder")) # Hello, Langrinder!
