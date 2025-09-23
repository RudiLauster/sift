import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QModelIndex, QPoint, QRect, Qt
from PyQt5.QtGui import (
    QColor,
    QFontMetrics,
    QIcon,
    QPainter,
    QStandardItem,
    QStandardItemModel,
)
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QAction,
    QApplication,
    QButtonGroup,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMenu,
    QPushButton,
    QStackedWidget,
    QStyle,
    QStyledItemDelegate,
    QToolButton,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

dbg_count = 0


def tryouts_1():
    class BarDelegate(QStyledItemDelegate):

        def initStyleOption(self, option, index):
            super().initStyleOption(option, index)

        def paint(self, painter, option, index):
            # self._print_state(option)

            dummy_index = QModelIndex()
            super().paint(painter, option, dummy_index)

            painter.save()
            # QApplication.style().drawControl(QStyle.CE_ItemViewItem, option, painter)

            value = index.data(Qt.DisplayRole)
            percent = float(value) if value else 0
            bar_margin = 2
            # bar_rect = QRect(
            #    option.rect.left() + bar_margin,
            #    option.rect.top() + option.rect.height() // 4,
            #    int((option.rect.width() - 2 * bar_margin) * (percent / 100.0)),
            #    option.rect.height() // 2,
            # )
            bar_rect = QRect(
                option.rect.left(),
                option.rect.top() + 1,
                int(option.rect.width() * (percent / 100.0)),
                option.rect.height() - 2,
            )
            painter.setRenderHint(QPainter.Antialiasing)
            painter.fillRect(bar_rect, QColor(100, 200, 250))
            painter.setPen(Qt.black)
            painter.drawText(option.rect, Qt.AlignVCenter, f"{int(percent)}%")

            # QApplication.style().drawPrimitive(QStyle.PE_PanelItemViewItem, hover_opt, painter)

            painter.restore()

            # if option.state & QStyle.State_MouseOver:
            #    painter.save()
            #    painter.setRenderHint(QPainter.Antialiasing)
            #    # hover_color = QColor("#cce8ff")
            #    hover_color = QColor("#ff0000")
            #    painter.fillRect(option.rect, hover_color)
            #    painter.restore()

            # Now draw hover effect on top if mouse-over
            # if option.state & QStyle.State_MouseOver:
            #    hover_opt = QStyleOptionViewItem(option)
            #    hover_opt.state |= QStyle.State_MouseOver
            #    QApplication.style().drawPrimitive(QStyle.PE_PanelItemViewItem, hover_opt, painter)

        def _print_state(self, option):
            global dbg_count
            dbg_count += 1
            print(f"----- ( {dbg_count} ) ---------------")
            for state_flag in self.descrs.keys():
                if option.state & state_flag:
                    print(f"state_flag: {self.descrs[state_flag]}")
            print(f"MouseOver? {int(option.state & QStyle.State_MouseOver)}")
            print(f"Text: {option.text}")

        descrs = {
            QStyle.State_None: "QStyle.State_None",
            QStyle.State_Active: "QStyle.State_Active",
            QStyle.State_AutoRaise: "QStyle.State_AutoRaise",
            QStyle.State_Children: "QStyle.State_Children",
            QStyle.State_DownArrow: "QStyle.State_DownArrow",
            QStyle.State_Editing: "QStyle.State_Editing",
            QStyle.State_Enabled: "QStyle.State_Enabled",
            QStyle.State_HasFocus: "QStyle.State_HasFocus",
            QStyle.State_Horizontal: "QStyle.State_Horizontal",
            QStyle.State_KeyboardFocusChange: "QStyle.State_KeyboardFocusChange",
            QStyle.State_MouseOver: "QStyle.State_MouseOver",
            QStyle.State_NoChange: "QStyle.State_NoChange",
            QStyle.State_Off: "QStyle.State_Off",
            QStyle.State_On: "QStyle.State_On",
            QStyle.State_Raised: "QStyle.State_Raised",
            QStyle.State_ReadOnly: "QStyle.State_ReadOnly",
            QStyle.State_Selected: "QStyle.State_Selected",
            QStyle.State_Item: "QStyle.State_Item",
            QStyle.State_Open: "QStyle.State_Open",
            QStyle.State_Sibling: "QStyle.State_Sibling",
            QStyle.State_Sunken: "QStyle.State_Sunken",
            QStyle.State_UpArrow: "QStyle.State_UpArrow",
            QStyle.State_Mini: "QStyle.State_Mini",
            QStyle.State_Small: "QStyle.State_Small",
        }

    class PersistentTooltip(QLabel):
        def __init__(self, parent=None):
            super().__init__(parent, Qt.ToolTip)
            self.setWindowFlags(Qt.ToolTip)
            self.setStyleSheet("background-color: #ffffdd; border: 1px solid black; padding: 3px;")
            self.hide()

        def show_tooltip(self, text, pos):
            self.setText(text)
            self.adjustSize()
            self.move(pos)
            self.show()

        def hide_tooltip(self):
            self.hide()

    class CustomHeaderView(QHeaderView):
        def __init__(self, orientation, parent=None):
            super().__init__(orientation, parent)
            self.column_limits: dict[int, tuple] = {}
            self.SEP_CLICK_TOL = 5

        def setColumnLimits(self, column, min_width, max_width):
            self.column_limits[column] = (min_width, max_width)

        def mouseDoubleClickEvent(self, event):
            if event.button() == Qt.LeftButton:
                col_index = self._get_separator_at_position(event.pos().x())
                if col_index >= 0:
                    self._process_col_resize(col_index)
                    return
            super().mouseDoubleClickEvent(event)

        def adjust_all_columns(self):
            for col_index in range(self.count()):
                self._process_col_resize(col_index)

        def _eval_width(self, logical_index, demanded_width):
            if logical_index in self.column_limits:
                min_width = self.column_limits[logical_index][0]
                max_width = self.column_limits[logical_index][1]
                if demanded_width < min_width:
                    return min_width
                elif max_width < demanded_width:
                    return max_width
                else:
                    return demanded_width
            return demanded_width

        def _process_col_resize(self, col_index):
            # Check if this column should resize to header text
            header_width = self._getHeaderTextWidth(col_index)
            # Calculate the ideal size for contents
            tree_view = self.parent()
            contents_width = tree_view.sizeHintForColumn(col_index)
            signif_width = max(header_width, contents_width)
            ideal_width = self._eval_width(col_index, signif_width)
            print(
                f"> {col_index}: header_width:{header_width} contents_width:{contents_width} ideal_width:{ideal_width} column_limits:{self.column_limits[col_index]}"
            )
            # Resize the section
            self.resizeSection(col_index, ideal_width)

        def _getHeaderTextWidth(self, logical_index):
            """Calculate the width needed for the header text"""
            if not self.model():
                return 0
            # Get the header text
            header_text = self.model().headerData(logical_index, self.orientation(), Qt.DisplayRole)
            if not header_text:
                return 0
            # Get font metrics for the header font
            font_metrics = QFontMetrics(self.font())
            # Calculate text width with some padding
            text_width = font_metrics.width(str(header_text))
            # Add padding for margins, sort indicators, etc.
            padding = 10  # Adjust this value as needed
            return text_width + padding

        def _get_separator_at_position(self, x_pos):
            for i in range(self.count()):
                section_end = self.sectionPosition(i) + self.sectionSize(i)

                # Check if click is within tolerance of separator
                if abs(x_pos - section_end) <= self.SEP_CLICK_TOL:
                    return i

            return -1

    class EnhancedTreeView(QTreeView):
        def __init__(self, model):
            super().__init__()

            self.setMouseTracking(True)
            self._last_index = None

            header = CustomHeaderView(Qt.Horizontal, self)
            self.setHeader(header)

            self.setModel(model)

            widths = [50, 80, 10000, 30]
            resizable_col = 1
            for col in range(4):
                col_size = header._getHeaderTextWidth(col)
                header.setColumnLimits(col, col_size, col_size + widths[col])
                if col != resizable_col:
                    header.setSectionResizeMode(col, header.Interactive)
                else:
                    header.setSectionResizeMode(col, header.Stretch)

            self.setHeaderHidden(False)
            header.setStretchLastSection(False)
            header.setSectionsClickable(True)

            header.setMinimumSectionSize(20)
            header.setMaximumSectionSize(200)

            self.tooltip = PersistentTooltip(self)

        def adjust_all_columns(self):
            self.header().adjust_all_columns()

        def mouseMoveEvent(self, event):
            index = self.indexAt(event.pos())

            if index != self._last_index:
                self._last_index = index
                if not index.isValid():
                    self.tooltip.hide_tooltip()
                    return

                text = str(index.data(Qt.DisplayRole))
                option = self.viewOptions()
                option.rect = self.visualRect(index)

                font_metrics = QFontMetrics(option.font)
                text_width = font_metrics.width(text)
                column_width = self.columnWidth(index.column())

                if text_width > column_width:
                    global_pos = self.viewport().mapToGlobal(event.pos() + QPoint(20, 20))
                    self.tooltip.show_tooltip(text, global_pos)
                else:
                    self.tooltip.hide_tooltip()

            super().mouseMoveEvent(event)

        def leaveEvent(self, event):
            self.tooltip.hide_tooltip()
            self._last_index = None
            super().leaveEvent(event)

    def setup_adaptiv_double_spinbox(window):
        from uwsift.ui.custom_widgets import QAdaptiveDoubleSpinBox

        layout = QVBoxLayout()
        spinbox = QAdaptiveDoubleSpinBox()
        spinbox.setRange(-1e6, 1e6)
        spinbox.setDecimals(10)
        spinbox.setValue(2.0)

        layout.addWidget(spinbox)
        window.setLayout(layout)

    def setup_layer_details_pane(window):
        from uwsift.ui.layer_details_widget_ui import Ui_LayerDetailsPane

        details_pane_ui = Ui_LayerDetailsPane()
        details_pane_ui.setupUi(window)

    def setup_layer_treeview(window):
        from uwsift.view.layer_tree_view import LayerTreeView

        dockWidgetContents = QWidget(window)
        dockWidgetContents.setObjectName("dockWidgetContents")
        horizontalLayout = QHBoxLayout(dockWidgetContents)
        layers_treeview_ui = LayerTreeView(dockWidgetContents)

        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        layers_treeview_ui = LayerTreeView(dockWidgetContents)
        layers_treeview_ui.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        layers_treeview_ui.setDragDropMode(QAbstractItemView.InternalMove)
        layers_treeview_ui.setAlternatingRowColors(True)
        layers_treeview_ui.setObjectName("treeView")
        verticalLayout.addWidget(layers_treeview_ui)
        horizontalLayout.addLayout(verticalLayout)

        window.setLayout(horizontalLayout)

    def setup_treeview_demo(window=None):
        # Create tree view and model
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Name", "Progress", "Comment", "last"])
        tree_view = EnhancedTreeView(model)

        parent_item = model.invisibleRootItem()

        # Add items with 3 columns
        item1 = QStandardItem("Task 1")
        progress1 = QStandardItem("25")
        comment1 = QStandardItem("Started")
        last1 = QStandardItem("The LC1")
        parent_item.appendRow([item1, progress1, comment1, last1])

        item2 = QStandardItem("Task 2 Task 2 Task 2 Task 2")
        progress2 = QStandardItem("80")
        comment2 = QStandardItem("Almost done")
        last2 = QStandardItem("The LC2")
        parent_item.appendRow([item2, progress2, comment2, last2])

        item3 = QStandardItem("Task 3")
        progress3 = QStandardItem("50")
        comment3 = QStandardItem("In progress")
        last3 = QStandardItem("The LC3")
        parent_item.appendRow([item3, progress3, comment3, last3])

        item4 = QStandardItem("Another loooong name")
        progress4 = QStandardItem("66")
        comment4 = QStandardItem("In progress, again.")
        last4 = QStandardItem("The LC4")
        parent_item.appendRow([item4, progress4, comment4, last4])

        tree_view.adjust_all_columns()

        tree_view.setItemDelegateForColumn(1, BarDelegate())

        tree_view.setAlternatingRowColors(True)

        return tree_view, model

    app = QApplication([])
    window = QWidget()
    main_layout = QVBoxLayout(window)

    # setup_adaptiv_double_spinbox(window)
    # setup_layer_details_pane(window)
    # setup_layer_treeview(window)
    tv, model = setup_treeview_demo(window)

    main_layout.addWidget(tv)

    input_layout = QHBoxLayout()

    text_input = QLineEdit()
    text_input.setMaxLength(200)  # max 200 characters
    text_input.setPlaceholderText("Enter item text (max 200 chars)")
    input_layout.addWidget(text_input)

    add_button = QPushButton("Add")

    def handle_add_button():
        text = text_input.text().strip()
        if text:
            item = QStandardItem(text)
            progress = QStandardItem(f"{len(text)}")
            comment = QStandardItem("In progress")
            last = QStandardItem("The LC3")
            parent_item = model.invisibleRootItem()
            parent_item.appendRow([item, progress, comment, last])
            # text_input.clear()

    add_button.clicked.connect(handle_add_button)

    input_layout.addWidget(add_button)

    main_layout.addLayout(input_layout)

    window.show()
    window.resize(600, 400)

    app.exec_()


def tryouts_2():

    class SegmentedDemo(QWidget):
        def __init__(self):
            super().__init__()

            # stack of pages
            self.stack = QStackedWidget()
            self.stack.addWidget(QLabel("View A 😎"))
            self.stack.addWidget(QLabel("View B 🚀"))

            # two buttons behaving like a segmented control
            btn_a = QPushButton("Show A")
            btn_b = QPushButton("Show B")
            for b in (btn_a, btn_b):
                b.setCheckable(True)
                b.setFlat(True)
                b.setStyleSheet(
                    """
                    QPushButton {
                        border: 1px solid #888;
                        padding: 6px 12px;
                    }
                    QPushButton:checked {
                        background-color: #4caf50;
                        color: white;
                    }
                """
                )

            group = QButtonGroup(self)
            group.setExclusive(True)
            group.addButton(btn_a, 0)
            group.addButton(btn_b, 1)
            group.buttonClicked[int].connect(self.stack.setCurrentIndex)

            btn_a.setChecked(True)  # default selection

            # layout
            btn_layout = QHBoxLayout()
            btn_layout.addWidget(btn_a)
            btn_layout.addWidget(btn_b)

            layout = QVBoxLayout()
            layout.addLayout(btn_layout)
            layout.addWidget(self.stack)
            self.setLayout(layout)

    app = QApplication(sys.argv)
    w = SegmentedDemo()
    w.show()
    sys.exit(app.exec_())


def tryouts_3():
    class StackedDemo(QWidget):
        def __init__(self):
            super().__init__()

            self.stack = QStackedWidget()
            self.stack.addWidget(QLabel("View A 😎"))
            self.stack.addWidget(QLabel("View B 🚀"))

            combo = QComboBox()
            combo.addItems(["Show A 😎", "Show B 🚀"])
            combo.currentIndexChanged.connect(self.stack.setCurrentIndex)

            layout = QVBoxLayout()
            layout.addWidget(combo)
            layout.addWidget(self.stack)
            self.setLayout(layout)

    app = QApplication(sys.argv)
    w = StackedDemo()
    w.show()
    sys.exit(app.exec_())


def tryouts_4():
    class ToolButtonDemo(QWidget):
        def __init__(self):
            super().__init__()

            self.label = QLabel("Nothing is happening…")
            self.label.setStyleSheet("font-size: 18px;")

            # Create a QToolButton
            self.toggle_btn = QToolButton()
            self.toggle_btn.setCheckable(True)
            self.toggle_btn.setToolTip("Toggle me!")
            self.toggle_btn.setIcon(QIcon.fromTheme("view-hidden"))  # use system icon
            self.toggle_btn.setIconSize(self.toggle_btn.iconSize() * 2)

            # Connect toggle signal
            self.toggle_btn.toggled.connect(self.on_toggle)

            # Layout
            layout = QVBoxLayout()
            layout.addWidget(self.toggle_btn)
            layout.addWidget(self.label)
            self.setLayout(layout)

        def on_toggle(self, checked):
            if checked:
                self.toggle_btn.setIcon(QIcon.fromTheme("view-visible"))  # icon changes when toggled
                self.label.setText("🔥 Button is ON! 🔥")
            else:
                self.toggle_btn.setIcon(QIcon.fromTheme("view-hidden"))
                self.label.setText("😴 Button is OFF 😴")

    app = QApplication(sys.argv)
    w = ToolButtonDemo()
    w.show()
    sys.exit(app.exec_())


def tryouts_5():
    class ToolButtonLabelDemo(QWidget):
        def __init__(self):
            super().__init__()

            # Create a checkable tool button
            self.toggle_btn = QToolButton()
            self.toggle_btn.setCheckable(True)
            self.toggle_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # icon + text
            self.toggle_btn.setIcon(QIcon.fromTheme("view-hidden"))
            self.toggle_btn.setText("😴 Off")  # initial text
            self.toggle_btn.setStyleSheet("font-size: 16px; padding: 6px;")
            self.toggle_btn.setIconSize(self.toggle_btn.iconSize() * 2)

            # Connect toggle signal
            self.toggle_btn.toggled.connect(self.on_toggle)

            layout = QVBoxLayout()
            layout.addWidget(self.toggle_btn)
            self.setLayout(layout)

        def on_toggle(self, checked):
            if checked:
                self.toggle_btn.setIcon(QIcon.fromTheme("view-visible"))
                self.toggle_btn.setText("🔥 On! 🔥")
            else:
                self.toggle_btn.setIcon(QIcon.fromTheme("view-hidden"))
                self.toggle_btn.setText("😴 Off")

    app = QApplication(sys.argv)
    w = ToolButtonLabelDemo()
    w.show()
    sys.exit(app.exec_())


def tryouts_6():
    class CustomToolButton(QToolButton):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setPopupMode(QToolButton.MenuButtonPopup)
            self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.last_action = None

        def update_default_action(self, action):
            """Promote the action to the default button view."""
            self.setDefaultAction(action)
            self.last_action = action
            self.setIcon(action.icon())
            self.setText(action.text())
            self.setToolTip(action.toolTip())

    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("QToolButton Last Action Demo")
            self.setGeometry(100, 100, 300, 200)

            layout = QVBoxLayout(self)

            self.button = CustomToolButton(self)
            layout.addWidget(self.button)

            # Create actions
            action1 = QAction(QIcon.fromTheme("document-open"), "Open File", self)
            action1.setToolTip("Open a file")
            action1.triggered.connect(lambda: self.action_triggered(action1))

            action2 = QAction(QIcon.fromTheme("document-save"), "Save File", self)
            action2.setToolTip("Save the current file")
            action2.triggered.connect(lambda: self.action_triggered(action2))

            action3 = QAction(QIcon.fromTheme("edit-copy"), "Copy File", self)
            action3.setToolTip("Copy the file")
            action3.triggered.connect(lambda: self.action_triggered(action3))

            # Create menu
            self.menu = QMenu(self)
            for act in [action1, action2, action3]:
                self.menu.addAction(act)

            self.button.setMenu(self.menu)
            self.button.update_default_action(action1)  # initial default

        def action_triggered(self, action):
            print(f"{action.text()} triggered")
            self.button.update_default_action(action)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# tryouts_1()
# tryouts_2()
tryouts_3()
# tryouts_4()
# tryouts_5()
# tryouts_6()
