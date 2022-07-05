// See https://aka.ms/new-console-template for more information
using Microsoft.Win32;
using System.Diagnostics;




string s_cmds = $" {@"D:\hehua\dev\QNTools\scripts\cgteamwork\test.py"}";
ProcessStartInfo processInfo = new ProcessStartInfo($"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}", s_cmds)
{
    CreateNoWindow = true,
    UseShellExecute = true,
    WindowStyle = ProcessWindowStyle.Normal

};
Process process_task = new Process { StartInfo = processInfo };
process_task.Start();
process_task.WaitForExit();

Console.WriteLine(s_cmds);
