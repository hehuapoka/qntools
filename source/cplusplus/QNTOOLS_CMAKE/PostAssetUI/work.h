#pragma once
#include <qthread.h>
#include <qstring.h>

class mywork :public QThread
{
	Q_OBJECT
signals:
	void tex_finished(int min, int max);
signals:
	void task_process();

public:
	explicit mywork(QObject *parent=0);
	~mywork();

	QString usd_path;
	QString asset_name;
	bool convert_tx = true;
private:
	QObject* _main_ptr;

protected:
	void run() override;


};