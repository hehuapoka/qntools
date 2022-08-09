#include "work.h"
#include "EnvUtils.h"
#include <qdebug.h>
#include <qprocess.h>
#include "assetprocess.hpp"
mywork::mywork(QObject* parent):QThread(parent)
{
}

mywork::~mywork()
{
}

void mywork::run()
{
	std::map<std::string,std::string> images;
	GetAssetTexture_DLL(usd_path.toStdString().c_str(), images);
	//bool ok = GetAssetTexture_DLL(usd_path.toStdString().c_str(), images);
	emit tex_finished(0, images.size() + 1);
	for (auto& a : images)
	{
		QStringList parms;
		parms  << EnvTools::GetTexInPath(a.first) << "-u" << "-v" << "--compression" << "DWAA:100"
			<< "--colorconfig" << EnvTools::GetACESConfig()
			<< "--colorconvert" << a.second.c_str() << "ACES - ACEScg"
			<< "--oiio"
			<< "-o" << EnvTools::GetTxOutPath(usd_path.toStdString().c_str(), a.first, asset_name.toStdString());
		QProcess p;
		p.start(EnvTools::GetMakeTx(), parms);
		p.waitForFinished();
		if (p.exitStatus() == QProcess::ExitStatus::CrashExit)
		{
			emit task_exit(a.first + "\n");
		}
		//qDebug() << parms;
		//qDebug() << parms;
		//QThread::sleep(0.1);
		emit task_process();
	}
}