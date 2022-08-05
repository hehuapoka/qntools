#include "EnvUtils.h"
#include <cstdlib>
EnvUtils::EnvUtils()
{
   char libvar[512];
   size_t requiredSize;

   getenv_s( &requiredSize, libvar, 0, "QNTools");
   if (requiredSize != 0)
   {
      printf("LIB doesn't exist!\n");
   }
}
const char* GetIcon(const char* Icon)
{

}
