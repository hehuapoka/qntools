#pragma once
#pragma execution_character_set("utf-8")
#ifndef BOOST_ALL_DYN_LINK
#define BOOST_ALL_DYN_LINK
#endif
#include <boost/filesystem.hpp>
#include <string>
#include <vector>
#include <qstringlist.h>
#include <qstring>
void getFileList(const std::string& path,QStringList& m_file_list)
{
    if (!path.empty())
    {
        namespace fs = boost::filesystem;

        fs::path apk_path(path);

        for (auto& i:fs::directory_iterator(apk_path))
        {
            const fs::path cp = (i);
            if (fs::is_directory(cp))
                continue;
            if (cp.extension() == ".usd" || cp.extension() == ".usda" || cp.extension() == ".usdc")
                m_file_list.push_back(cp.string().c_str());
        }
    }
}


void getImgList(const std::string& path, QStringList& m_file_list)
{
    if (!path.empty())
    {
        namespace fs = boost::filesystem;

        fs::path apk_path(path);
        apk_path=apk_path / "Textures";

        if (!fs::exists(apk_path)) return;

        for (auto& i : fs::directory_iterator(apk_path))
        {
            const fs::path cp = (i);
            if (fs::is_directory(cp))
                continue;
            if (cp.extension() == ".tx")
                m_file_list.push_back(cp.string().c_str());
        }
    }
}