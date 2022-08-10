#include "singletask.h"
#include "EnvUtils.h"
#include "widget.h"
#include <qprocess.h>
void SingleTask::run()
{
	QProcess p;
	p.start(EnvTools::GetMakeTx(), _cmd);
	p.waitForFinished(-1);
	QMetaObject::invokeMethod(static_cast<widget*>(_main_ptr), "updataProcessBar", Qt::QueuedConnection);
}