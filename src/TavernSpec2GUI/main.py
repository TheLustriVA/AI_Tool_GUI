from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QFormLayout, QListWidget, QInputDialog, QFileDialog
from PyQt5.QtCore import Qt
from PIL import Image
from stegano import lsb
import json
import sys

# Initialize PyQt5 application
app = QApplication(sys.argv)

# Create widgets
name_edit = QLineEdit()
first_mes_edit = QTextEdit()
scenario_edit = QTextEdit()
description_edit = QTextEdit()
personality_edit = QTextEdit()
mes_example_edit = QTextEdit()
creator_notes_edit = QTextEdit()
system_prompt_edit = QTextEdit()
post_history_instructions_edit = QTextEdit()
alternate_greetings_edit = QListWidget()
tags_edit = QListWidget()
creator_edit = QLineEdit()
character_version_edit = QLineEdit()
extensions_edit = QTextEdit()
clear_button = QPushButton("Clear")
save_button = QPushButton("Save JSON")

# Create layout and add widgets
layout = QVBoxLayout()
form_layout = QFormLayout()
form_layout.addRow("Name:", name_edit)
form_layout.addRow("First Message:", first_mes_edit)
form_layout.addRow("Scenario:", scenario_edit)
form_layout.addRow("Description:", description_edit)
form_layout.addRow("Personality:", personality_edit)
form_layout.addRow("Message Example:", mes_example_edit)
form_layout.addRow("Creator Notes:", creator_notes_edit)
form_layout.addRow("System Prompt:", system_prompt_edit)
form_layout.addRow("Post History Instructions:", post_history_instructions_edit)
form_layout.addRow("Alternate Greetings:", alternate_greetings_edit)
form_layout.addRow("Tags:", tags_edit)
form_layout.addRow("Creator:", creator_edit)
form_layout.addRow("Character Version:", character_version_edit)
form_layout.addRow("Extensions:", extensions_edit)
layout.addLayout(form_layout)
layout.addWidget(clear_button)
layout.addWidget(save_button)

# Create main window
main_win = QWidget()
main_win.setLayout(layout)

def create_placeholder_image():
    img = Image.new('RGB', (300, 300), color='white')
    return img

def embed_json_in_image(json_data, image):
    secret_img = lsb.hide(image, json.dumps(json_data))
    return secret_img


# Event handling for "Clear" button
def clear():
    name_edit.clear()
    first_mes_edit.clear()
    scenario_edit.clear()
    description_edit.clear()
    personality_edit.clear()
    mes_example_edit.clear()
    creator_notes_edit.clear()
    system_prompt_edit.clear()
    post_history_instructions_edit.clear()
    alternate_greetings_edit.clear()
    tags_edit.clear()
    creator_edit.clear()
    character_version_edit.clear()
    extensions_edit.clear()

# Event handling for "Save JSON" button
def save_json():
    data = {
        "spec": "chara_card_v2",
        "spec_version": "2.0",
        "data": {
            "name": name_edit.text(),
            "first_mes": first_mes_edit.text(),
            "scenario": scenario_edit.text(),
            "description": description_edit.toPlainText(),
            "personality": personality_edit.text(),
            "mes_example": mes_example_edit.toPlainText(),
            "creator_notes": creator_notes_edit.text(),
            "system_prompt": system_prompt_edit.text(),
            "post_history_instructions": post_history_instructions_edit.text(),
            "alternate_greetings": [],  # You can populate this from the QListWidget
            "tags": [],  # You can populate this from the QListWidget
            "creator": creator_edit.text(),
            "character_version": character_version_edit.text(),
            "extensions": json.loads(extensions_edit.toPlainText())
        }
    }
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getSaveFileName(None, "Save JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
    if fileName:
        with open(fileName, 'w') as f:
            json.dump(data, f, indent=4)
    placeholder_img = create_placeholder_image()
    secret_img = embed_json_in_image(data, placeholder_img)
    secret_img.save("secret_image.png")

save_button.clicked.connect(save_json)

# Run application
main_win.show()
sys.exit(app.exec_())
