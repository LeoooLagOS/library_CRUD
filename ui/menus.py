from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from ui.i18n import t
from ui.tables import build_users_table, build_books_table
from core.models import User, Book
from core.storage import load_data, save_data, USERS_FILE, BOOKS_FILE

console = Console()


def print_message(view: str, key: str, style: str = "white"):
    console.print(f"[{style}]{t(view, key)}[/{style}]")


def display_main_menu():
    console.clear()
    menu_text = (
        f"[bold green]{t('main_menu', 'opt_users')}[/bold green]\n"
        f"[bold blue]{t('main_menu', 'opt_books')}[/bold blue]\n"
        f"[bold yellow]{t('main_menu', 'opt_loans')}[/bold yellow]\n"
        f"[bold red]{t('main_menu', 'opt_exit')}[/bold red]"
    )
    console.print(Panel(
        menu_text,
        title=f"[bold cyan]{t('main_menu', 'title')}[/bold cyan]",
        border_style="cyan",
        expand=False
    ))


def generate_user_id(users_data: list) -> str:
    """Busca el ID más alto y genera el siguiente en formato U-XXX."""
    max_id = 0
    for u in users_data:
        uid = u.get("user_id", "")
        if uid.startswith("U-"):
            try:
                num = int(uid.split("-")[1])
                if num > max_id:
                    max_id = num
            except ValueError:
                pass
    return f"U-{(max_id + 1):03d}"


def ask_valid_input(view: str, key: str, default_val: str = None) -> str:
    """Valida que el input no esté vacío y permite cancelar con :q"""
    prompt_str = t(view, key)
    if default_val:
        prompt_str += t('users', 'keep_current').format(default_val)
    prompt_str += f" [dim]{t('common', 'type_cancel')}[/dim]"

    while True:
        # Forzamos a rich a que siempre devuelva un string ("" en lugar de None)
        # y desactivamos su UI de default automático
        val = Prompt.ask(
            prompt_str,
            default=default_val if default_val else "",
            show_default=False
        )

        if val == ":q":
            return None  # Señal para abortar la operación

        # Ahora val está garantizado de ser un string, por lo que .strip() no fallará
        if not val.strip():
            print_message('common', 'error_empty', 'bold red')
        else:
            return val.strip()


def generate_book_id(books_data: list) -> str:
    """Genera IDs con formato B-XXX."""
    max_id = 0
    for b in books_data:
        bid = b.get("book_id", "")
        if bid.startswith("B-"):
            try:
                num = int(bid.split("-")[1])
                if num > max_id:
                    max_id = num
            except ValueError:
                pass
    return f"B-{(max_id + 1):03d}"


def ask_valid_int(view: str, key: str, default_val: str = None) -> int:
    """Valida que el input sea numérico y no vacío."""
    while True:
        val_str = ask_valid_input(view, key, default_val)
        if val_str is None:
            return None  # Cancelado con :q

        try:
            return int(val_str)
        except ValueError:
            print_message('books', 'error_invalid_int', 'bold red')

def manage_users_menu():
    """Controlador del submenú para el CRUD de Usuarios."""
    while True:
        console.clear()
        console.print(f"[bold cyan]--- {t('users', 'title')} ---[/bold cyan]")
        console.print(t('users', 'opt_add'))
        console.print(t('users', 'opt_list'))
        console.print(t('users', 'opt_update'))
        console.print(t('users', 'opt_delete'))
        console.print(t('users', 'opt_back'))

        choice = Prompt.ask(f"\n[bold cyan]{t('common', 'prompt_choice')} [1/2/3/4/5][/bold cyan]")

        if choice == "1":
            # --- CREATE ---
            users_data = load_data(USERS_FILE)

            # Generar ID automáticamente
            user_id = generate_user_id(users_data)
            console.print(f"\n[bold yellow]{t('users', 'generated_id')}: {user_id}[/bold yellow]")

            fname = ask_valid_input('users', 'prompt_fname')
            if fname is None:
                print_message('common', 'cancel_msg', 'yellow')
                Prompt.ask(t('common', 'press_enter'))
                continue

            lname_p = ask_valid_input('users', 'prompt_lname_p')
            if lname_p is None:
                print_message('common', 'cancel_msg', 'yellow')
                Prompt.ask(t('common', 'press_enter'))
                continue

            lname_m = ask_valid_input('users', 'prompt_lname_m')
            if lname_m is None:
                print_message('common', 'cancel_msg', 'yellow')
                Prompt.ask(t('common', 'press_enter'))
                continue

            new_user = User(user_id, fname, lname_p, lname_m)
            users_data.append(new_user.to_dict())
            save_data(USERS_FILE, users_data)

            print_message('users', 'success_added', "bold green")
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "2":
            # --- READ ---
            users_data = load_data(USERS_FILE)
            table = build_users_table(users_data)
            console.print(table)
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "3":
            # --- UPDATE ---
            users_data = load_data(USERS_FILE)
            uid_to_update = ask_valid_input('users', 'prompt_update_id')
            if uid_to_update is None:
                continue

            user_found = False

            for u in users_data:
                if u.get("user_id") == uid_to_update:
                    user_found = True

                    fname = ask_valid_input('users', 'prompt_fname', u.get('first_name'))
                    if fname is None: break

                    lname_p = ask_valid_input('users', 'prompt_lname_p', u.get('last_name_paternal'))
                    if lname_p is None: break

                    lname_m = ask_valid_input('users', 'prompt_lname_m', u.get('last_name_maternal'))
                    if lname_m is None: break

                    u["first_name"] = fname
                    u["last_name_paternal"] = lname_p
                    u["last_name_maternal"] = lname_m

                    save_data(USERS_FILE, users_data)
                    print_message('users', 'success_updated', "bold green")
                    break

            if not user_found and uid_to_update is not None:
                print_message('users', 'error_not_found', "bold red")

            Prompt.ask(t('common', 'press_enter'))

        elif choice == "4":
            # --- DELETE ---
            users_data = load_data(USERS_FILE)
            uid_to_delete = ask_valid_input('users', 'prompt_delete_id')

            if uid_to_delete is None:
                print_message('common', 'cancel_msg', 'yellow')
                Prompt.ask(t('common', 'press_enter'))
                continue

            filtered_data = [u for u in users_data if u.get("user_id") != uid_to_delete]

            if len(filtered_data) < len(users_data):
                save_data(USERS_FILE, filtered_data)
                print_message('users', 'success_deleted', "bold green")
            else:
                print_message('users', 'error_not_found', "bold red")

            Prompt.ask(t('common', 'press_enter'))

        elif choice == "5":
            break

        else:
            print_message('common', 'invalid_opt', "bold red")
            Prompt.ask(t('common', 'press_enter'))


def manage_books_menu():
    """Controlador del submenú para el CRUD de Libros."""
    while True:
        console.clear()
        console.print(f"[bold blue]--- {t('books', 'title')} ---[/bold blue]")
        console.print(t('books', 'opt_add'))
        console.print(t('books', 'opt_list'))
        console.print(t('books', 'opt_update'))
        console.print(t('books', 'opt_delete'))
        console.print(t('books', 'opt_back'))

        choice = Prompt.ask(f"\n[bold cyan]{t('common', 'prompt_choice')} [1/2/3/4/5][/bold cyan]")

        if choice == "1":
            books_data = load_data(BOOKS_FILE)
            book_id = generate_book_id(books_data)
            console.print(f"\n[bold yellow]{t('books', 'generated_id')}: {book_id}[/bold yellow]")

            title = ask_valid_input('books', 'prompt_title')
            if title is None: continue

            author = ask_valid_input('books', 'prompt_author')
            if author is None: continue

            stock = ask_valid_int('books', 'prompt_stock')
            if stock is None: continue

            new_book = Book(book_id, title, author, stock)
            books_data.append(new_book.to_dict())
            save_data(BOOKS_FILE, books_data)

            print_message('books', 'success_added', "bold green")
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "2":
            books_data = load_data(BOOKS_FILE)
            table = build_books_table(books_data)
            console.print(table)
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "3":
            books_data = load_data(BOOKS_FILE)
            bid_to_update = ask_valid_input('books', 'prompt_update_id')
            if bid_to_update is None: continue

            book_found = False
            for b in books_data:
                if b.get("book_id") == bid_to_update:
                    book_found = True

                    title = ask_valid_input('books', 'prompt_title', b.get('title'))
                    if title is None: break

                    author = ask_valid_input('books', 'prompt_author', b.get('author'))
                    if author is None: break

                    stock = ask_valid_int('books', 'prompt_stock', str(b.get('stock')))
                    if stock is None: break

                    b["title"] = title
                    b["author"] = author
                    b["stock"] = stock

                    save_data(BOOKS_FILE, books_data)
                    print_message('books', 'success_updated', "bold green")
                    break

            if not book_found and bid_to_update is not None:
                print_message('books', 'error_not_found', "bold red")

            Prompt.ask(t('common', 'press_enter'))

        elif choice == "4":
            books_data = load_data(BOOKS_FILE)
            bid_to_delete = ask_valid_input('books', 'prompt_delete_id')
            if bid_to_delete is None: continue

            filtered_data = [b for b in books_data if b.get("book_id") != bid_to_delete]

            if len(filtered_data) < len(books_data):
                save_data(BOOKS_FILE, filtered_data)
                print_message('books', 'success_deleted', "bold green")
            else:
                print_message('books', 'error_not_found', "bold red")

            Prompt.ask(t('common', 'press_enter'))

        elif choice == "5":
            break
        else:
            print_message('common', 'invalid_opt', "bold red")
            Prompt.ask(t('common', 'press_enter'))
from rich.table import Table
from ui.i18n import t

def build_users_table(users_data: list) -> Table:
    table = Table(title=t('users', 'title'), style="cyan")
    table.add_column("ID", style="bold yellow")
    table.add_column("First Name", style="white")
    table.add_column("Paternal", style="white")
    table.add_column("Maternal", style="white")
    table.add_column("Borrowed", justify="center")

    for u in users_data:
        borrowed = str(len(u.get("borrowed_books", [])))
        table.add_row(
            u.get("user_id", ""),
            u.get("first_name", ""),
            u.get("last_name_paternal", ""),
            u.get("last_name_maternal", ""),
            borrowed
        )
    return table

def build_books_table(books_data: list) -> Table:
    table = Table(title=t('books', 'title'), style="blue")
    table.add_column("ID", style="bold yellow")
    table.add_column("Title", style="white")
    table.add_column("Author", style="white")
    table.add_column("Stock", justify="right")
    table.add_column("Status", justify="center")

    for b in books_data:
        stock = int(b.get("stock", 0))
        status = "[green]Available[/green]" if stock > 0 else "[red]Out of Stock[/red]"
        table.add_row(
            b.get("book_id", ""),
            b.get("title", ""),
            b.get("author", ""),
            str(stock),
            status
        )
    return table


def manage_loans_menu():
    """Controlador del submenú para Préstamos y Devoluciones."""
    while True:
        console.clear()
        console.print(f"[bold yellow]--- {t('loans', 'title')} ---[/bold yellow]")
        console.print(t('loans', 'opt_borrow'))
        console.print(t('loans', 'opt_return'))
        console.print(t('loans', 'opt_back'))

        choice = Prompt.ask(f"\n[bold cyan]{t('common', 'prompt_choice')} [1/2/3][/bold cyan]")

        if choice == "1":
            # --- PRESTAR (BORROW) ---
            uid = ask_valid_input('loans', 'prompt_uid')
            if uid is None: continue

            users_data = load_data(USERS_FILE)
            user_idx = next((i for i, u in enumerate(users_data) if u.get("user_id") == uid), None)

            if user_idx is None:
                print_message('users', 'error_not_found', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            borrowed_list = users_data[user_idx].get("borrowed_books", [])
            if len(borrowed_list) >= 3:
                print_message('loans', 'err_max_books', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            bid = ask_valid_input('loans', 'prompt_bid')
            if bid is None: continue

            books_data = load_data(BOOKS_FILE)
            book_idx = next((i for i, b in enumerate(books_data) if b.get("book_id") == bid), None)

            if book_idx is None:
                print_message('books', 'error_not_found', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            if int(books_data[book_idx].get("stock", 0)) <= 0:
                print_message('loans', 'err_no_stock', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            # Ejecutar transacción
            users_data[user_idx]["borrowed_books"].append(bid)
            books_data[book_idx]["stock"] = int(books_data[book_idx]["stock"]) - 1

            save_data(USERS_FILE, users_data)
            save_data(BOOKS_FILE, books_data)

            print_message('loans', 'success_borrow', "bold green")
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "2":
            # --- DEVOLVER (RETURN) ---
            uid = ask_valid_input('loans', 'prompt_uid')
            if uid is None: continue

            users_data = load_data(USERS_FILE)
            user_idx = next((i for i, u in enumerate(users_data) if u.get("user_id") == uid), None)

            if user_idx is None:
                print_message('users', 'error_not_found', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            bid = ask_valid_input('loans', 'prompt_bid')
            if bid is None: continue

            borrowed_list = users_data[user_idx].get("borrowed_books", [])
            if bid not in borrowed_list:
                print_message('loans', 'err_not_borrowed', 'bold red')
                Prompt.ask(t('common', 'press_enter'))
                continue

            books_data = load_data(BOOKS_FILE)
            book_idx = next((i for i, b in enumerate(books_data) if b.get("book_id") == bid), None)

            # Ejecutar transacción inversa
            users_data[user_idx]["borrowed_books"].remove(bid)
            if book_idx is not None:
                books_data[book_idx]["stock"] = int(books_data[book_idx]["stock"]) + 1
                save_data(BOOKS_FILE, books_data)

            save_data(USERS_FILE, users_data)

            print_message('loans', 'success_return', "bold green")
            Prompt.ask(t('common', 'press_enter'))

        elif choice == "3":
            break
        else:
            print_message('common', 'invalid_opt', "bold red")
            Prompt.ask(t('common', 'press_enter'))
