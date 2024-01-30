import requests
import asyncio

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThreadPool, QRunnable
import sys


class MyRunnable(QRunnable):
    def __init__(self, async_function):
        super().__init__()
        self.async_function = async_function

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_function())


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def create_text(self, name, text, font, alignment, layout):
        name = QtWidgets.QLabel()
        name.setText(text)
        name.setFont(font)
        name.setAlignment(alignment)
        layout.addWidget(name)
        return name

    def create_button(self, name, text, font, layout, stretch, connect_to):
        name = QPushButton()
        name.setText(text)
        name.setFont(font)
        layout.addWidget(name, stretch)
        name.setCheckable(True)
        name.clicked.connect(connect_to)
        return name

    def create_line_edit(self, name, layout, stretch):
        name = QtWidgets.QLineEdit()
        layout.addWidget(name, stretch)
        return name

    def hide_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.takeAt(i)
            if item.widget():
                item.widget().hide()

    def initUI(self):
        sites = {}

        def get_user_input():
            def isnum(text):
                try:
                    float(text)
                except:
                    return True

            if len(line_edit_link.text()) < 1 or len(line_edit_timeout.text()) < 1:
                error.setText('Пустое поле. Введите ссылку и таймаут.')
            if isnum(line_edit_timeout.text()):
                error.setText('Введите число (цифрами).')
                return None
            if int(line_edit_timeout.text()) < 0:
                error.setText('Число слишком маленькое!')
            else:
                print(int(line_edit_timeout.text()))
                error.setText('')
                txt = additional_text.text()
                url = line_edit_link.text()
                txt += f'{url}\n'
                timeout = int(line_edit_timeout.text())
                sites[url] = timeout
                line_edit_link.clear()
                line_edit_timeout.clear()
                additional_text.setText(txt)

        def start_async_process():

            if len(sites) < 1:
                error.setText('Вы не указали ни одной ссылки')
            else:
                error.setText('')
                additional_text.setText('')

                global RUNNING
                RUNNING = True

                global outputs
                outputs = []

                global button_stop
                button_stop = self.create_button('button_stop', 'стоп', font12, VLayout, 0, stop)
                site_urls = list(sites.keys())

                for i in range(len(sites)):
                    globals()[f'output_{i}'] = self.create_text(
                        f'output_{i}', f'Ожидание ответа от {site_urls[i]}', font11, Qt.AlignLeft, VLayout2
                                                )
                    outputs.append(globals()[f'output_{i}'])

                QThreadPool.globalInstance().start(MyRunnable(main))

        async def check(url, txtobj):
            main_text.setText('\nПроверка доступности сайтов.\n')
            try:
                info = requests.get(url)
                if info.status_code >= 200 and info.status_code < 300:
                    txt = f'Сайт {url} доступен'
                    txtobj.setText(txt)
                else:
                    txt = f'Сайт {url} недоступен. (код ошибки: {info.status_code})'
                    txtobj.setText(txt)
            except:
                txt = f'Ошибка подключения к {url}'
                txtobj.setText(txt)

        async def cycle(url, timeout, txtobj):
            while RUNNING == 1:
                await check(url, txtobj)
                await asyncio.sleep(timeout)

        async def main():
            self.hide_layout(HLayout2)
            self.hide_layout(HLayout3)
            tasks = []
            site_list = list(sites.keys())
            for i in range(len(site_list)):
                timeout = sites.get(site_list[i])
                tasks.append(cycle(site_list[i], timeout, outputs[i]))
            await asyncio.gather(*tasks)

        def stop():
            global RUNNING
            RUNNING = False

            sites.clear()
            main_text.setText(start_text)
            additional_text.setText('\nЗдесь появятся url сайтов для проверки:\n')
            widgets = {line_edit_link: 3, line_edit_timeout: 1, button_next1: 1, button_check1: 1,
                       example_text1: None, example_text2: None}


            for widget in widgets:
                widget.show()
                if widgets[widget] != None:
                    HLayout2.addWidget(widget, widgets[widget])
                else:
                    HLayout3.addWidget(widget)
            button_stop.deleteLater()
            for i in outputs:
                i.deleteLater()

        self.setWindowTitle('проверка доступности сайтов')
        self.resize(900, 600)

        font12 = QFont()
        font12.setPointSize(12)
        font11 = QFont()
        font11.setPointSize(11)

        VLayout = QVBoxLayout()
        VLayout.setAlignment(Qt.AlignTop)
        self.setLayout(VLayout)

        HLayout1 = QHBoxLayout()
        HLayout2 = QHBoxLayout()
        HLayout3 = QHBoxLayout()
        VLayout2 = QVBoxLayout()


        start_text = (
            '\nЗдравствуйте! Эта программа проверит доступны ли нужные вам сайты. \n'
            'Просто вставьте ссылку на сайт в одно поле ввода и время ожидания отклика — в другое.\n'
            'Нажмите на кнопку "добавить", чтобы внести сайт в список для проверки.\n'
            'После можно будет добавить больше ссылок. Кнопка "проверка", запускает процесс.\n'
        )
        main_text = self.create_text('main_text', start_text, font12, Qt.AlignCenter, HLayout1)
        VLayout.addLayout(HLayout1)

        line_edit_link = self.create_line_edit('line_edit_link', HLayout2, 3)
        line_edit_timeout = self.create_line_edit('line_edit_timeout', HLayout2, 1)
        button_next1 = self.create_button('button_next1', 'добавить', font12, HLayout2, 1, get_user_input)
        button_check1 = self.create_button('button_check1', 'проверка', font12, HLayout2, 1, start_async_process)
        VLayout.addLayout(HLayout2)

        example_text1 = self.create_text('example_text1', 'например: https://google.com',
                                         font11, Qt.AlignLeft, HLayout3)
        example_text2 = self.create_text('example_text2', 'в секундах',
                                         font11, Qt.AlignLeft, HLayout3)
        VLayout.addLayout(HLayout3)

        error = self.create_text('error', '', font11, Qt.AlignLeft, VLayout)
        additional_text = self.create_text(
            'additional_text', '\nЗдесь появятся url сайтов для проверки:\n', font11,
            Qt.AlignLeft, VLayout2
        )

        VLayout.addLayout(VLayout2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = Application()
    root.show()
    sys.exit(app.exec_())
