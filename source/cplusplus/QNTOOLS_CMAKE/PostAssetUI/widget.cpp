#pragma execution_character_set("utf-8")
#include "widget.h"
#include "ui_widget.h"
#include "EnvUtils.h"
#include <qdebug.h>
static QStringList AssetType{ "Element","Chars","Props","Sets" };

widget::widget(QWidget *parent):QWidget(parent), ui(new Ui::Widget)
{
	usd_path = "D:/test/test2/maya3.usda";

	ui->setupUi(this);
	this->setWindowTitle(tr("资产打包"));

	ui->progressBar->setMinimum(0);
	ui->progressBar->setMaximum(100);
	ui->progressBar->setValue(0);



	task = new mywork(this);
	QObject::connect(ui->pushButton, &QPushButton::clicked, this, &widget::clickButton);

	//QObject::connect(task, &mywork::tex_finished, this, &widget::resetProcessBar);
	QObject::connect(task, &mywork::task_process, this, &widget::updataProcessBar);
	QObject::connect(task, &mywork::finished, this, [=]() {ui->pushButton->setEnabled(true); });


}

widget::~widget()
{
}


void widget::clickButton()
{
	if (ui->lineEdit->text().isEmpty()) return;
	if (!EnvTools::FileExist(usd_path.toStdString().c_str())) return;
	QString asset_type = AssetType[ui->comboBox->currentIndex()];

	task->asset_name = asset_type + "_" + ui->lineEdit->text();
	task->usd_path = usd_path;
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
	ui->progressBar->setValue(ui->progressBar->value() + 1);
	//qDebug() << "a";
}