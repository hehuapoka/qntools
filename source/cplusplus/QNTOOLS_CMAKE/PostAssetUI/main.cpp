// CMakeProject.cpp: 定义应用程序的入口点。
//
#include <QApplication>
#include <QWidget>
#include "widget.h"

using namespace std;

int main(int argc,char** argv)
{
	QApplication app(argc,argv);

	widget win;;
	win.show();
	return app.exec();
}
