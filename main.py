from rich.prompt import Prompt
from ui.i18n import set_language, t
from ui.menus import display_main_menu, print_message, manage_users_menu, manage_books_menu, manage_loans_menu


def setup_language():
    lang_choice = Prompt.ask(
        "Select your language / Seleccione su idioma [en/es]",
        default="es",
    )
    if lang_choice not in ["en", "es"]:
        lang_choice = "es"
    set_language(lang_choice)

def main():
    setup_language()

    while True:
        display_main_menu()
        choice = Prompt.ask(f"[bold cyan]{t('common', 'prompt_choice')} [1/2/3/4][/bold cyan]")
        if choice == "1":
            manage_users_menu()

        elif choice == "2":
            manage_books_menu()

        elif choice == "3":
            manage_loans_menu()

        elif choice == "4":
            print_message('common', 'goodbye', "bold green")
            break
        else:
            print_message('common', 'invalid_opt', "bold red")
            Prompt.ask(t('common', 'press_enter'))

if __name__ == "__main__":
    main()