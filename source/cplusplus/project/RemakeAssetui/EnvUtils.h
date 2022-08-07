#ifndef ENVUTILS_H
#define ENVUTILS_H
#include <QString>
class EnvTools
{
public:
    EnvTools();
    QString GetQNtools();
    QString GetIcon(const char* path);
    bool FileExist(const char* path);
private:
    QString QNTools;
};
#endif // ENVUTILS_H
