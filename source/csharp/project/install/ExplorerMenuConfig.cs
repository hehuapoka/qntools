using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Win32;

public static class ExplorerMenuConfig
{
    public static void Set()
    {
        //创建管理器右键菜单
        Console.WriteLine("开始Window文件管理器右键菜单");

        if (File.Exists("bin\\menuconfig.json"))
        {
            string a = File.ReadAllText("bin\\menuconfig.json", System.Text.Encoding.UTF8);
            RegeditKey? menus = JsonSerializer.Deserialize<RegeditKey>(a);
            if (menus != null)
            {
                RegistryKey reg = Registry.ClassesRoot;
                RegistryKey? bkey = reg.OpenSubKey(@"Directory\Background\shell\QNTools");
                if (bkey != null)
                {
                    reg.DeleteSubKeyTree(@"Directory\Background\shell\QNTools");

                }
                reg.CreateSubKey(@"Directory\Background\shell\QNTools");


                CreateMenu(menus, @"Directory\Background\shell\QNTools", reg);


            }
        }
        else
        {
            Console.WriteLine("配置文件menuconfig.json不存在");
        }
        Console.WriteLine("Window文件管理器右键菜单完成");
    }
    public static void CreateMenu(RegeditKey ra, string ckey, RegistryKey ks)
    {
        string install_dir = Path.GetFullPath(Directory.GetCurrentDirectory());
        RegistryKey mykey = ks.CreateSubKey(ckey);

        foreach (var v in ra.Values)
        {
            if (ra.Name == "command")
            {
                if (v.Name == "Default" && v.Value != null)
                {
                    mykey.SetValue("", Path.Combine(install_dir, "bin", v.Value));
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
                else
                {
                    mykey.SetValue(v.Name, v.Value ?? "");
                }
            }
        }
        foreach (var rk in ra.Childrens)
        {
            CreateMenu(rk, $"{ckey}\\{rk.Name}", ks);
        }
    }
}

