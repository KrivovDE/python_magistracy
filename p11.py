import tkinter as tk
from tkinter import ttk, messagebox
import json
import requests


class GitHubRepoInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Information")
        self.root.geometry("600x400")

        # Список репозиториев из статьи
        self.repositories = [
            {"name": "kubernetes", "full_name": "kubernetes/kubernetes"},
            {"name": "spark", "full_name": "apache/spark"},
            {"name": "vscode", "full_name": "microsoft/vscode"},
            {"name": "nixpkgs", "full_name": "NixOS/nixpkgs"}
        ]

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = ttk.Label(self.root, text="GitHub Repository Information",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        # Информация о задании
        info_text = ("По последней цифре зачетки (4) выбран репозиторий: KUBERNETES\n"
                     "Введите 'kubernetes' в поле ниже для получения информации")
        info_label = ttk.Label(self.root, text=info_text, justify="center")
        info_label.pack(pady=10)

        # Поле ввода
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20)

        ttk.Label(input_frame, text="Имя репозитория:").grid(row=0, column=0, padx=5)
        self.repo_entry = ttk.Entry(input_frame, width=30)
        self.repo_entry.grid(row=0, column=1, padx=5)
        self.repo_entry.insert(0, "kubernetes")

        # Кнопка
        self.get_button = ttk.Button(input_frame, text="Получить информацию",
                                     command=self.get_repo_info)
        self.get_button.grid(row=0, column=2, padx=10)

        # Поле для вывода
        output_frame = ttk.LabelFrame(self.root, text="Результат", padding=10)
        output_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.result_text = tk.Text(output_frame, height=10, wrap="word")
        self.result_text.pack(fill="both", expand=True)

        # Добавляем скроллбар
        scrollbar = ttk.Scrollbar(self.result_text)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip().lower()

        if repo_name != "kubernetes":
            messagebox.showwarning("Предупреждение",
                                   "По вашему варианту (цифра 4) доступен только репозиторий 'kubernetes'")
            self.repo_entry.delete(0, tk.END)
            self.repo_entry.insert(0, "kubernetes")
            return

        try:
            # Получаем информацию о пользователе Kubernetes с GitHub API
            url = "https://api.github.com/users/kubernetes"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Формируем данные в нужном формате
                result_data = {
                    'company': data.get('company'),
                    'created_at': data.get('created_at'),
                    'email': data.get('email'),
                    'id': data.get('id'),
                    'name': data.get('name'),
                    'url': data.get('url')
                }

                # Выводим в текстовое поле
                self.result_text.delete(1.0, tk.END)
                formatted_json = json.dumps(result_data, indent=2, ensure_ascii=False)
                self.result_text.insert(1.0, formatted_json)

                # Сохраняем в файл
                self.save_to_file(result_data)

                messagebox.showinfo("Успех",
                                    f"Информация успешно получена и сохранена в файл 'github_repositories.json'")
            else:
                messagebox.showerror("Ошибка",
                                     f"Не удалось получить данные. Код ошибки: {response.status_code}")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def save_to_file(self, data):
        """Сохраняет данные в JSON файл"""
        try:
            with open('github_repositories.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить файл: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GitHubRepoInfoApp(root)
    root.mainloop()