using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using System.Diagnostics;
namespace MayaTaskManager
{
    public class TaskServer
   {
        TcpListener listener;
        bool runing = true;
        Byte[] bytes = new Byte[1024];

        Dictionary<string,MayaTask> mayaTasks = new Dictionary<string, MayaTask>();
        TaskServer(string address,int port)
        {
            this.listener = new TcpListener(IPAddress.Parse(address),port);
        }
        public async Task Start()
        {
            try
            {
                this.listener.Start();
                while(runing)
                {
                    TcpClient client = await listener.AcceptTcpClientAsync();
                    NetworkStream stream = client.GetStream();
                    await stream.ReadAsync(bytes,0, bytes.Length);
                    string data = System.Text.Encoding.ASCII.GetString(bytes);
                    ServerCmd? cmd = SolverCmd(data);
                    if(cmd != null)
                    {
                        if(cmd.Cmd == ServerCmdType.MayaPy)
                        {
                            string Id=AddNewMayaTask(data);
#if DEBUG
                            await stream.WriteAsync(System.Text.Encoding.ASCII.GetBytes(Id));
#endif
                        }
                    }
#if DEBUG
                    foreach (var c in mayaTasks)
                    {
                        Console.WriteLine($"{c.Key}----{c.Value}");
                    }
#endif


                }

            }
            catch(Exception e)
            {

            }
        }
        public void Stop()
        {
            runing = false;
            this.listener.Stop();
        }
        private string AddNewMayaTask(string a)
        {

#if DEBUG
            a = "D:\\hehua\\dev\\QNTools\\scripts\\cgteamwork\\test.py" ;
#endif
            using (Process pc = new Process())
            {
                pc.StartInfo.FileName = $"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}";
                pc.StartInfo.Arguments = a;
                pc.StartInfo.CreateNoWindow = false;
                pc.StartInfo.UseShellExecute = true;
                pc.Start();
                MayaTask ac=new MayaTask { Proc = pc };
                mayaTasks.Add(ac.Id, ac);
                return ac.Id;
            }

           return "";
        }
        private ServerCmd? SolverCmd(string s)
        {
            return JsonSerializer.Deserialize<ServerCmd>(s);
        }
    }
}
