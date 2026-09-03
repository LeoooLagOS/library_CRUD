from rich.table import Table
from ui.i18n import t


def build_users_table(users_data: list) -> Table:
    """Construye la tabla de rich para mostrar los usuarios usando i18n."""
    table = Table(title=t('users', 'title'), style="cyan")
    table.add_column(t('users', 'col_id'), style="bold yellow")
    table.add_column(t('users', 'col_fname'), style="white")
    table.add_column(t('users', 'col_lname_p'), style="white")
    table.add_column(t('users', 'col_lname_m'), style="white")
    table.add_column(t('users', 'col_borrowed'), justify="center")

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
    """Construye la tabla de rich para mostrar los libros usando i18n."""
    table = Table(title=t('books', 'title'), style="blue")
    table.add_column(t('books', 'col_id'), style="bold yellow")
    table.add_column(t('books', 'col_title'), style="white")
    table.add_column(t('books', 'col_author'), style="white")
    table.add_column(t('books', 'col_stock'), justify="right")
    table.add_column(t('books', 'col_status'), justify="center")

    for b in books_data:
        stock = int(b.get("stock", 0))

        # El estado también se traduce dinámicamente
        if stock > 0:
            status = f"[green]{t('books', 'status_avail')}[/green]"
        else:
            status = f"[red]{t('books', 'status_out')}[/red]"

        table.add_row(
            b.get("book_id", ""),
            b.get("title", ""),
            b.get("author", ""),
            str(stock),
            status
        )
    return table