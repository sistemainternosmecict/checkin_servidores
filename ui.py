import sys
import threading
import socket
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from main import app, get_local_ip
from werkzeug.serving import make_server

class FlaskServerThread(threading.Thread):
    """Thread para rodar o servidor Flask em background."""
    def __init__(self, host, port=5000):
        super().__init__()
        self.host = host
        self.port = port
        self.server = None
        self.running = False

    def run(self):
        self.server = make_server(self.host, self.port, app)
        self.running = True
        self.server.serve_forever()

    def stop(self):
        if self.server:
            self.server.shutdown()
        self.running = False


class ServerControlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Servidor de Checkin")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label_status = QLabel("Servidor parado")
        self.label_status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_status)

        self.label_ip = QLabel("")
        self.label_ip.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_ip)

        self.button_toggle = QPushButton("Iniciar Servidor")
        self.button_toggle.clicked.connect(self.toggle_server)
        layout.addWidget(self.button_toggle)

        self.setLayout(layout)

        self.flask_thread = None
        self.host_ip = get_local_ip()
        self.port = 5000

    def toggle_server(self):
        if self.flask_thread and self.flask_thread.running:
            self.stop_server()
        else:
            self.start_server()

    def start_server(self):
        self.flask_thread = FlaskServerThread(self.host_ip, self.port)
        self.flask_thread.start()
        self.label_status.setText("✅ Servidor em execução")
        self.label_ip.setText(f"Acesse em: http://{self.host_ip}:{self.port}")
        self.button_toggle.setText("Parar Servidor")

    def stop_server(self):
        if self.flask_thread:
            self.flask_thread.stop()
            self.flask_thread.join()
        self.label_status.setText("⛔ Servidor parado")
        self.label_ip.setText("")
        self.button_toggle.setText("Iniciar Servidor")


if __name__ == "__main__":
    app_ui = QApplication(sys.argv)
    window = ServerControlUI()
    window.show()
    sys.exit(app_ui.exec())
