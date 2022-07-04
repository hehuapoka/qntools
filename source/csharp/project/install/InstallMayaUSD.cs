using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public static class InstallMayaUSD
{
    public static void Set()
    {
        DupMod();
    }
    public static void DupMod()
    {
        string a = @"D:\hehua\dev\QNTools";//Path.GetFullPath(Directory.GetCurrentDirectory());

        string b = Path.Combine(a, @"libs\Maya\templete");
        string usd = Path.Combine(a, @"libs\USD");
        string maya = Path.Combine(a, @"libs\Maya");
        if (Directory.Exists(b))
        {
            foreach(string s in Directory.GetFiles(b))
            {
                string dest_file = Path.Combine(maya, Path.GetFileName(s));
                File.Copy(s,dest_file , true);
                ModifyMod(dest_file, usd.Replace("\\", "/"), maya.Replace("\\", "/"));
            }
        }
    }
    public static void ModifyMod(string src,string usd,string maya)
    {
        try
        {
           string d = File.ReadAllText(src, Encoding.UTF8);
           d = d.Replace("%USD%", usd).Replace("%MAYA%",maya);
           File.WriteAllText(src, d);
        }
        catch(Exception e)
        {
            Console.WriteLine($"不能打开文件{e.Message}");
        }
        
    }
    public static void ModifyMayaEnv()
    {
        string temp_Dir =Path.GetTempPath();
        string maya_env = Path.Combine(temp_Dir, @"maya\2022\Maya.env");
        if(File.Exists(maya_env))
        {

        }
        else
        {
            //File.WriteAllText($"\nMAYA_TEMPLETE_PATH\n");
        }
    }
}