tasks = {
    "Полагодити дриль": "виконано",
    "Перевірити пилки": "очікує",
    "Оновити список інструментів": "в процесі"
}

def add_task(name, status):
    tasks[name] = status

def delete_task(name):
    if name in tasks:
        del tasks[name]

def update_task_status(name, status):
    if name in tasks:
        tasks[name] = status

# Приклади змін
add_task("Замінити молоток", "очікує")
update_task_status("Оновити список інструментів", "виконано")
delete_task("Перевірити пилки")

print("Поточні задачі:")
print(tasks)

waiting_tasks = [name for name, status in tasks.items() if status == "очікує"]
print(" Задачі зі статусом 'очікує':")
print(waiting_tasks)
