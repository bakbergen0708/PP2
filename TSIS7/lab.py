import tkinter as tk
from PIL import Image, ImageTk

# Описание:
# Этот код создает пользовательский курсор в окне Tkinter. Он заменяет стандартный курсор мыши на изображение,
# устанавливает пользовательский курсор, чтобы он следовал за движениями мыши по окну, и изменяет цвет курсора при клике.

class CustomCursorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Cursor App")

        # Загрузка изображения пользовательского курсора
        self.cursor_image = Image.open("TSIS7/custom_cursor.png")
        self.cursor = ImageTk.PhotoImage(self.cursor_image)

        # Создание метки для отображения пользовательского курсора
        self.cursor_label = tk.Label(self.root, image=self.cursor, bg='yellow')
        self.cursor_label.pack()

        # Привязка движения мыши к методу motion
        self.root.bind('<Motion>', self.motion)

        # Привязка клика мыши к методу click
        self.root.bind('<Button-1>', self.click)

    def motion(self, event):
        # Перемещение метки пользовательского курсора в позицию мыши
        self.cursor_label.place(x=event.x, y=event.y)

    def click(self, event):
        # Изменение цвета курсора при клике
        # Для демонстрации давайте инвертируем цвета изображения курсора
        inverted_image = Image.eval(self.cursor_image, lambda x: 255 - x)
        self.cursor = ImageTk.PhotoImage(inverted_image)
        self.cursor_label.config(image=self.cursor)

# Создание главного окна
root = tk.Tk()
app = CustomCursorApp(root)

# Запуск приложения
root.mainloop()