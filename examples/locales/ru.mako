@start
    Привет, я бот из примера ${F.link(F.bold("Langrinder"), "github.com/tirch/langrinder")}!

@help
    ${F.bold(f"Мяу, {F.mention()}!")}
    Здесь мы тестируем Langrinder

@nested_start Вот стартовое сообщение: ${this.start()}
@friends У меня есть ${fr_arg} ${plural(fr_arg, "друг", "друга", "друзей")}
@iam Ты ${gender("мальчик", "девочка", "дуб?")}
@meow ${meow}
@nowtime Сейчас ${time.in_words(now, seconds=False)}