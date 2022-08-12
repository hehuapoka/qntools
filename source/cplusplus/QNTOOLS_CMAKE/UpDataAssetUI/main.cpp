// QNTOOLS_CMAKE.cpp: 定义应用程序的入口点。
#include <qapplication.h>
#include "widget.h"
using namespace std;

int main(int argc,char** argv)
{
	QApplication app(argc, argv);
	widget* win;
	win = new widget();
	win->show();
	return app.exec();
}
