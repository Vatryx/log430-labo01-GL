"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from views.app_view import AppView
if __name__ == '__main__':
    app_view = AppView()
    app_view.execute_app()
