// See https://aka.ms/new-console-template for more information
using Microsoft.Win32;
using System.Diagnostics;




//ProcessStartInfo processInfo = new ProcessStartInfo($"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}", s_cmds)
//{
//    CreateNoWindow = true,
//    UseShellExecute = true,
//    WindowStyle = ProcessWindowStyle.Normal

//};
//Process process_task = new Process { StartInfo = processInfo };
//process_task.Start();
//process_task.WaitForExit();
#if DEBUG
args = new string[] { @"E:\Work\dev\qntools\scripts\cgteamwork\test.py"};
#endif
using(Process pc = new Process())
{
    pc.StartInfo.FileName = $"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}";
    pc.StartInfo.Arguments = String.Join(' ',args);
    pc.StartInfo.CreateNoWindow = false;
    pc.StartInfo.UseShellExecute = false;
    pc.Start();
    pc.WaitForExit();
}
Console.WriteLine("ok");
