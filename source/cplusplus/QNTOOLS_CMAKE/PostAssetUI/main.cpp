// CMakeProject.cpp: 定义应用程序的入口点。
//
#include <QApplication>
#include <QWidget>
#include "widget.h"
#include <qdebug.h>

using namespace std;

int main(int argc,char** argv)
{
	QApplication app(argc,argv);
	widget* win;
	if (argc > 1)
		win = new widget(nullptr, argv[1]);
	else
		win = new widget();
	win->show();
	return app.exec();
}
