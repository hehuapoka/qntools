using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using Microsoft.Win32;
public static class env
{
    public static void Set()
    {
        Console.WriteLine("开始设置环境变量");

        
        Console.WriteLine("设置QNTOOLS");
        env.SetQNTOOLS();

        Console.WriteLine("设置MAYA_INSTALL_LOCATION");
        env.SetMayaLocaltion();

        Console.WriteLine("设置CGTEAMWORK_LOCATION");
        env.SetCgTeamWorkLocaltion();

        Console.WriteLine("设置OCIO");
        env.SetOCIO();

        Console.WriteLine("设置环境变量完成");
    }
    public static void SetQNTOOLS()
    {
        Environment.SetEnvironmentVariable("QNTOOLS", Path.GetFullPath(Directory.GetCurrentDirectory()), EnvironmentVariableTarget.User);
    }

    public static void SetPATH()
    {
        Environment.SetEnvironmentVariable("QNTOOLS", Path.GetFullPath(Directory.GetCurrentDirectory()), EnvironmentVariableTarget.User);
    }

    public static void SetOCIO()
    {
        Environment.SetEnvironmentVariable("OCIO", Path.GetFullPath(Path.Combine(Directory.GetCurrentDirectory(), @"config\aces_1.2\config.ocio")), EnvironmentVariableTarget.User);
    }
    public static void SetMayaLocaltion()
    {
        RegistryKey reg = Registry.LocalMachine;
        RegistryKey? MAYA_INSTALL_LOCATION = reg.OpenSubKey(@"SOFTWARE\Autodesk\Maya\2022\Setup\InstallPath");
        if (MAYA_INSTALL_LOCATION != null)
        {
            Object? a = MAYA_INSTALL_LOCATION.GetValue("MAYA_INSTALL_LOCATION");
            if (a != null)
                Environment.SetEnvironmentVariable("MAYA_INSTALL_LOCATION", Path.GetFullPath(Regex.Replace(a.ToString() ?? "", @"\\$", "")), EnvironmentVariableTarget.User);
        }
        else
        {
            Environment.SetEnvironmentVariable("MAYA_INSTALL_LOCATION", Path.GetFullPath(@"C:\Program Files\Autodesk\Maya2022"), EnvironmentVariableTarget.User);
        }
    }
    static void SetCgTeamWorkLocaltion()
    {
        RegistryKey reg = Registry.LocalMachine;
        RegistryKey? MAYA_INSTALL_LOCATION = reg.OpenSubKey(@"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{9FBC5986-4B24-40FD-8CD5-BE4E7E710EF9}_is1");
        if (MAYA_INSTALL_LOCATION != null)
        {
            Object? a = MAYA_INSTALL_LOCATION.GetValue("InstallLocation");
            if (a != null)
                Environment.SetEnvironmentVariable("CGTEAMWORK_LOCATION", Path.GetFullPath(Regex.Replace(a.ToString() ?? "", @"\\$","")), EnvironmentVariableTarget.User);
        }
        else
        {
            Environment.SetEnvironmentVariable("CGTEAMWORK_LOCATION", Path.GetFullPath(@"C:\CgTeamWork_v6.2"), EnvironmentVariableTarget.User);
        }
    }
}
