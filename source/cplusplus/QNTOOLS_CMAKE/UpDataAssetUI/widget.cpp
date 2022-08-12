#pragma execution_character_set("utf-8")
#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif


#include "widget.h"
#include "ui_widget.h"
#include "tool.hpp"


widget::widget(QWidget* parent) :QWidget(parent), ui(new Ui::Widget)
{
	ui->setupUi(this);
	setWindowTitle(tr("提交资产"));
	resize(800, 600);

	init();
}

void widget::init()
{
	using namespace boost;
	//get all usd 


	QStringList m_file_list;
	getFileList("./", m_file_list);

	ui->usd->addItems(m_file_list);

	QStringList m_img_list;
	getImgList("./", m_img_list);

	ui->img->addItems(m_img_list);

	for (int a = 0; a < ui->img->count(); a++)
	{
		QListWidgetItem* c =  ui->img->item(a);
		c->setCheckState(Qt::CheckState::Checked);
	}

	for (int a = 0; a < ui->usd->count(); a++)
	{
		QListWidgetItem* c = ui->usd->item(a);
		c->setCheckState(Qt::CheckState::Checked);
	}
}