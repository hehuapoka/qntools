#pragma once

#include <QWidget>
#include <qpushbutton.h>
#include <QVBoxLayout>
#include <qcombobox.h>
QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class widget : public QWidget
{
	Q_OBJECT

public:
	explicit widget(QWidget* parent = nullptr);
	~widget()
	{

	}
private:
	void init();
	Ui::Widget* ui;
};
