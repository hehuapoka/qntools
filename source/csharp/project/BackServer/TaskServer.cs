using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//using System.Text.Json;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using System.Diagnostics;
using Newtonsoft.Json;
using BackServer;
namespace MayaTaskManager
{
    public class TaskServer
   {
        private readonly ILogger<Worker> _logger;

        TcpListener listener;
        bool runing = true;

        Dictionary<string,MayaTask> mayaTasks = new Dictionary<string, MayaTask>();
        public TaskServer(string address,int port, ILogger<Worker> logger)
        {
            _logger = logger;
            this.listener = new TcpListener(IPAddress.Parse(address),port);
        }
        public async Task Start()
        {
            try
            {
                this.listener.Start();
                _logger.LogInformation("服务准备完成");
                while (runing)
                {
                    Byte[] bytes = new Byte[1024];

                    TcpClient client = await listener.AcceptTcpClientAsync();

                    _logger.LogInformation("Connected...");

                    NetworkStream stream = client.GetStream();
                    int i = 1;
                    i = await stream.ReadAsync(bytes, 0, bytes.Length);
                    string data = System.Text.Encoding.ASCII.GetString(bytes).Replace("\0", "");

                    _logger.LogInformation($"command: {data}");

                    ServerCmd? cmd = SolverCmd(data);

                    if (cmd != null)
                    {
                        if (cmd.Cmd == ServerCmdType.MayaPy)
                        {
                            string Id = AddNewMayaTask(cmd.Args);
                            await stream.WriteAsync(System.Text.Encoding.ASCII.GetBytes(Id));
                        }
                        else if (cmd.Cmd == ServerCmdType.MayaPyStatus)
                        {
                            bool Check = CheckMayaTask(cmd.Args);
                            await stream.WriteAsync(System.Text.Encoding.ASCII.GetBytes(Check.ToString()));
                        }
                        else if (cmd.Cmd == ServerCmdType.MayaAllPyStatus)
                        {
                            string Mess = CheckAllMayaTask();
                            await stream.WriteAsync(System.Text.Encoding.ASCII.GetBytes(Mess));
                        }
                    }


                    //foreach (var c in mayaTasks)
                    //{
                    //    Console.WriteLine($"{c.Key} ---- {c.Value.GetStatus()}\n\n\n");
                    //}

                    client.Close();


                }
            }
            catch(Exception e)
            {
                _logger.LogError(e.ToString());
            }    
                

        }
        public void Stop()
        {
            runing = false;
            this.listener.Stop();
        }
        private string AddNewMayaTask(string a)
        {
            Process pc = new Process();
                pc.StartInfo.FileName = $"{Path.Combine(Environment.GetEnvironmentVariable("MAYA_LOCATION") ?? "", "bin\\mayapy.exe")}";
            pc.StartInfo.Arguments = a;
            pc.StartInfo.CreateNoWindow = false;
            pc.StartInfo.UseShellExecute = false;
            pc.Start();

            //Console.WriteLine(a);
            MayaTask ac = new MayaTask(ref pc);
            mayaTasks.Add(ac.Id, ac);
            return ac.Id;
        }
        private bool CheckMayaTask(string a)
        {
            try
            {
                return mayaTasks[a].GetStatus();
            }
            catch(Exception e)
            {
                _logger.LogError(e.Message);
                return false;
            }
            
        }
        private string CheckAllMayaTask()
        {
            try
            {
                return JsonConvert.SerializeObject(mayaTasks);
            }
            catch (Exception e)
            {
                _logger.LogError(e.Message);
                return "{}";
            }

        }
        private ServerCmd? SolverCmd(string s)
        {
            return JsonConvert.DeserializeObject<ServerCmd>(s);
        }
    }
}
