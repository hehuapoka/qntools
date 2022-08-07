#include "widget.h"
//#include <fstream>
//#include <sstream>
//#include <string>
#include <QApplication>
#include <QtDebug>
int main(int argc, char *argv[])
{
//    std::ifstream styleio("style.css");
//    std::string style_str;
//    if(styleio.is_open())
//    {
//        std::stringstream style_stream;
//        style_stream<<styleio.rdbuf();
//        style_str=style_stream.str();
//    }
    QApplication a(argc, argv);
    Widget w;
    if(argc > 1)
        w.usd_path=argv[1];
    //w.setStyleSheet(style_str.c_str());
    w.show();
    return a.exec();
}
