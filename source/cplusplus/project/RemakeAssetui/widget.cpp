#include "widget.h"
#include "./ui_widget.h"
#include <QDebug>
#include <QFileDialog>
#include <QMessageBox>
#pragma execution_character_set("utf-8")


Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget),env(new EnvTools())
{
    this->setWindowIcon(QIcon(env->GetIcon("elem.png")));
    ui->setupUi(this);
    ui->progressBar->setAlignment(Qt::AlignCenter);
    this->setMinimumSize(400,200);


    QObject::connect(ui->pushButton,&QPushButton::clicked,this,&Widget::PrintQNTools);
}

Widget::~Widget()
{
    delete ui;
    delete env;
}

void Widget::PrintQNTools()
{
    std::string asset_name = ui->lineEdit->text().toStdString();
    if(asset_name.empty())
    {
        QMessageBox::warning(this,tr("警告!"),tr("请为资产设置一个名称"));
        return;
    }

    if(!env->FileExist(usd_path.toStdString().c_str()))
        usd_path = QFileDialog::getOpenFileName(this,tr("选择USD文件"),"C:/","USD (*.usd *.usda *.usdc)");
    if(!env->FileExist(usd_path.toStdString().c_str()))
        return;


    images.clear();

    bool ok=GetAssetTexture_DLL(usd_path.toStdString().c_str(),images);
    qDebug() << ok;
    if(ok)
    {
        ui->progressBar->setMinimum(0);
        ui->progressBar->setMaximum(images.size()+1);
        ui->progressBar->setValue(0);
        ui->pushButton->setDisabled(true);

        PricessTexture * a = new PricessTexture(PricessTextureTaskType::TEX,asset_name,usd_path.toStdString(),&images,this);
        QObject::connect(a,&PricessTexture::done,this,&Widget::FinishedTexture);
        QObject::connect(a,&PricessTexture::finished,this,[=](){a->deleteLater();ui->pushButton->setEnabled(true);});
        a->start();

    }


}

void Widget::FinishedTexture(int num)
{
    //QMessageBox::information(this,tr("提示!"),tr("任务已经完成"));
    //ui->pushButton->setDisabled(true);
    ui->progressBar->setValue(num);
}
