
# Modern To-Do List Application 📝

A sleek, modern, and draggable **To-Do List Application** built with Python and Tkinter. The app allows you to organize tasks efficiently with features like task addition, deletion, clearing, and auto-save functionality. It also includes a desktop widget mode for quick access to tasks.

---

## Features ✨

- **Minimalist Design**: Modern look and feel with a draggable and centered window.
- **Task Management**: Add, delete, and clear tasks with ease.
- **Auto-Save**: Automatically saves tasks, so your data persists between sessions.
- **Keyboard Shortcuts**: Press `Enter` to add tasks quickly.
- **Customizable Behavior**: Includes minimize and close buttons for easy window management.
- **Standalone Executable**: Converts into a `.exe` file for standalone use.

---

## Installation 🛠️

### Prerequisites
- Python 3.6 or later
- Required Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `pickle` (comes pre-installed with Python)

### Steps
1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/modern-todo-list.git
   cd modern-todo-list
   ```

2. Run the application directly:
   ```bash
   python todo_list.py
   ```

3. (Optional) To create an executable for Windows:
   - Install **PyInstaller**:
     ```bash
     pip install pyinstaller
     ```
   - Build the `.exe` file:
     ```bash
     pyinstaller --onefile --noconsole todo_list.py
     ```
   - The `.exe` file will be generated in the `dist` folder.

---

## How to Use 🖱️

1. Launch the application.
2. Enter a task in the input field and press the `Add Task` button (or hit `Enter`).
3. Select a task from the list to delete it using the `Delete Task` button.
4. Clear all tasks using the `Clear All` button.
5. Minimize or close the app using the corresponding buttons in the header.
6. Your tasks will be automatically saved and reloaded when you reopen the app.

---

## Screenshots 📸

### Main Interface
![image](https://github.com/user-attachments/assets/efc9fe4c-f5cf-46e6-9b06-05b8bebb44f3)


### Adding and Managing Tasks
![image](https://github.com/user-attachments/assets/b9cdd352-3e1f-43bb-a597-0c8c1be7244a)


---

## Future Enhancements 🚀

- Add support for recurring tasks and deadlines.
- Integration with cloud storage for syncing tasks across devices.
- A desktop widget that remains visible without opening the main application.

---

## Contributing 🤝

Contributions are welcome! If you have suggestions or find issues, feel free to:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Added new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## License 📄

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements 🙏

- Designed using **Tkinter**, Python’s standard GUI library.
- Inspired by the need for a simple and elegant task management tool.
