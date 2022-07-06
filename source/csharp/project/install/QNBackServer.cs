//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
//using System.Management;
//using System.Management.Automation;

//public static class QNBackServer
//{
//    public static void Set()
//    {
//        Console.WriteLine("开始安装QNBackServer");
//        string exe_path = Path.Combine(Path.GetFullPath(Directory.GetCurrentDirectory()),"bin");
//        //Runspace runspace= RunspaceFactory.CreateRunspace();
//        //runspace.Open();

//        //Pipeline pipeline= runspace.CreatePipeline();

//        //pipeline.Commands.AddScript($"sc.exe create QNBackServer binPath={exe_path}");
//        //pipeline.Commands.AddScript($"sc.exe config QNBackServer start=auto");
//        //pipeline.Commands.AddScript($"sc.exe start QNBackServer");

//        //pipeline.Invoke();
//        //runspace.Close();
//        PowerShell.Create().AddScript($"sc.exe create QNBackServer binPath={exe_path}\nsc.exe config QNBackServer start=auto\nsc.exe start QNBackServer",true)
//            .Invoke();
//        Console.WriteLine("安装QNBackServer完成");
//    }
//}
