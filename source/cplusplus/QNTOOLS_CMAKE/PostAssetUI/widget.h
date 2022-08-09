#pragma once

#include <QWidget>
#include "work.h"
QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class widget : public QWidget
{
	Q_OBJECT

public:
	explicit widget(QWidget *parent = nullptr);
	~widget();

private:
	Ui::Widget* ui;
	mywork* task;
	QString usd_path;

private:
	void clickButton();
	void resetProcessBar(int min, int max);
	void updataProcessBar();
	void errorMessage(std::string message);
};
