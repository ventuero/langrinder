@start
    Hi, i am bot from ${F.link(F.bold("Langrinder"), "github.com/tirch/langrinder")} example!

@help
    ${F.bold(f"Meow, {F.mention()}!")}
    Here we are testing Langrinder

@nested_start Here is start message: ${this.start()}

@friends I have ${fr_arg} ${plural(fr_arg, "friend", "friends")}
@iam You are ${gender("male", "female", "oak?")}
@meow ${meow}
@nowtime Now ${time.in_words(now, seconds=False)}