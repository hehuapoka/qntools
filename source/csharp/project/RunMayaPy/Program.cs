// See https://aka.ms/new-console-template for more information
using Microsoft.Win32;
using System.Diagnostics;
using System.Text.Json;
using MayaTaskManager;



//ProcessStartInfo processInfo = new ProcessStartInfo($"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}", s_cmds)
//{
//    CreateNoWindow = true,
//    UseShellExecute = true,
//    WindowStyle = ProcessWindowStyle.Normal

//};
//Process process_task = new Process { StartInfo = processInfo };
//process_task.Start();
//process_task.WaitForExit();
//#if DEBUG
//args = new string[] { "D:\\hehua\\dev\\QNTools\\scripts\\cgteamwork\\test.py" };
//#endif
//using(Process pc = new Process())
//{
//    pc.StartInfo.FileName = $"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}";
//    pc.StartInfo.Arguments = String.Join(' ',args);
//    pc.StartInfo.CreateNoWindow = true;
//    pc.StartInfo.UseShellExecute = true;
//    pc.Start();
//    pc.WaitForExit();
//}
TaskServer a = new TaskServer("127.0.0.1", 10340);
await a.Start();
//string data="{\"Cmd\":1,\"Args\":\"D:\\\\hehua\\\\dev\\\\QNTools\\\\scripts\\\\cgteamwork\\\\test1.py\"}";
//Console.WriteLine(data);
//Console.WriteLine(JsonSerializer.Serialize(new ServerCmd() { Args= @"D:\hehua\dev\QNTools\scripts\cgteamwork\test1.py"}));
//ServerCmd? cmd = JsonSerializer.Deserialize<ServerCmd>(data);
Console.WriteLine("ok");
