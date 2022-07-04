using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Win32;

public static class UsdFormatConfig
{
    public static void Set()
    {
        Console.WriteLine("开始设置USD打开方式");
        if (File.Exists("bin\\usdformatconfig.json"))
        {
            string a = File.ReadAllText("bin\\usdformatconfig.json", System.Text.Encoding.UTF8);
            List<RegeditKey>? RegeditKeys = JsonSerializer.Deserialize<List<RegeditKey>>(a);
            if (RegeditKeys != null)
            {
                RegistryKey reg = Registry.ClassesRoot;
                foreach (RegeditKey item in RegeditKeys)
                {
                    //clean
                    RegistryKey? bkey = reg.OpenSubKey(item.Name);
                    if (bkey != null)
                    {
                        reg.DeleteSubKeyTree(item.Name);

                    }
                    reg.CreateSubKey(item.Name);


                    CreateFormat(item, item.Name, reg);
                }


            }
        }
        //设置文件格式打开方式
        Console.WriteLine("设置USD打开方式完成");
    }
    public static void CreateFormat(RegeditKey ra, string ckey, RegistryKey ks)
    {
        string install_dir = Path.GetFullPath(Directory.GetCurrentDirectory());
        RegistryKey mykey = ks.CreateSubKey(ckey);
        foreach (var v in ra.Values)
        {
            if (ra.Name == "command")
            {
                if (v.Name == "Default" && v.Value != null)
                {
                    mykey.SetValue("", Path.Combine(install_dir, "bin", v.Value) + " \"%1\"");
                }
                else
                {
                    mykey.SetValue(v.Name, v.Value ?? "");
                }
            }
            else if (ra.Name == "DefaultIcon")
            {
                if (v.Name == "Default" && v.Value != null)
                {
                    mykey.SetValue(v.Name, Path.Combine(install_dir, "icon", v.Value ?? ""));
                }
                else
                {
                    mykey.SetValue(v.Name, v.Value ?? "");
                }
            }
            else
            {
                if (v.Name == "Icon")
                {
                    mykey.SetValue(v.Name, Path.Combine(install_dir, "icon", v.Value ?? ""));
                }
                else if (v.Name == "Default" && v.Value != null)
                {
                    mykey.SetValue("", v.Value);
                }
                else
                {
                    mykey.SetValue(v.Name, v.Value ?? "");
                }
            }
        }
        foreach (var rk in ra.Childrens)
        {
            CreateFormat(rk, $"{ckey}\\{rk.Name}", ks);
        }
    }
}