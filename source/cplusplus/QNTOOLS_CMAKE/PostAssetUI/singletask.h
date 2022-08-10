#pragma once
#include <qobject.h>
#include <QRunnable>
#include <qstring.h>
#include <qstringlist.h>
class SingleTask:public QRunnable
{
public:
	SingleTask(QObject* main_ptr,const QStringList& cmd):QRunnable(),_main_ptr(main_ptr), _cmd(cmd)
	{
		
	}
	~SingleTask()
	{

	}

	void run() override;

private:
	QStringList _cmd;
	QObject* _main_ptr;
};