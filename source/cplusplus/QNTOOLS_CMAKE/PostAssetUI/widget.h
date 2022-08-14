#pragma once

#include <QWidget>
#include <qstring.h>
#include <qsettings.h>
#include "work.h"
QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class widget : public QWidget
{
	Q_OBJECT

public:
	explicit widget(QWidget *parent = nullptr,QString path = "");
	~widget();
	QString usd_path;

private:
	Ui::Widget* ui;
	mywork* task;
	QSettings* qset;

public slots:
	void clickButton();
public slots:
	void resetProcessBar(int min, int max);
public slots:
	void updataProcessBar();
public slots:
	void changeUsdPath(QString value);
public:
	void modifyUsdPath();

protected:
	bool eventFilter(QObject* obj, QEvent* event);
};
