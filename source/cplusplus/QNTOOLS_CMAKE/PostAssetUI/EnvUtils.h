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
    static bool FileExist(const char* path);

};
#endif // ENVUTILS_H
