from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QInputDialog, QTextEdit, QTabWidget, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("My PyQt5 App")

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://chat.openai.com"))

        # Create a QLineEdit for notes
        self.note_field = QTextEdit()
        self.note_field.setPlaceholderText("Enter your notes here...")

        # Create buttons
        self.add_todo_btn = QPushButton("Add To-Do")
        self.show_todo_btn = QPushButton("Show To-Do List")
        self.save_note_btn = QPushButton("Save Note")
        self.clear_note_btn = QPushButton("Clear Note")
        self.refresh_web_btn = QPushButton("Refresh Web View")
        self.url_field = QLineEdit()
        self.url_field.setPlaceholderText("Enter URL...")

        # To-Do List
        self.todo_list = QTextEdit()
        self.todo_list.setPlaceholderText("To-Do List...")

        # Tab Widget
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.web_view, "Web View")
        self.tab_widget.addTab(self.todo_list, "To-Do List")

        # Connect buttons to functions
        self.add_todo_btn.clicked.connect(self.add_todo)
        self.show_todo_btn.clicked.connect(self.show_todo)
        self.save_note_btn.clicked.connect(self.save_note)
        self.clear_note_btn.clicked.connect(self.clear_note)
        self.refresh_web_btn.clicked.connect(self.refresh_web)
        self.url_field.returnPressed.connect(self.load_url)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        layout.addWidget(self.note_field)
        layout.addWidget(self.add_todo_btn)
        layout.addWidget(self.show_todo_btn)
        layout.addWidget(self.save_note_btn)
        layout.addWidget(self.clear_note_btn)
        layout.addWidget(self.refresh_web_btn)
        layout.addWidget(self.url_field)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_todo(self):
        text, ok = QInputDialog.getText(self, "Add To-Do", "To-Do:")
        if ok:
            self.todo_list.append(text)

    def show_todo(self):
        self.tab_widget.setCurrentIndex(1)

    def save_note(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as f:
                f.write(self.note_field.toPlainText())

    def clear_note(self):
        self.note_field.clear()

    def refresh_web(self):
        self.web_view.reload()

    def load_url(self):
        url = self.url_field.text()
        self.web_view.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
