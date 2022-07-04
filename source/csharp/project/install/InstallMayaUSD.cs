using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

public static class InstallMayaUSD
{
    public static void Set()
    {
        Console.WriteLine("开始安装MayaUSD");
        DupMod();
        Console.WriteLine("MayaUSD安装完成");
    }
    public static void DupMod()
    {
        string a = Path.GetFullPath(Directory.GetCurrentDirectory());           //@"E:\Work\dev\qntools";

        string b = Path.Combine(a, @"config\modules");
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
            ModifyMayaEnv(maya);
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
    public static void ModifyMayaEnv(string maya)
    {
        string temp_Dir = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
        string maya_env = Path.Combine(temp_Dir, @"maya\2022\Maya.env");
        if(File.Exists(maya_env))
        {
            string env_text = File.ReadAllText(maya_env,Encoding.UTF8);
            Match reg_config= Regex.Match(env_text, @"#QNCONFIG\n.*\n#QNCONFIGEND");
            if(reg_config.Success)
            {
                env_text=env_text.Remove(reg_config.Index,reg_config.Length);
            }
            env_text += $"\n\n\n#QNCONFIG\nMAYA_MODULE_PATH = {maya}\n#QNCONFIGEND\n";
            File.WriteAllText(maya_env, env_text, Encoding.UTF8);

        }
        else
        {
            //如何目录不存在就创建目录
            if(!Directory.Exists(Path.GetDirectoryName(maya_env)))
            {
                Directory.CreateDirectory(maya_env);
            }
            //写出配置
            File.WriteAllText(maya_env,$"#QNCONFIG\nMAYA_MODULE_PATH = {maya}\n#QNCONFIGEND\n",Encoding.UTF8);
        }
    }
}