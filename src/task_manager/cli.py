from .services import add_task
from .storage import save_tasks, load_tasks
from .utils import validate_status



FILENAME = "data,json"


def run_cli():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Фильтр по статусу")
        print("4. Сортировка")
        print("5. Сохранить")
        print("0. Выход")

        choice = input()

        if choice == "1":
            title = input()
            tasks = add_task(tasks,title)