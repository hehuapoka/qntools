#pragma execution_character_set("utf-8")
#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif
#include "widget.h"
#include "ui_widget.h"
#include "EnvUtils.h"
#include <qdebug.h>
#include <qevent.h>
#include <qmessagebox.h>
#include <qfiledialog.h>
#include <boost/filesystem.hpp>
static QStringList AssetType{ "Elements","Chars","Props","Sets" };

widget::widget(QWidget *parent, QString path):QWidget(parent), ui(new Ui::Widget),usd_path(path),qset(new QSettings("./Setting.ini", QSettings::IniFormat))
{
	//usd_path = "D:/test/test2/maya3.usda";

	ui->setupUi(this);
	ui->progressBar->setAlignment(Qt::AlignCenter);
	ui->lineEdit_2->setText(usd_path);
	this->setWindowTitle(tr("资产打包"));

	ui->lineEdit_2->installEventFilter(this);

	ui->progressBar->setMinimum(0);
	ui->progressBar->setMaximum(100);
	ui->progressBar->setValue(0);



	task = new mywork(this);
	QObject::connect(ui->lineEdit_2, &QLineEdit::textChanged, this, &widget::changeUsdPath);
	QObject::connect(ui->pushButton, &QPushButton::clicked, this, &widget::clickButton);

	QObject::connect(task, &mywork::tex_finished, this, &widget::resetProcessBar);
	QObject::connect(task, &mywork::task_process, this, &widget::updataProcessBar);
	QObject::connect(task, &mywork::finished, this, [=]() {ui->pushButton->setEnabled(true); });


}

widget::~widget()
{
}

void widget::changeUsdPath(QString value)
{
	usd_path = ui->lineEdit_2->text();
}

void widget::clickButton()
{
	if (!boost::filesystem::exists(usd_path.toStdString()))
	{
		QMessageBox::warning(this, tr("错误"), tr("请选择一个USD文件"));
		return;
	}
		
	if (ui->lineEdit->text().isEmpty()) return;
	if (!EnvTools::FileExist(usd_path.toStdString().c_str())) return;
	QString asset_type = AssetType[ui->comboBox->currentIndex()];

	task->asset_name = asset_type + "_" + ui->lineEdit->text();
	task->usd_path = usd_path;
	task->convert_tx = ui->checkBox->checkState() == Qt::Checked;
	ui->pushButton->setDisabled(true);
	task->start();
}

void widget::resetProcessBar(int min, int max)
{
	ui->progressBar->setMinimum(min);
	ui->progressBar->setMaximum(max);
	ui->progressBar->setValue(0);
}
void widget::updataProcessBar()
{
	int current = ui->progressBar->value();
	ui->progressBar->setValue(current + 1);
	ui->number->setText(QString(" %1 / %2").arg(current).arg(ui->progressBar->maximum()));
	//qDebug() << "a";
}

bool widget::eventFilter(QObject* obj, QEvent* event)
{
	if (obj == ui->lineEdit_2) {
		if (event->type() == QEvent::MouseButtonDblClick) {
			modifyUsdPath();
			return true;
		}
		else {
			return false;
		}
	}
	else {
		// pass the event on to the parent class
		return QWidget::eventFilter(obj, event);
	}
}

void widget::modifyUsdPath()
{
	QString lastPath = qset->value("LastFilePath").toString();
	QString pf=QFileDialog::getOpenFileName(this, tr("选择USD文件"), lastPath, tr("USD File (*.usd)"));
	if (pf.isEmpty())
		return;
	if (!EnvTools::FileExist(pf.toStdString().c_str()))
		return;

	ui->lineEdit_2->setText(pf);
	changeUsdPath(pf);
}