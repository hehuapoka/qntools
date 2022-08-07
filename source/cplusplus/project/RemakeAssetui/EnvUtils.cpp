#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif

#include "EnvUtils.h"
#include <QtCore>
#include <QtDebug>
#include <string>
#include <boost/filesystem.hpp>

EnvTools::EnvTools()
{
    QNTools = qEnvironmentVariable("QNTools");
}

QString EnvTools::GetQNtools()
{
    return QNTools;
}
QString EnvTools::GetIcon(const char* path)
{
    boost::filesystem::path pa = boost::filesystem::path(QNTools.toStdString()) /"icon"/ path;
    return pa.string().c_str();
}


bool EnvTools::FileExist(const char* path)
{
    if(boost::filesystem::exists(path))
        return true;
    return false;
}
