# ui/i18n.py

translations = {
    "en": {
        "common": {
            "prompt_lang": "Select your language / Seleccione su idioma [en/es]",
            "prompt_choice": "Select an option:",
            "invalid_opt": "Invalid option. Please try again.",
            "press_enter": "Press Enter to continue...",
            "goodbye": "Shutting down system. Goodbye!",
            "error_empty": "Error: Field cannot be empty.",
            "cancel_msg": "Operation cancelled.",
            "type_cancel": "(Type ':q' to cancel)"
        },
        "main_menu": {
            "title": "📚 Library Management System",
            "opt_users": "[1] User Management (CRUD)",
            "opt_books": "[2] Book Catalog (CRUD)",
            "opt_loans": "[3] Loan & Return System",
            "opt_exit": "[4] Exit System"
        },
        "users": {
            "col_id": "ID",
            "col_fname": "First Name",
            "col_lname_p": "Paternal",
            "col_lname_m": "Maternal",
            "col_borrowed": "Borrowed",
            "title": "👤 User Management",
            "opt_add": "[1] Register New User",
            "opt_list": "[2] List All Users",
            "opt_update": "[3] Modify User",
            "opt_delete": "[4] Delete User",
            "opt_back": "[5] Back to Main Menu",
            "prompt_id": "Enter User ID: ",
            "prompt_fname": "Enter First Name: ",
            "prompt_lname_p": "Enter Paternal Last Name: ",
            "prompt_lname_m": "Enter Maternal Last Name: ",
            "prompt_update_id": "Enter User ID to modify: ",
            "prompt_delete_id": "Enter User ID to delete: ",
            "success_added": "User successfully registered!",
            "success_updated": "User successfully updated!",
            "success_deleted": "User successfully deleted!",
            "error_not_found": "Error: User not found.",
            "keep_current": " (Press Enter to keep: {})",
            "generated_id": "Auto-generated ID"
        },
        "books": {
            "col_id": "ID",
            "col_title": "Title",
            "col_author": "Author",
            "col_stock": "Stock",
            "col_status": "Status",
            "status_avail": "Available",
            "status_out": "Out of Stock",
            "title": "📚 Book Catalog",
            "opt_add": "[1] Register New Book",
            "opt_list": "[2] List All Books",
            "opt_update": "[3] Modify Book",
            "opt_delete": "[4] Delete Book",
            "opt_back": "[5] Back to Main Menu",
            "prompt_title": "Enter Book Title: ",
            "prompt_author": "Enter Author: ",
            "prompt_stock": "Enter Stock Quantity: ",
            "prompt_update_id": "Enter Book ID to modify: ",
            "prompt_delete_id": "Enter Book ID to delete: ",
            "success_added": "Book successfully registered!",
            "success_updated": "Book successfully updated!",
            "success_deleted": "Book successfully deleted!",
            "error_not_found": "Error: Book not found.",
            "error_invalid_int": "Error: Must be a valid whole number.",
            "generated_id": "Auto-generated ID",
            "keep_current": " (Press Enter to keep: {})"
        },
        "loans": {
            "title": "🤝 Loan & Return System",
            "opt_borrow": "[1] Borrow a Book",
            "opt_return": "[2] Return a Book",
            "opt_back": "[3] Back to Main Menu",
            "prompt_uid": "Enter User ID: ",
            "prompt_bid": "Enter Book ID: ",
            "err_max_books": "Error: User has reached the maximum limit of 3 books.",
            "err_no_stock": "Error: Book is currently out of stock.",
            "err_not_borrowed": "Error: This user has not borrowed this book.",
            "success_borrow": "Book successfully borrowed!",
            "success_return": "Book successfully returned!"
        }
    },
    "es": {
        "common": {
            "prompt_lang": "Select your language / Seleccione su idioma [en/es]",
            "prompt_choice": "Elija una opción:",
            "invalid_opt": "Opción no válida. Inténtelo de nuevo.",
            "press_enter": "Presione Enter para continuar...",
            "goodbye": "Apagando el sistema. ¡Adiós!",
            "error_empty": "Error: El campo no puede estar vacío.",
            "cancel_msg": "Operación cancelada.",
            "type_cancel": "(Escribe ':q' para cancelar)",
        },
        "main_menu": {
            "title": "📚 Sistema de Gestión Bibliotecaria",
            "opt_users": "[1] Gestión de Usuarios (CRUD)",
            "opt_books": "[2] Catálogo de Libros (CRUD)",
            "opt_loans": "[3] Sistema de Préstamos y Devoluciones",
            "opt_exit": "[4] Salir del Sistema"
        },
        "users": {
            "col_id": "ID",
            "col_fname": "Nombre(s)",
            "col_lname_p": "Paterno",
            "col_lname_m": "Materno",
            "col_borrowed": "Prestados",
            "title": "👤 Gestión de Usuarios",
            "opt_add": "[1] Registrar Nuevo Usuario",
            "opt_list": "[2] Consultar Usuarios",
            "opt_update": "[3] Modificar Usuario",
            "opt_delete": "[4] Eliminar Usuario",
            "opt_back": "[5] Volver al Menú Principal",
            "prompt_id": "Ingrese ID de Usuario: ",
            "prompt_fname": "Ingrese Nombre(s): ",
            "prompt_lname_p": "Ingrese Apellido Paterno: ",
            "prompt_lname_m": "Ingrese Apellido Materno: ",
            "prompt_update_id": "Ingrese ID del Usuario a modificar: ",
            "prompt_delete_id": "Ingrese ID del Usuario a eliminar: ",
            "success_added": "¡Usuario registrado con éxito!",
            "success_updated": "¡Usuario modificado con éxito!",
            "success_deleted": "¡Usuario eliminado con éxito!",
            "error_not_found": "Error: Usuario no encontrado.",
            "keep_current": " (Presione Enter para mantener: {})",
            "generated_id": "ID generado automáticamente"
        },
        "books": {
            "col_id": "ID",
            "col_title": "Título",
            "col_author": "Autor",
            "col_stock": "Stock",
            "col_status": "Estado",
            "status_avail": "Disponible",
            "status_out": "Agotado",
            "title": "📚 Catálogo de Libros",
            "opt_add": "[1] Registrar Nuevo Libro",
            "opt_list": "[2] Consultar Catálogo",
            "opt_update": "[3] Modificar Libro",
            "opt_delete": "[4] Eliminar Libro",
            "opt_back": "[5] Volver al Menú Principal",
            "prompt_title": "Ingrese el Título del Libro: ",
            "prompt_author": "Ingrese el Autor: ",
            "prompt_stock": "Ingrese la cantidad en Stock: ",
            "prompt_update_id": "Ingrese ID del Libro a modificar: ",
            "prompt_delete_id": "Ingrese ID del Libro a eliminar: ",
            "success_added": "¡Libro registrado con éxito!",
            "success_updated": "¡Libro modificado con éxito!",
            "success_deleted": "¡Libro eliminado con éxito!",
            "error_not_found": "Error: Libro no encontrado.",
            "error_invalid_int": "Error: Debe ser un número entero válido.",
            "generated_id": "ID generado automáticamente",
            "keep_current": " (Presione Enter para mantener: {})"
        },
        "loans": {
            "title": "🤝 Sistema de Préstamos y Devoluciones",
            "opt_borrow": "[1] Prestar un Libro",
            "opt_return": "[2] Devolver un Libro",
            "opt_back": "[3] Volver al Menú Principal",
            "prompt_uid": "Ingrese el ID del Usuario: ",
            "prompt_bid": "Ingrese el ID del Libro: ",
            "err_max_books": "Error: El usuario ha alcanzado el límite máximo de 3 libros.",
            "err_no_stock": "Error: El libro se encuentra agotado en este momento.",
            "err_not_borrowed": "Error: Este usuario no tiene prestado este libro.",
            "success_borrow": "¡Préstamo registrado con éxito!",
            "success_return": "¡Libro devuelto con éxito!"
        }
    }
}

# Default language state
current_lang = "es"


def set_language(lang_code: str):
    global current_lang
    if lang_code in translations:
        current_lang = lang_code


def t(view: str, key: str) -> str:
    lang_dict = translations.get(current_lang, translations["en"])
    view_dict = lang_dict.get(view, {})
    return view_dict.get(key, f"MISSING_{view.upper()}_{key.upper()}")