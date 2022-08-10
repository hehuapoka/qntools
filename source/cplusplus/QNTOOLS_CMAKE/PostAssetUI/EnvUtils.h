#ifndef ENVUTILS_H
#define ENVUTILS_H
#include <QString>
class EnvTools
{
public:
    static QString GetQNtools();
    static QString GetIcon(const char* path);
    static QString GetMakeTx();
    static QString GetACESConfig();
    static QString GetTxOutPath(const std::string& src,const std::string& dest, const std::string asset_name);
    static QString GetTexInPath(const std::string& src);
    static bool FileExist(const char* path);
    static void CreateDirs(const std::string& usd_path, const std::string& asset_name);

};
#endif // ENVUTILS_H
