#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif

#include "EnvUtils.h"
#include <QtCore>
#include <QtDebug>
#include <string>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>



QString EnvTools::GetQNtools()
{
    return qEnvironmentVariable("QNTools");
}
QString EnvTools::GetIcon(const char* path)
{
    std::string pa = (boost::filesystem::path(GetQNtools().toStdString()) /"icon"/ path).string();
    boost::replace_all(pa, "\\", "/");
    return pa.c_str();
}

QString EnvTools::GetACESConfig()
{
    std::string pa = (boost::filesystem::path(GetQNtools().toStdString()) / "config/aces_1.2/config.ocio").string();
    boost::replace_all(pa, "\\", "/");
    return pa.c_str();
}

QString EnvTools::GetMakeTx()
{
    std::string pa = (boost::filesystem::path(GetQNtools().toStdString()) / "libs/OIIO/maketx.exe").string();
    boost::replace_all(pa, "\\", "/");
    return pa.c_str();
}

QString EnvTools::GetTxOutPath(const std::string& src, const std::string& dest , const std::string asset_name)
{
    std::string pa = (boost::filesystem::path(src).parent_path() / asset_name / "Textures" / boost::filesystem::path(dest).filename().replace_extension("tx")).string();

    boost::replace_all(pa, "\\", "/");
    return pa.c_str();
}

QString EnvTools::GetTexInPath(const std::string& src)
{
    std::string pa = src;

    boost::replace_all(pa, "\\", "/");
    return pa.c_str();
}



bool EnvTools::FileExist(const char* path)
{
    if(boost::filesystem::exists(path))
        return true;
    return false;
}

void EnvTools::CreateDirs(const std::string& usd_path, const std::string& asset_name)
{
    boost::filesystem::path a = boost::filesystem::path(usd_path).parent_path() / asset_name / "Textures";
    if (!boost::filesystem::exists(a))
        
        boost::filesystem::create_directories(a);
}
