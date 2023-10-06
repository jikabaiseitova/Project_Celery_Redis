from backend.my_app.tasks import my_task

result = my_task.delay(4, 6)
result_value = result.get()

