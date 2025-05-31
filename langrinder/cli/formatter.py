from colorama import Fore, Style
from halo import Halo


def error(err_type: str, message: str):
    return (
        Fore.RED
        + "(｡•́︿•̀｡) Error! "
        + Fore.RESET
        + Fore.WHITE
        + err_type + ": "
        + Fore.RESET
        + Fore.LIGHTBLACK_EX
        + message
        + Style.RESET_ALL
    )


def loading(text: str):
    return Halo(text=text, spinner="dots")


def success(text: str):
    kaomoji = "(｡•̀ᴗ-)✧"
    return (
        Fore.LIGHTBLUE_EX
        + f"{kaomoji} Yay! "
        + Fore.RESET
        + Fore.WHITE
        + text
        + Style.RESET_ALL
    )


def note(text: str):
    kaomoji = "눈_눈"
    return (
        Fore.YELLOW
        + f"{kaomoji} Note: "
        + Fore.RESET
        + Fore.WHITE
        + text
        + Style.RESET_ALL
    )


def message(title: str, text: str):
    return (
        Fore.LIGHTBLUE_EX
        + f"{title}: "
        + Fore.RESET
        + Fore.WHITE
        + str(text)
        + Style.RESET_ALL
    )
