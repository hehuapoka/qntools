using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MayaTaskManager
{
    public enum ServerCmdType { System,MayaPy,MayaPyStatus}
    public class ServerCmd
    {
        public ServerCmdType Cmd { get; set; }
        public string Args { get; set; } = "";
    }
}
