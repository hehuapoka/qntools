#pragma execution_character_set("utf-8")
#include "work.h"
#include "EnvUtils.h"
#include <qdebug.h>
#include <qthreadpool.h>
#include <qprocess.h>
#include "assetprocess.hpp"
#include "singletask.h"
mywork::mywork(QObject* parent):QThread(parent), _main_ptr(parent)
{
	
}

mywork::~mywork()
{
}

void mywork::run()
{
	std::map<std::string,std::string> images;
	if (convert_tx)
	{
		GetAssetTexture_DLL(usd_path.toStdString().c_str(), images);
		//bool ok = GetAssetTexture_DLL(usd_path.toStdString().c_str(), images);
		emit tex_finished(0, images.size() + 2);
		EnvTools::CreateDirs(usd_path.toStdString(), asset_name.toStdString());
		for (auto& a : images)
		{
			QStringList parms;
			parms << EnvTools::GetTexInPath(a.first) << "-u" << "-v" << "--compression" << "DWAA:100"
				<< "--colorconfig" << EnvTools::GetACESConfig()
				<< "--colorconvert" << a.second.c_str() << "ACES - ACEScg"
				<< "--oiio"
				<< "-o" << EnvTools::GetTxOutPath(usd_path.toStdString().c_str(), a.first, asset_name.toStdString());
			/*QProcess p;
			p.start(EnvTools::GetMakeTx(), parms);*/
			//p.waitForFinished();
			//emit task_process();
			SingleTask* s_task = new SingleTask(_main_ptr, parms);
			QThreadPool::globalInstance()->start(s_task);
		}
		QThreadPool::globalInstance()->setMaxThreadCount(6);
		QThreadPool::globalInstance()->waitForDone();
	}
	else
	{
		emit tex_finished(0, 1);
	}

	int ok = PostProcessAsset_DLL(usd_path.toStdString().c_str(), asset_name.toStdString().c_str());
	emit task_process();
}