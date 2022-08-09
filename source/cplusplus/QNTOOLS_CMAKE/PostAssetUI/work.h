#pragma once
#include <qthread.h>

class mywork :public QThread
{
	Q_OBJECT
signals:
	void tex_finished(int min, int max);
signals:
	void task_process();
signals:
	void task_exit(std::string);

public:
	explicit mywork(QObject *parent=0);
	~mywork();

	QString usd_path;
	QString asset_name;

protected:
	void run() override;


};